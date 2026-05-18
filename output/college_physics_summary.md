# Oxford Physics College Analysis — Summary

Generated from FOI 2025 data (per-college acceptance rates, direct applicants, 2022–2024).

---

## Data source and methodology

**Source**: WhatDoTheyKnow FOI response, University of Oxford, July 2025
File: `data/foi_physics_college_2025.xlsx` (51KB, 29 colleges × 6 cycles)

**Metric**: Acceptance rate for *direct* Physics applicants, attributed to the initially-applied
college. Acceptances include any college — the reallocation effect is therefore **already absorbed**.

This is the correct metric for college choice: "given Philip applies directly to college X,
what fraction of students in his position eventually get into Oxford Physics?"

**Why this is better than shortlist rates**: Shortlist rates (e.g., from Keble feedback PDFs)
capture only the pre-reallocation stage. Oxford explicitly reallocates oversubscribed candidates to
other colleges. Acceptance rates post-attribution capture the full pipeline.

**Exclusions**: Open applicants (~20% of all Physics applicants) are not included.
Wolfson College is absent from the FOI data (not listed).

---

## Oxford-wide prior

| Year | Direct apps | Accepted | Rate |
|------|-------------|----------|------|
| 2022 | 1353 | 167 | 12.3% |
| 2023 | 1325 | 156 | 11.8% |
| 2024 | 1358 | 156 | 11.5% |
| **3yr** | **4036** | **479** | **11.9%** |

Prior for Bayesian shrinkage: Beta(2.37, 17.63) ≡ 20 pseudo-observations at 11.9%.

---

## Full ranked table (direct-applicant acceptance rate, 3yr 2022–2024)

Sorted by shrunk rate (highest to lowest). Wilson CI and Bayesian CI use k_known as lower bound
for suppressed cells; those colleges are noted with suppression flag.

| Rank | College | Apps | Acc | Raw rate | Shrunk | 95% Wilson CI | AVOID | Note |
|------|---------|------|-----|----------|--------|---------------|-------|------|
| 1 | Merton College | 182 | 32 | 17.6% | 17.0% | [12.7%, 23.8%] | | |
| 2 | St Edmund Hall | 67 | 12 | 17.9% | 16.5% | [10.6%, 28.8%] | | |
| 3 | Lady Margaret Hall | 86 | 15 | 17.4% | 16.4% | [10.9%, 26.8%] | | |
| 4 | St Catherine's College | 130 | 22 | 16.9% | 16.2% | [11.5%, 24.3%] | | |
| 5 | St Anne's College | 81 | 14 | 17.3% | 16.2% | [10.6%, 26.9%] | | |
| 6 | Somerville College | 162 | 27 | 16.7% | 16.1% | [11.7%, 23.2%] | | |
| 7 | New College | 178 | 28 | 15.7% | 15.3% | [11.1%, 21.8%] | | |
| 8 | Christ Church | 157 | 23 | 14.6% | 14.3% | [10.0%, 21.0%] | | |
| 9 | Jesus College | 172 | 25 | 14.5% | 14.3% | [10.0%, 20.6%] | | |
| 10 | Exeter College | 117 | 16 | 13.7% | 13.4% | [8.6%, 21.1%] | | |
| 11 | Balliol College | 235 | 30 | 12.8% | 12.7% | [9.1%, 17.6%] | | |
| 12 | The Queen's College | 94 | 12 | 12.8% | 12.6% | [7.5%, 21.0%] | | |
| 13 | **Keble College** | 365 | 44 | 12.1% | 12.0% | [9.1%, 15.8%] | | |
| 14 | Wadham College | 125 | 15 | 12.0% | 12.0% | [7.4%, 18.9%] | | |
| 15 | Hertford College | 214 | 25 | 11.7% | 11.7% | [8.0%, 16.7%] | | |
| 16 | St John's College | 218 | 25 | 11.5% | 11.5% | [7.9%, 16.4%] | | |
| 17 | Magdalen College | 219 | 25 | 11.4% | 11.5% | [7.9%, 16.3%] | | |
| 18 | Mansfield College | 108 | 10† | 9.3% | 9.7% | [5.1%, 16.2%] | | 1yr suppressed |
| 19 | Brasenose College | 116 | 10† | 8.6% | 9.1% | [4.7%, 15.1%] | | 1yr suppressed |
| 20 | Trinity College | 172 | 15 | 8.7% | 9.1% | [5.4%, 13.9%] | | |
| 21 | Oriel College | 41 | 3† | 7.3% | 8.8% | [2.5%, 19.4%] | | 2yr suppressed |
| 21 | Pembroke College | 41 | 3† | 7.3% | 8.8% | [2.5%, 19.4%] | | 2yr suppressed |
| 23 | University College | 224 | 19 | 8.5% | 8.8% | [5.5%, 12.9%] | | |
| 24 | Lincoln College | 94 | 7† | 7.5% | 8.2% | [3.7%, 14.6%] | | 1yr suppressed |
| 25 | St Hilda's College | 54 | 3† | 5.6% | 7.3% | [1.9%, 15.1%] | | 2yr suppressed |
| 26 | St Peter's College | 68 | 4† | 5.9% | 7.2% | [2.3%, 14.2%] | | 2yr suppressed |
| 27 | **Worcester College** | 196 | 12† | 6.1% | 6.7% | [3.5%, 10.4%] | **AVOID** | 1yr suppressed |
| 28 | St Hugh's College | 75 | 3† | 4.0% | 5.7% | [1.4%, 11.1%] | | 2yr suppressed |
| 29 | Corpus Christi College | 45 | 0† | — | 3.7% | [0%, 7.9%] | | all suppressed |

† k_known is a lower bound. True acceptances ≥ shown value.
Oxford mean for reference: **11.9%** (prior).

---

## Revised verdict on Keble (rank 13)

**Keble is NOT flagged AVOID based on acceptance-rate data.**

Previous analysis used shortlist rates from Keble's own feedback PDFs
(141/35, 120/30, 127/23 — shortlisted/applied for 2022/2023/2024),
giving a raw shortlist rate of ~22.7% vs Oxford mean ~30.5%.
This appeared significantly below average.

The FOI data changes this conclusion:

| Year | Direct applicants (FOI) | Accepted | Rate |
|------|------------------------|----------|------|
| 2022 | 102 | 13 | 12.7% |
| 2023 | 142 | 16 | 11.3% |
| 2024 | 121 | 15 | 12.4% |
| 3yr | 365 | 44 | **12.1%** |

Bayesian shrunk rate: **12.0%** vs Oxford mean **11.9%** — essentially identical.
Wilson 95% CI: [9.1%, 15.8%] — comfortably straddles the Oxford mean.

**Decomposition**:
- Capacity effect (pre-reallocation): confirmed — Keble attracts many direct applicants (~122/yr
  for 8 places), so shortlist rates by Keble itself are suppressed.
- Reallocation effect: Keble reallocates strong candidates to other colleges, where they succeed.
  This reallocation is fully captured in the FOI acceptance rate.
- Residual post-reallocation effect: negligible — 12.1% ≈ 11.9% Oxford mean.

**Conclusion**: The initial AVOID flag on Keble was based on pre-reallocation shortlist rates,
which are an unreliable guide to actual success probability. **Keble applicants succeed at the
Oxford average rate.** Avoid Keble is retracted.

---

## Key finding: Worcester (rank 27, AVOID)

**Worcester College is flagged AVOID** based on acceptance-rate data.

| Year | Direct applicants | Accepted | Rate |
|------|------------------|----------|------|
| 2022 | 63 | 5 | 7.9% |
| 2023 | 52 | * (suppressed) | — |
| 2024 | 81 | 7 | 8.6% |
| 3yr | 196 | 12+ | **≤8.2%** |

Bayesian shrunk rate (lower bound): **6.7%** vs Oxford mean **11.9%**.
Wilson 95% CI upper bound: **10.4%** — below Oxford mean 11.9%.

**This means: even if the Wilson CI represents Worcester at its best, its expected acceptance
rate still falls short of the Oxford average.**

**Decomposition**:
- Capacity effect: Worcester has ~65 direct applicants/year for an estimated 4–5 Physics places
  → ~13 direct applicants/place, modestly above the Oxford average rate of 11.9% → does not
  fully explain the 5–6pp shortfall.
- Applicant-pool effect: the most likely driver — Worcester's direct Physics applicants may
  self-select to be weaker-than-average relative to their chosen college. Without conditional
  ESAT/PAT score data by college, this cannot be confirmed.
- Reallocation effect: absorbed into FOI acceptance rate. Even post-reallocation, Worcester
  direct applicants succeed at a below-average rate.
- Residual: 6.7% vs 11.9% Oxford mean (-5.2pp), replicated across 2 confirmed years.

**For Philip**: This AVOID flag likely reflects pool quality, not Worcester-specific disadvantage.
A strong applicant (Philip) would not necessarily face this rate. However, choosing Worcester
means competing against a pool where many applicants are below the Oxford threshold, which does
not help Philip's positioning. The safest interpretation: **avoid Worcester for Physics unless
other factors strongly favour it**.

---

## Colleges with insufficient data (excluded from AVOID determination)

These colleges have 2–3 years of suppressed acceptance data and cannot be reliably assessed:

| College | Apps | Known acc | Suppressed years | Comment |
|---------|------|-----------|-----------------|---------|
| Corpus Christi | 45 | 0† | 3 | All suppressed; likely ≤3/yr accepted |
| Oriel | 41 | 3† | 2 | Too few direct applicants |
| Pembroke | 41 | 3† | 2 | Too few direct applicants |
| St Hilda's | 54 | 3† | 2 | Appears low but CI too wide |
| St Hugh's | 75 | 3† | 2 | Wilson CI upper bound just below mean |
| St Peter's | 68 | 4† | 2 | Appears low but CI too wide |
| Lincoln | 94 | 7† | 1 | 1yr suppressed; borderline |

Note: Wolfson College is not in the FOI data (not listed among Physics-admitting colleges
in the direct-applicant dataset).

---

## Bottom-line recommendation

| Category | Colleges | Reasoning |
|----------|---------|-----------|
| **AVOID** | Worcester | Acceptance rate (6.7% shrunk) significantly below mean; Wilson CI upper bound below mean; consistent across 2yr |
| **Potentially avoid** | University College, Trinity | Both ~8.5–8.7% raw rate; Wilson CI includes mean; not statistically AVOID but consistently below |
| **Treat as equivalent** | All others (ranks 1–17) | All within sampling noise of Oxford mean after shrinkage |
| **Insufficient data** | Corpus Christi, Oriel, Pembroke, St Hilda's, St Peter's, St Hugh's | Cannot assess reliably |

**Working decision rule** (updated):
1. Exclude Worcester.
2. Treat University College and Trinity with mild caution (not statistically AVOID, but consistently
   on the low side).
3. All other colleges (including Keble, Balliol, Hertford, New, Christ Church, Merton, Somerville)
   are statistically indistinguishable — choose by fit.
4. Philip's ESAT score is the dominant variable for any college in the "treat as equivalent" set.

---

## Critical architectural caveat

Oxford Physics shortlisting is **department-led**. The department confirms that a key goal is that
"the probability of admission should not depend on the applicant's choice of college." Reallocation
explicitly corrects for initial oversubscription.

The FOI data confirms this: acceptance rates across most colleges cluster within ~3pp of the
11.9% mean after shrinkage. The residual variation is consistent with applicant-pool quality
differences, not college-specific bias.

**For Philip**: the marginal hour is almost always better spent on ESAT and interview practice
than on optimising college choice. Choose by visit, atmosphere, or gut feeling — not by
one-decimal-place acceptance rate differences.

---

## Key caveats

1. **Metric is acceptance rate, not shortlist rate.** The reallocation effect is absorbed.
   Per-college shortlist rates (pre-reallocation) would show more apparent variation.
2. **Direct applicants only.** Open applicants (~20%) are excluded from both numerator and
   denominator. Colleges that attract many open applicants have smaller direct-applicant samples.
3. **Applicant-pool composition cannot be assessed** without conditional ESAT score data.
   Apparent rate differences are driven primarily by who self-selects to each college.
4. **Suppressed cells** (marked with †) mean k_known is a lower bound. For AVOID flagging,
   a college must meet the criteria even using the lower bound.
5. **Prior strength K=20** is a modelling choice. Changing K=10–30 shifts shrunk rates slightly
   but does not change the AVOID determination for Worcester.
6. **Wolfson College** is not in the FOI data — it may not admit direct Physics applicants
   through the standard process, or numbers may be too small.
