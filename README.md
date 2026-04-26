# eml-jupyter — ARCHIVED

> **🗄  This package is archived as of 2026-04-25 (E-129 consolidation).**
>
> The functionality has been folded into the main `monogate` package
> as of `monogate 2.4.0+`. New users should install:
>
> ```bash
> pip install monogate[jupyter]
> ```
>
> and load via:
>
> ```python
> %load_ext monogate.jupyter
> ```
>
> The standalone `eml-jupyter` PyPI / GitHub package is **frozen at
> 0.1.2** and will receive no further updates. The `Lean-verified`
> pill on the display panel now reads green-with-link (Universality.lean
> was user-verified 2026-04-25) for any expression in the EML class —
> this is automatic via the bundled `monogate.witness` module.
>
> See [monogate's CHANGELOG entry for 2.4.0](https://github.com/almaguer1986/monogate/blob/master/python/CHANGELOG.md#240--2026-04-25--universality-witness--cli--jupyter-folded-in)
> for details.

---

# eml-jupyter (historical)

Rich notebook display + cell magic for the EML substrate. Annotate
every SymPy expression in a Jupyter cell with its Pfaffian profile,
registry identification, and (eventually) Lean-verification badge.

## Install

```bash
pip install 'eml-jupyter[notebook]'
```

## Quick start

In a notebook cell:

```python
%load_ext eml_jupyter

import sympy as sp
x = sp.Symbol('x')

1 / (1 + sp.exp(-x))
```

You see the LaTeX rendering AS WELL AS a panel below it showing:

```
┌───────────────────────────────────────────────────────────┐
│ EML witness for 1/(1 + exp(-x))                           │
│                                                            │
│ predicted_depth                  2                         │
│ pfaffian_r                       1                         │
│ ...                                                        │
│ fingerprint        p1-d2-w1-c-1-h534bee                    │
│                                                            │
│ ┌───────────────────────────────────────────────────────┐ │
│ │ sigmoid (canonical)  (exact · ml)                      │ │
│ │ Logistic sigmoid 1/(1+e^-x).                           │ │
│ └───────────────────────────────────────────────────────┘ │
│                                                            │
│ Lean-verified: pending (EML_Universality.lean not yet     │
│   user-verified in VS Code lean4 extension)               │
└───────────────────────────────────────────────────────────┘
```

The panel is colour-coded by severity:

- low (`predicted_depth ≤ 2`) — green left border
- mid (`predicted_depth 3-4`) — amber left border
- high (`≥5` or `is_pfaffian_not_eml`) — red left border

## Cell magic

```python
%%eml_witness
sp.exp(x) / (1 + sp.exp(x))
```

The cell body is evaluated as a Python expression. The result is
fed through `eml_witness.universality_witness` and the panel
rendered below — including the canonical-equivalent path
when one exists.

## Lean integration story

The "Lean-verified" pill at the bottom of every panel is wired
directly to `UniversalityWitness.verified_in_lean`. While that
flag is `False` (the default until `EML_Universality.lean` is
written, compiles cleanly under lake, AND is verified by the
user in VS Code lean4 extension), the pill reads "pending".
Once the flag flips, the pill turns green and links to the
Lean source on GitHub.

## Status

Beta. v0.1.0. Patent pending. Pure Python; the only optional
dependency is `ipython` (under the `notebook` extra) — the
package's rendering helpers (`render_witness_html`,
`render_witness_text`) work standalone in any Python context.
