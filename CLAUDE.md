# CLAUDE.md — Oxford Physics Application Project

## Purpose

This document defines the working context, priorities, and research methodology
for supporting Philip's application to read Physics (F303) or Physics &
Philosophy (VF53) at the University of Oxford.

It exists to keep effort focused on variables that actually move the outcome,
rather than on what is easy to measure.

---

## Candidate Profile (working assumptions)

- Year 12 at time of writing
- Selective state school (non-private)
- Strong STEM GCSEs; one grade 6 in English Literature
- Target courses: Physics (F303), possibly Physics & Philosophy (VF53)
- Has completed Balliol's "Try Before You Buy" Physics taster programme
- Has published an independent dimensional-analysis project (Trinity test
  shockwave power law) as a Streamlit app with GitHub source
- No contextual flag (POLAR/ACORN) expected to apply

---

## Honest Priority Ranking

Effort distribution should approximate:

| Priority | Activity                          | Share of effort |
|----------|-----------------------------------|-----------------|
| 1        | ESAT preparation                  | ~50%            |
| 2        | Interview technique               | ~20%            |
| 3        | Personal statement                | ~10%            |
| 4        | Independent physics/maths depth   | ~10%            |
| 5        | College choice analysis           | ~5%             |
| 6        | FOI / admissions process research | ~5%             |

The previous ChatGPT project had this roughly inverted. Do not repeat that.

---

## What Actually Decides the Outcome

1. **ESAT score** — primary shortlisting filter. Highest leverage variable
   under candidate control.
2. **A-level predicted grades** — A*A*A* in Maths, Further Maths, Physics is
   the expected baseline.
3. **Interview performance** — decisive once shortlisted. Tests live
   thinking under pressure, not content recall.
4. **Personal statement and academic context** — used as supporting
   evidence, not as a primary filter.
5. **College choice** — small marginal effect, mostly absorbed by Oxford's
   reallocation system. Avoid two or three persistently oversubscribed
   colleges; otherwise pick by fit.

GCSEs are used as context only. There is no formal GCSE requirement for
Physics. A grade 6 in English Literature is not a meaningful risk for this
profile.

---

## Research Methodology (for any quantitative claim)

Any statistical claim about colleges, shortlisting rates, or offer
probabilities must follow these rules:

### Data sources, in order of trust

1. Oxford Annual Admissions Statistical Report (official, multi-year aggregates)
2. Oxford Undergraduate Admissions Statistics dataset (per-course, per-college)
3. WhatDoTheyKnow FOI disclosures with attached spreadsheets
4. Department of Physics admissions page and annual admissions report
5. HESA cross-institutional data (for benchmarking only)

Do not use Student Room threads, unofficial spreadsheets, or single-source
forum posts as primary evidence. They are useful only as pointers to
official documents.

### Statistical hygiene

- Use **three-year or five-year rolling averages**. Never quote a
  single-year college-level percentage as decision-relevant.
- Compute **Wilson score confidence intervals** for every rate involving
  fewer than ~50 candidates.
- Apply **Bayesian shrinkage** toward the Oxford-wide Physics mean
  (~30% shortlist rate). Shrinkage factor proportional to sample size.
- Report **rank changes after shrinkage**, not raw ranks. Most apparent
  top-college effects disappear after shrinkage.
- Note **suppressed cells** (asterisks in FOI tables) explicitly. Do not
  impute values silently.

### Decomposition discipline

When discussing college-level effects, decompose into:

- **Applicant-pool effect** (who self-selects to apply there)
- **Capacity effect** (Physics places per applicant — the only cleanly
  measurable signal)
- **Reallocation effect** (how much the pool corrects initial mistakes)
- **Residual college-specific effect** (usually within noise)

If a claim cannot be assigned to one of these buckets, it is probably folk
wisdom.

### Forbidden reasoning patterns

- "College X shortlists at 40% so it is easier" — without checking pool quality
- "Univ is bad for non-contextual candidates" — without evidence of conditional rates
- "Christ Church is intimidating" — aesthetic claim, not statistical
- Ranking colleges to one decimal place
- Repeating Student Room received wisdom as fact

---

## Open Research Backlog

Items marked `[high]` are worth doing. Items marked `[low]` are tempting but
low-yield.

### ESAT preparation
- [ ] [high] Establish baseline ESAT score from a clean past-paper attempt
- [ ] [high] Build weekly past-paper rotation (PAT legacy papers + ESAT specimen)
- [ ] [high] Identify weakest module among Maths I, Maths II, Physics
- [ ] [high] Work through BPhO Round 1 problems as supplementary practice
- [ ] [med] Isaac Physics progression to Challenge level

### Interview preparation
- [ ] [high] Schedule mock interviews with someone willing to push back
- [ ] [high] Practice thinking aloud on unfamiliar problems
- [ ] [high] Read Feynman Lectures Vol I selectively for conceptual depth
- [ ] [med] Review Oxford Physics interview question archives (official only)
- [ ] [med] Practice extending the dimensional analysis project under questioning

### Personal statement
- [ ] [high] Draft v1 around the Trinity dimensional analysis project
- [ ] [high] Include what was hard and what remained unanswered
- [ ] [med] Brief mention of P&P angle if applying for both courses
- [ ] [low] LinkedIn polish (already drafted; not application-critical)

### College choice (limited budget)
- [x] Build 30-college data template (`data/college_physics_raw.csv`) with confirmed schema
- [x] Confirm Oxford-wide shortlist prior: 30.5% (492/1633, 536/1672, 525/1790 for 2022–2024)
- [x] Confirm Keble data from college-specific feedback PDFs (3 years: 141/35, 120/30, 127/23)
- [x] Confirm intake numbers: Keble=8, Balliol=8, St Hugh's=6, University=10, Wadham=8
- [x] Build full analysis notebook (`analysis/oxford_physics_colleges.ipynb`) with Wilson CI, Bayesian shrinkage (K=20, prior 30.5%), AVOID flags, capacity signal, and summary output
- [x] ~~Identify Keble as AVOID~~ — **REVISED**: Keble acceptance rate 12.1% ≈ Oxford mean 11.9%; reallocation corrects shortlist disadvantage; Keble AVOID flag retracted
- [x] Obtain per-college data: downloaded WhatDoTheyKnow FOI 2025 (`data/foi_physics_college_2025.xlsx`) — direct-applicant acceptance rates for all 29 colleges, 2022–2024
- [x] Run full analysis on FOI data: Wilson CI, Bayesian shrinkage (K=20, prior 11.9%), AVOID flags for all 29 colleges
- [x] Identify Worcester College as AVOID: shrunk acceptance rate 6.7%, Wilson CI upper bound 10.4% < Oxford mean 11.9%; consistent across 2yr (2023 suppressed) — `output/college_physics_summary.md`
- [ ] [med] Identify if University College or Trinity warrant caution (both ~8.5–8.7% raw, within Wilson CI of mean; watch but not statistically AVOID)
- [ ] [med] Visit shortlisted colleges in person if feasible
- [ ] [low] Adjust for "access college" effects without conditional data
- [ ] [low] Draft additional FOI requests for shortlist-level per-college data (to cross-check acceptance-rate analysis)

### Process understanding
- [x] Identify that Physics shortlisting is department-led
- [x] Draft FOI request for Physics admissions procedures document
- [x] Confirm Annual Admissions Statistical Report requires browser access (HTTP 403 programmatically — all years)
- [ ] [med] Track response from the FOI request
- [ ] [low] Search for further admissions manuals

---

## Decision Log

Record significant decisions and the reasoning, so we can revisit them later.

| Date       | Decision                                    | Reasoning |
|------------|---------------------------------------------|-----------|
| 2026-05-18 | Pivot effort from college analysis to ESAT  | College effect statistically small after shrinkage; ESAT is highest-leverage variable |
| 2026-05-18 | Keble AVOID flag retracted                  | FOI 2025 acceptance-rate data shows Keble direct applicants succeed at 12.1% ≈ Oxford mean 11.9%. Previous AVOID flag used shortlist rates (pre-reallocation), which overstate the disadvantage. Reallocation corrects Keble's oversubscription. |
| 2026-05-18 | Worcester College flagged AVOID             | Acceptance rate 6.7% shrunk (lower bound); Wilson CI upper bound 10.4% < Oxford mean 11.9%; consistent 2yr; most likely applicant-pool quality effect but enough evidence to avoid. |
| 2026-05-18 | Annual Report does not contain per-college Physics data | 2025 Annual Admissions Statistical Report (downloaded via Playwright) is structured by demographic variable (ACORN, POLAR, gender, ethnicity); no per-college per-subject cross-tab. |
| 2026-05-18 | FOI 2025 is primary data source for college analysis | WhatDoTheyKnow FOI to Oxford, July 2025: direct-applicant acceptance rates for all 29 colleges, UCAS cycles 2019–2024. Metric incorporates reallocation; most useful for college choice. |
| 2026-05-11 | LinkedIn post published                     | Real artefact from Balliol taster programme; useful for interview talking-point, not for admissions per se |

---

## Working Principles

1. **Honest over comforting.** If the data does not support a conclusion,
   say so. The previous project optimised for the appearance of insight.
2. **Effort follows leverage.** Spend time where it changes the outcome.
3. **Single-year college numbers are not insight.** They are noise.
4. **The application is one decision, not many.** Avoid analysis paralysis
   on college choice; the marginal hour is almost always better spent on
   ESAT or interview practice.
5. **Anything unfalsifiable is folk wisdom.** Including claims about which
   colleges are "more academic" or "more accessible" without conditional
   data.

---

## What This Document Is Not

- Not a substitute for the official Oxford admissions guidance
- Not financial, legal, or formal academic advice
- Not a guarantee of outcomes — Oxford Physics admits roughly 1 in 9
  applicants; even strong candidates are rejected

---

*Last updated: 2026-05-18 (college analysis — FOI data session; Keble retracted, Worcester flagged)*