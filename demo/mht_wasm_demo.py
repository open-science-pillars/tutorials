# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo", "numpy", "matplotlib"]
# ///
# WASM companion demo (Session 13): the ECCO 2010 MHT story in the
# browser, no install, no credentials. Data embedded below are the
# build's verified 2010 values (recipes/ecco-mht-26n.md provenance:
# computed live from PO.DAAC granules, 2026-07-04, and asserted by the
# transport_analysis golden notebook).

import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np

    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # ECCO v4r4 meridional heat transport at 26.5N, 2010, PW.
    GLOBAL = np.array([-0.313, -0.115, 1.031, 1.303, 1.234, 1.629,
                       1.922, 1.897, 1.670, 1.500, 1.211, 0.206])
    BASINS = {"Atlantic (atlExt)": 0.666, "Pacific (pacExt)": 0.430,
              "Indian (indExt)": 0.002}
    RAPID_SPREAD = 0.40   # PW, temporal std (Johns et al. 2011)
    RAPID_MEAN = 1.33     # PW, 2004-2007
    return BASINS, GLOBAL, MONTHS, RAPID_MEAN, RAPID_SPREAD, mo, np


@app.cell
def _(mo):
    mo.md(
        """
# The 2010 AMOC minimum, in your browser

ECCO v4r4 meridional heat transport at **26.5N** through 2010, the
documented AMOC-minimum year. Verified values from the
[Open Science Pillars](https://github.com/open-science-pillars) build:
computed live from PO.DAAC granules and locked in by a golden notebook.

**The scope lesson:** a latitude line without a basin mask is the FULL
circle. The RAPID-comparable number is the Atlantic one.
"""
    )
    return


@app.cell
def _(mo):
    show_rapid = mo.ui.checkbox(label="Show the RAPID comparison envelope (Atlantic scope only)", value=True)
    show_rapid
    return (show_rapid,)


@app.cell
def _(BASINS, GLOBAL, MONTHS, RAPID_MEAN, RAPID_SPREAD, mo, np, show_rapid):
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 3.6),
                                   gridspec_kw={"width_ratios": [2, 1]})
    ax1.axhline(0, color="0.8", lw=0.8)
    ax1.plot(MONTHS, GLOBAL, "o-", color="#20669c", label="Global circle, monthly")
    ax1.axhline(GLOBAL.mean(), color="#20669c", ls="--", lw=1,
                label=f"Global 2010 mean {GLOBAL.mean():.3f} PW")
    atl = BASINS["Atlantic (atlExt)"]
    ax1.axhline(atl, color="#c25a1e", ls="-", lw=1.6,
                label=f"Atlantic 2010 mean {atl:.3f} PW")
    if show_rapid.value:
        ax1.axhspan(RAPID_MEAN - RAPID_SPREAD, RAPID_MEAN + RAPID_SPREAD,
                    color="#c25a1e", alpha=0.12,
                    label=f"RAPID 2004-2007: {RAPID_MEAN} +/- {RAPID_SPREAD} PW")
    ax1.set_ylabel("MHT at 26.5N (PW)")
    ax1.set_title("ECCO v4r4, 2010")
    ax1.legend(fontsize=7, loc="lower center")

    names = list(BASINS) + ["Sum", "Global (no mask)"]
    vals = list(BASINS.values()) + [sum(BASINS.values()), float(GLOBAL.mean())]
    colors = ["#c25a1e", "#20669c", "#6a6a6a", "#333333", "#7b2d8b"]
    ax2.bar(range(5), vals, color=colors)
    ax2.set_xticks(range(5), ["Atl", "Pac", "Ind", "Sum", "Circle"], fontsize=8)
    ax2.set_ylabel("2010 mean (PW)")
    ax2.set_title("Basin sum = full circle")
    fig.tight_layout()
    caption = mo.md(
        f"""
*Left: the global-circle monthly series swings from {GLOBAL.min():.2f}
to {GLOBAL.max():.2f} PW; the deep winter dips are the AMOC minimum.
Right: the basin decomposition sums to the circle exactly
({sum(BASINS.values()):.3f} = {GLOBAL.mean():.3f} PW), which is how the
scope error was caught. The Atlantic 2010 mean sits below the RAPID
2004-2007 envelope because 2010 was anomalous, and single-year means
carry a wider envelope: uncertainty framing per the project recipe.*
"""
    )
    mo.vstack([mo.as_html(fig), caption])
    return


if __name__ == "__main__":
    app.run()
