# Oxford Physics — College Selector

A Streamlit app that applies rigorous statistical analysis to FOI-disclosed data on Oxford Physics
undergraduate admissions, helping applicants choose which college to apply to.

## What it does

- Loads per-college Physics acceptance rates from a July 2025 FOI disclosure to the University of Oxford
- Applies Wilson score confidence intervals and Bayesian shrinkage (prior = Oxford mean, K=20)
- Flags colleges where direct applicants have acceptance rates statistically below the Oxford average
- Shows per-year breakdowns for any selected college

## Key finding

The reallocation system works as Oxford claims. After accounting for reallocation (the FOI metric
attributes acceptances back to the originally-chosen college), most colleges cluster within sampling
noise of the 11.9% Oxford-wide acceptance rate. Only **Worcester College** is robustly flagged AVOID.

Keble — often cited anecdotally as oversubscribed — has a 12.1% acceptance rate, essentially
identical to the Oxford mean. Its pre-reallocation shortlist disadvantage is corrected by Oxford's
reallocation process.

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data

`data/foi_physics_college_2025.xlsx` — FOI response (University of Oxford, July 2025) via
[WhatDoTheyKnow](https://www.whatdotheyknow.com/request/physics_admissions_data_by_colle).
Contains direct-applicant Physics application and acceptance counts for all 29 colleges,
UCAS cycles 2019–2024.

## Methodology

- **Metric**: acceptance rate for direct applicants, attributed to the initially-applied college
  (reallocation effect absorbed)
- **Wilson CI**: 95% confidence intervals; suppressed cells treated as lower bounds
- **Bayesian shrinkage**: Beta(2.37, 17.63) prior ≡ 20 pseudo-observations at the Oxford mean
- **AVOID criteria**: shrunk rate > 2pp below Oxford mean, Wilson CI upper bound below mean,
  ≥30 applicants, ≤1 suppressed year

## Context

This is part of a broader analysis supporting an Oxford Physics application (F303). The analysis
follows the principle that ESAT score is the dominant variable — college choice has a small
marginal effect for any college outside the AVOID set.
