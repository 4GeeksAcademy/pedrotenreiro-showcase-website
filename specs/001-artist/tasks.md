## Editable Data

- [x] Define the editable `data/artist.json` structure and populate it with fictional demo profile, biography, portrait metadata, repertoire, offerings, contact, location, and sample event data.

## JSON Rendering and Page Structure

- [x] Update the existing Flask route to load `data/artist.json` and render the page server-side without adding client-side JavaScript or dependencies.
- [x] Build semantic page markup with the `#hero`, `#about`, `#experience`, and `#events` sections and matching header navigation.
- [x] Render artist details and visible fictional-demo labeling from the JSON source rather than duplicating artist-specific content in the markup.
- [x] Add accurate page metadata and static Schema.org data based on the rendered JSON; do not represent fictional sample events as real events.

## Design and Accessibility

- [x] Implement the mobile-first visual design in external `style.css` using Flexbox and viewport-height minimums that allow sections to expand.
- [x] Add accessible image alternatives, heading structure, keyboard navigation, visible focus states, and sufficient contrast.

## Verification

- [x] Verify JSON edits are reflected in rendered output and invalid or missing data is handled without exposing mock information as fact.
- [x] Validate HTML and JSON-LD, confirm stylesheet loading, and review keyboard access and mobile/desktop layouts for clipping, overlap, and horizontal scrolling.
