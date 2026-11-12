# volshi.com — unified rebuild (Stitch export, hand-cleaned)

Branch `stitch-rebuild`, 2026-11-12. The previous site is preserved
whole under `old/`. This root is the new unified site, built from the
Stitch export with every invented number/ID/hash/version stripped by
hand and verified by grep (see GOAL.md in the assistant's notes).

- `/` home, `/the-system/`, `/katie/`, `/research/` (research + invest
  sections), `/invest/` redirects to `/research/#invest`.
- `/mobile/*` mirrors for narrow viewports; desktop pages redirect
  there under 768px.
- `stitch-variants/` holds superseded Stitch generations, kept for
  reference. One stale variant (home_1) was excluded: it was the only
  file containing invented research-paper titles.
- Images are hotlinked to Stitch's Google-hosted URLs for now;
  localizing them to `assets/` is still open.
