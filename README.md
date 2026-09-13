# tutorials

The Open Science Pillars tutorial book (Quarto): three timed,
fresh-install-tested walkthroughs plus the demo assets. New to a term
(runtime, golden notebook, WASM)? See the
[glossary](https://github.com/open-science-pillars/marketplace/blob/main/GLOSSARY.md).

**Prerequisite:** Claude Code with the marketplace added
(`claude plugin marketplace add open-science-pillars/marketplace`), or
Claude Cowork with the same marketplace added under plugins. Start with
Tutorial 1; the other two assume it.

- [Tutorial 1, Getting Started](tutorial-1-getting-started.qmd): install
  core, orient, quality-control a test dataset, produce an anomaly analysis.
  Measured 4.6 minutes fresh.
- [Tutorial 2, ECCO Heat Transport with a SWOT coda](tutorial-2-ecco-mht.qmd):
  real PO.DAAC data through the volume gate, meridional heat transport at
  26.5N against RAPID, a report with provenance. Measured 15.0 minutes fresh
  including downloads.
- [Tutorial 3, Build a Domain Plugin](tutorial-3-build-a-plugin.qmd): from
  the plugin template to an installed capability with one gated skill, one
  evidence-linked concept and one green golden notebook. Measured 12.3
  minutes scaffold-to-installed.
- [index.qmd](index.qmd): the book's front page, with the setup per runtime.
- [demo/](demo/): the script of the recorded launch demo and the
  browser-runnable (WASM) meridional heat transport (MHT) companion (no
  install, no credentials).

The timings are measured on Claude Code. Runtime status, stated the same way
on the index page and in every tutorial header: Claude Code supported;
Claude Cowork tested, per-release qualification in progress; Claude Science a
future runtime.

Build locally with `quarto render`. Applied-tutorial authors start from
[templates/arset-style.md](templates/arset-style.md). License: Apache-2.0.
