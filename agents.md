# Agent Instructions

## Project
Build and maintain a modern, responsive personal website for an artist. Keep the experience focused on the artist, their practice, selected work, biography, and contact details.

## Implementation Constraints
- Use semantic HTML for page structure and meaningful landmarks.
- Keep styling in the separate `style.css` file and connect it from the HTML document with a stylesheet link. Do not add inline styles.
- Use CSS Flexbox for layout. Make layouts mobile-first and responsive without relying on fixed page widths.
- Use plain HTML and CSS only. Do not add JavaScript, frameworks, build tools, or third-party UI libraries.
- Keep changes focused and preserve the existing lightweight static-site setup.

## Design
- Create a polished, contemporary visual identity suited to the artist and their work; prioritize the artwork and clear navigation.
- Use a deliberate type and color system with readable text, consistent spacing, and restrained visual effects.
- Ensure navigation, images, and content adapt cleanly to small and large screens without clipping or horizontal scrolling.

## Accessibility
- Set the document language and use a logical heading hierarchy, landmarks, and descriptive link text.
- Provide meaningful alternative text for informative images; use empty alt text for purely decorative images.
- Ensure all interactive elements work with a keyboard, have visible focus states, and have sufficient color contrast.
- Do not communicate meaning through color alone. Respect reduced-motion preferences if motion is introduced.

## SEO and GEO
- Give each page a unique, accurate title and meta description, and include the appropriate language, viewport, canonical URL, and social-sharing metadata when the required values are known.
- Make the artist's name, discipline, biography, and artwork descriptions clear, accurate, and consistent in visible page content. Use descriptive headings and links; avoid keyword stuffing and unsupported claims.
- Use descriptive image filenames and alt text, and provide relevant image dimensions to reduce layout shifts.
- Use structured data only when it accurately describes visible content. If needed, add static JSON-LD data; do not add executable JavaScript.

## Verification
- Check the HTML for valid structure and confirm the external stylesheet is loaded.
- Review the page at narrow and wide viewport sizes, and verify keyboard navigation, focus visibility, image alternatives, and text contrast.
- Do not introduce new tooling or dependencies just to perform checks.
