# Artist Landing Page Technical Plan

## Objective

Build the single-page artist website defined in [spec.md](spec.md), with editable JSON content and clearly labeled mock values for information not yet supplied by Jack. Keep the browser experience semantic, responsive, accessible, and free of JavaScript.

## Implementation Sequence

1. **Prepare the content model**
   - Add `data/artist.json` as the editable source of artist/site content.
   - Include known facts: Jack Reinhardt, musician, private and public concerts, cover music across varied genres and styles, and original music.
   - Represent unknown biography, approved portrait, location/service area, booking contact, profile URLs, repertoire examples, and public event details with explicit mock values or empty values. Mark every mock entry with a `mock` indicator; mock events must never be presented as real or included in public structured data.
   - Keep fields organized for biography, image metadata, offerings, experience/repertoire, contact, and public events so the archive can grow without changing the page structure.

2. **Render the page from the data**
   - Use the existing `server.py` / Flask serving path to load the JSON and render the page server-side, keeping client-side JavaScript out of the implementation.
   - Update `index.html` to use semantic landmarks and the required sections in order: `#hero`, `#about`, `#experience`, and `#events`. Header links target About Me, Experience, and Events.
   - Use mock values only as clearly identified draft content during development; exclude mock data from public-facing claims, event listings, and JSON-LD.
   - Add accurate title/description metadata and static Schema.org JSON-LD based only on confirmed visible content. Use `Person` for confirmed artist facts and `Event` only for confirmed public events.

3. **Style the responsive page**
   - Implement the visual system in the external `style.css` with mobile-first Flexbox.
   - Give each section approximately viewport height with a minimum height, allowing content to expand naturally.
   - Ensure layout, navigation, and imagery reflow without horizontal scrolling, clipping, or overlap.

4. **Validate and review**
   - Check HTML structure, Flask rendering, JSON parsing, and stylesheet loading.
   - Review mobile and desktop layouts, keyboard navigation, focus visibility, headings, image alternatives, and contrast.
   - Validate published JSON-LD and verify it matches visible, confirmed information. Run event-specific rich-result checks only when real public event data exists.

## Data-to-Page Constraint

A browser cannot populate ordinary HTML from a separate JSON file using HTML and CSS alone. The recommended path above uses the project's existing Flask server for server-side rendering; it adds no browser JavaScript and no new package, but it does use a server-side framework. This is a point of tension with `agents.md`, which says to use plain HTML and CSS only and not to add frameworks. Before implementation, treat existing Flask server-side rendering as an explicit exception to that constraint, or choose the strict-static alternative below.

**Strict-static alternative:** Keep `index.html` as hand-authored static markup and retain `data/artist.json` as a structured archive/reference for future editing. Content must then be copied manually into the HTML; the page will not consume the JSON automatically. This preserves the HTML/CSS-only constraint but does not meet automatic JSON consumption.

## Planned Files

- `index.html` — semantic page structure, navigation, visible content, metadata, and static JSON-LD.
- `style.css` — responsive visual styling and Flexbox layouts.
- `data/artist.json` — editable content archive with known facts and explicitly marked mock/unknown data.
- `server.py` — only if the server-rendered JSON path is selected; load data and render HTML on the server.
- `specs/001-artist/spec.md` — requirements and acceptance criteria.
- `agents.md` — project implementation constraints.

## Acceptance Checks

- Required IDs exist exactly once and header links point to their matching sections.
- Site copy and structured data do not present mock or unknown values as facts.
- Confirmed JSON data is the content source for the rendered page if the Flask rendering option is selected.
- Sections are approximately viewport-height without fixed-height clipping; mobile and desktop layouts have no overlap or horizontal scrolling.
- Keyboard access, visible focus, image alternatives, contrast, HTML validity, CSS loading, and structured data pass the spec's validation plan.
- No client-side JavaScript, frontend framework, or new dependency is introduced.
