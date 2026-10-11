# Verification

- All five SVGs parse as XML.
- All five SVGs render with Inkscape as static PNGs.
- All SVG image/font assets are inline data URIs; no HTTP(S) asset references are present.
- SVGs contain no JavaScript or `foreignObject`.
- The README uses all five required relative SVG paths with `?v=1`.
- The package has no contribution-city section.
- A deterministic no-animation render set is included under `preview/no-animation/`.
- Exact animation-time captures at 0/2/5/9/13 seconds were not synthesized because SVG SMIL timing is not reliably controllable by the static renderer used here; the SVGs use SMIL from 0s and have readable base states.
- The requested portrait and pointing-character files were not supplied in this conversation. The current SVGs therefore use a transparent 1×1 placeholder and include `scripts/embed_images.py` for exact later embedding.
