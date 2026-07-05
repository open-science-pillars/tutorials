# Demo script: the ECCO-to-report story (surface-neutral)

One take, about six minutes, runnable verbatim on Claude Code, Cowork,
or Claude Science (on surfaces without Earthdata credentials the story
plays through planning and gates, which is itself the point). Session
13; the recording follows this script.

## Setup (before recording)

Both plugins installed; a project directory with `ocean-science.local.md`
filled (2 GB gate); on Code, the ECCO 2010 cache warm so downloads
do not dominate the take.

## Beat 1 (0:00): the question

Say exactly:

> How did the Atlantic's meridional heat transport at 26.5N in ECCO
> compare with the RAPID observations during the 2010 AMOC minimum?
> Plan the data before touching anything.

Camera focus: the PLAN. It cites knowledge concepts by name (the
regridded-budget rule, the no-formal-errors framing, the recipe's
expected range), estimates volumes, and downloads nothing.

## Beat 2 (1:00): the gate

Approve the plan. Focus: the loader states granule counts and sizes
BEFORE fetching; if the request had exceeded the gate, it would have
stopped and offered alternatives (mention the 7.25 TB request it once
stopped).

## Beat 3 (2:00): the scope lesson

Focus: the analysis distinguishes the Atlantic section (0.666 PW in
2010) from the full latitude circle (1.098 PW), and says WHY the
RAPID-comparable number is the Atlantic one. One sentence to camera:
"the project's own verification loop caught this distinction; the
recipe now teaches it."

## Beat 4 (3:30): the comparison

Focus: real RAPID/MOCHA observations fetched by DOI, matched windows,
correlation quoted, and the judgment: the offset sits INSIDE the
recipe's comparison spread, so no disagreement is declared. Honesty is
the feature: 2010 sits low because the ocean did that.

## Beat 5 (4:30): the report

Say: "Write this up as a report." Focus: the confirmation gate
(filename and sections BEFORE writing), then in the report: every
headline number carries an uncertainty statement, and Provenance cites
the knowledge concepts by bundle path.

## Beat 6 (5:30): the close

One line: "Skills act, knowledge bundles remember, verification keeps
both honest: and everything you just saw is open, inspectable, and
installable from github.com/open-science-pillars." Show the org page.
Optionally show the browser-runnable WASM companion (demo/wasm/) for
the audiences who want to touch the numbers without installing
anything.
