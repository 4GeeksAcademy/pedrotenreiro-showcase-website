try:
    # try to import flask, or return error if has not been installed
    from flask import Flask
    from flask import send_from_directory
    from flask import render_template
    from flask import Response
    from flask import request
except ImportError:
    print("You don't have Flask installed, run `$ pip3 install flask` and try again")
    exit(1)

import json
import gzip
import os

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), './')
app = Flask(__name__, template_folder=static_file_dir)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600


@app.after_request
def compress_text_response(response):
    compressible_types = {'text/html', 'text/css', 'application/json', 'image/svg+xml'}
    if (
        response.mimetype not in compressible_types
        or response.status_code in (204, 304)
        or response.headers.get('Content-Encoding')
        or request.accept_encodings.quality('gzip') <= 0
    ):
        return response

    response.direct_passthrough = False
    body = response.get_data()
    if len(body) < 500:
        return response

    response.set_data(gzip.compress(body, mtime=0))
    response.headers['Content-Encoding'] = 'gzip'
    response.headers.add('Vary', 'Accept-Encoding')
    return response


def has_text_fields(value, fields):
    return isinstance(value, dict) and all(isinstance(value.get(field), str) for field in fields)


def is_valid_artist_data(data):
    if not isinstance(data, dict) or data.get('dataStatus') != 'fictional-demo' or not isinstance(data.get('notice'), str):
        return False

    artist = data.get('artist')
    if not has_text_fields(artist, ('name', 'discipline', 'tagline')):
        return False

    biography = artist.get('biography')
    portrait = artist.get('portrait')
    repertoire = artist.get('repertoire')
    original_music = artist.get('originalMusic')
    contact = artist.get('contact')
    offerings = artist.get('offerings')
    events = artist.get('events')

    return (
        isinstance(biography, dict)
        and isinstance(biography.get('paragraphs'), list)
        and len(biography['paragraphs']) == 3
        and all(isinstance(paragraph, str) for paragraph in biography['paragraphs'])
        and biography.get('mock') is True
        and has_text_fields(portrait, ('alt',))
        and portrait.get('mock') is True
        and (portrait.get('src') is None or isinstance(portrait.get('src'), str))
        and all(portrait.get(size) is None or type(portrait.get(size)) is int for size in ('width', 'height'))
        and has_text_fields(repertoire, ('description',))
        and isinstance(repertoire.get('genres'), list)
        and all(isinstance(genre, str) for genre in repertoire['genres'])
        and isinstance(repertoire.get('songs'), list)
        and all(
            has_text_fields(song, ('title', 'artist', 'genre')) and song.get('mock') is True
            for song in repertoire['songs']
        )
        and repertoire.get('mock') is True
        and has_text_fields(original_music, ('description',))
        and original_music.get('mock') is True
        and isinstance(offerings, list)
        and all(has_text_fields(item, ('label', 'description')) and item.get('mock') is True for item in offerings)
        and has_text_fields(contact, ('email', 'label'))
        and contact.get('mock') is True
        and isinstance(events, list)
        and all(
            has_text_fields(event, ('name', 'startDate', 'venue', 'location', 'description'))
            and event.get('mock') is True
            for event in events
        )
    )


# Serving the index file
@app.route('/', methods=['GET'])
def serve_dir_directory_index():
    index_path = os.path.join(static_file_dir, 'index.html')
    if os.path.exists(index_path):
        artist_data_path = os.path.join(static_file_dir, 'data', 'artist.json')
        try:
            with open(artist_data_path, encoding='utf-8') as artist_data_file:
                artist_data = json.load(artist_data_file)
        except (OSError, json.JSONDecodeError, UnicodeError):
            return Response('Fictional demo content is temporarily unavailable.\n', status=503, mimetype='text/plain')
        if not is_valid_artist_data(artist_data):
            return Response('Fictional demo content is temporarily unavailable.\n', status=503, mimetype='text/plain')
        repertoire = artist_data['artist']['repertoire']
        genres = repertoire['genres']
        selected_genre = request.args.get('genre', 'All')
        if selected_genre not in genres and selected_genre != 'All':
            selected_genre = 'All'
        songs = repertoire['songs']
        if selected_genre != 'All':
            keyword = selected_genre.casefold()
            songs = [song for song in songs if keyword in song['genre'].casefold()]
        return render_template(
            'index.html',
            artist_data=artist_data,
            selected_genre=selected_genre,
            songs=songs,
        )
    else:
        return "<h1 align='center'>404</h1><h2 align='center'>Missing index.html file</h2><p align='center'><img src='https://github.com/4GeeksAcademy/html-hello/blob/main/.vscode/rigo-baby.jpeg?raw=true' /></p>"

# Serving any other image
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')
    response = send_from_directory(static_file_dir, path)
    return response

app.run(host='0.0.0.0',port=3000, debug=True, extra_files=['./',])
