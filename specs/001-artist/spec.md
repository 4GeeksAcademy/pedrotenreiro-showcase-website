# Artist Landing Page Specification

## Overview

Create a modern, responsive personal landing page for the fictional musician Jack Reinhardt. All artist, biography, repertoire, contact, and event details are fictional demo data stored in an editable JSON file. The website must use that JSON data to render its content. The site should introduce Jack, communicate his musical experience and offerings, and help visitors discover sample public events or inquire about a private concert.

## Goals

- Present Jack Reinhardt and his music clearly in the first viewport.
- Explain his biography, performance experience, repertoire, and concert offerings.
- Provide clear navigation to each main section and a path to event details or booking contact.
- Work accessibly across mobile and desktop viewports.
- Keep artist content in one editable JSON source and render the website from it.
- Identify the content as fictional demo data; do not present it as verified real-world information.
- Keep metadata and structured data consistent with the rendered demo content.

## Page Structure

Use one page with the following sections in this order. Each section must have the specified, unique `id`.

1. **Hero (`#hero`)**: Welcome visitors and introduce Jack Reinhardt as a musician. Clearly communicate that he performs cover and original music and offers public and private concerts. Include a primary link to events or booking information.
2. **About Me (`#about`)**: Present Jack's biography and a portrait. Use an informative, descriptive image alternative for the portrait.
3. **Experience (`#experience`)**: Describe performance experience and the range of cover music, genres, and styles, alongside original music. Include only confirmed repertoire or experience details.
4. **Events (`#events`)**: Present confirmed upcoming public concert information when available, and provide a way to inquire about private concerts. Do not represent private bookings as public events.

The header must contain a site title or artist name and navigation links labeled **About Me**, **Experience**, and **Events**, targeting `#about`, `#experience`, and `#events`. The hero is the home/top destination and must use `id="hero"`.

## Layout and Design

- Make each main section approximately one viewport tall using a minimum-height approach, such as `min-height: 100vh`; content must be allowed to expand beyond the viewport without clipping or overlap.
- Use a mobile-first responsive layout with CSS Flexbox. Do not rely on fixed page widths; prevent horizontal scrolling at narrow viewports.
- Give the page a deliberate, contemporary visual identity suited to a musician. Prioritize Jack, his music, and any relevant imagery over decoration.
- Use a consistent, readable type and color system, sufficient spacing, and restrained visual effects.
- Keep styling in the external `style.css` file linked from the HTML document. Do not use inline styles.

## Technical Constraints

- Use semantic HTML5 elements and meaningful page landmarks.
- Keep the browser experience to HTML and CSS; do not add client-side JavaScript, frontend frameworks, build tools, or third-party UI libraries.
- Store all artist content in an editable `data/artist.json` file, including clearly fictional demo values for biography, image, repertoire, booking/contact, location, and sample events.
- The website must consume `data/artist.json` to generate its rendered content; it must not duplicate artist data as hard-coded page content. Use the existing Flask server for server-side JSON loading/rendering, without adding dependencies.
- Keep the existing lightweight setup and do not add dependencies solely for this page.

## Accessibility

- Set the document language, use one clear page-level heading, and maintain a logical heading hierarchy.
- Use semantic navigation, main content, and section headings. Navigation labels must describe their destinations.
- Ensure all links are keyboard accessible, have visible focus indicators, and have sufficient text/background contrast.
- Provide descriptive alternative text for informative images; use empty alternative text for decorative images.
- Do not rely on color alone to convey meaning. If motion is introduced, respect the reduced-motion preference.
- Ensure text and controls reflow at narrow viewport widths without being clipped or overlapping.

## SEO, GEO, and Structured Data

- Provide an accurate page title and meta description, document language, and viewport metadata. Add canonical and social-sharing metadata only when the correct URL and image are known.
- Make the fictional artist identity, offerings, biography, and location clear in visible page text. Use natural language and avoid claims that imply the demo data is verified or real.
- Store geographic and contact details in the JSON data; label them as fictional demo information in the page.
- Add static Schema.org JSON-LD only when it matches the rendered content and is appropriate for a clearly fictional demo. Do not publish fictional sample events as real Event structured data.
- Keep all structured data consistent with the JSON source and visible page. Do not add executable JavaScript.

## Validation Plan

Before considering the page complete:

1. Validate the HTML structure with the W3C Nu HTML Checker and resolve errors introduced by the page.
2. Confirm `style.css` is linked and loads, and inspect the page at narrow mobile and wide desktop viewport sizes. Check for clipping, overlap, and horizontal scrolling.
3. Test navigation and all other links with a keyboard. Confirm visible focus, logical heading order, useful image alternatives, and adequate text contrast.
4. Validate any JSON-LD with the Schema.org Validator. If event markup is present, also check eligibility and errors with Google's Rich Results Test; do not add markup solely to obtain a rich result.
5. Confirm page content, metadata, and structured data come from or agree with `data/artist.json`, and that the fictional/demo status is clear.
6. Do not add test tools or dependencies to the project just to perform these checks.

## Acceptance Criteria

- The page contains `#hero`, `#about`, `#experience`, and `#events`, each exactly once.
- Header navigation links to About Me, Experience, and Events using the required IDs.
- The page introduces the fictional Jack Reinhardt and his private/public concert offerings, cover repertoire, and original music using data from `data/artist.json`.
- Artist data is editable in `data/artist.json`; changing its values changes the rendered page without duplicating those values in page markup.
- Fictional details and sample events are visibly identified as demo content and are not represented as verified real-world information.
- Sections are approximately viewport-height while expanding naturally when their content needs more space.
- Layout and navigation work at mobile and desktop sizes, with no horizontal scrolling or content overlap.
- Semantic structure, keyboard access, focus visibility, image alternatives, and contrast meet the accessibility requirements above.
- Metadata and any structured data match the rendered JSON content; fictional sample events are not marked up as real events.
- Implementation uses external CSS, server-side JSON rendering through the existing Flask server, and no client-side JavaScript, frontend frameworks, or added dependencies.

## JSON Data Requirements

`data/artist.json` is the editable source of artist-specific content. It should group the demo artist profile, biography, portrait and alternative text, genres/repertoire, original music, performance offerings, booking/contact details, location/service area, and sample public events. Values must be fictional and clearly labeled as demo data; event records must not be mistaken for real upcoming concerts. The server must read this file when rendering the page so edits to the JSON are reflected in the website.
