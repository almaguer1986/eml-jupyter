# Changelog

## [0.1.1] — 2026-04-25 — Audit fixes (cycle guard + assert→raise)

### Fixed
- **`_format_basic_text` now honours the IPython `cycle` flag.**
  Previously the parameter was discarded; under a recursive repr
  scenario the formatter could re-enter itself indefinitely. On
  cycle detection we now emit a compact `<EMLcycle: TypeName>`
  placeholder and bail.
- **`%%eml_witness` cell magic raises `RuntimeError` on missing
  shell** instead of using `assert self.shell is not None`.
  Asserts get stripped under `python -O` so the assert was
  effectively useless in optimised production runs.

## [0.1.0] — 2026-04-25 — Initial release

E-128 v0 substrate. Rich Jupyter / IPython display for the EML
substrate, plus a cell magic.

### Added

- **`%load_ext eml_jupyter`** — installs a display formatter for
  `sp.Basic`. Every SymPy expression evaluated in a cell renders
  with a Pfaffian-profile panel below the standard LaTeX output:
  predicted_depth, pfaffian_r, max_path_r, eml_depth, corrections,
  fingerprint, axes, identified registry match (when present),
  canonical-equivalent path (when one exists), and a
  Lean-verified pill. Severity-coloured left border (green / amber
  / red) by `predicted_depth`.
- **`%%eml_witness`** cell magic — evaluates the cell body as a
  Python expression, runs the result through
  `eml_witness.universality_witness`, and renders the witness
  panel.
- **`render_witness_html(w)` / `render_witness_text(w)`** — public
  helpers for embedding the panel anywhere (dashboards, blog
  posts, doc generators).
- **Idempotent install / uninstall** of the formatter; safe to
  load/unload repeatedly.

### Tests

- 14 cases — text + HTML render shape, severity colour for
  Bessel (high) vs canonical sigmoid (low), HTML escape safety,
  canonical-path inclusion, and IPython-integration smoke tests
  (skipped automatically when IPython isn't installed).
- mypy strict clean.

### Status

Beta. Pure Python. Patent pending. CI matrix mirrors the family.
