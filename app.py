import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import beta as beta_dist

st.set_page_config(
    page_title="Oxford Physics College Selector",
    page_icon="⚛️",
    layout="wide",
)

# ── Data loading & processing ──────────────────────────────────────────────────

@st.cache_data
def load_and_process():
    df = pd.read_excel("data/foi_physics_college_2025.xlsx", sheet_name="Data", header=0)
    df.columns = ["cycle", "course", "college", "applications", "acceptances"]

    df3 = df[df["cycle"].isin([2019, 2020, 2021, 2022, 2023, 2024])].copy()
    df3["acceptances"] = df3["acceptances"].replace("*", np.nan)
    df3["applications"] = pd.to_numeric(df3["applications"], errors="coerce")
    df3["acceptances"] = pd.to_numeric(df3["acceptances"], errors="coerce")

    # Per-year pivot for detail view
    per_year = df3.pivot_table(
        index="college", columns="cycle", values=["applications", "acceptances"], aggfunc="sum"
    )
    per_year.columns = [f"{m}_{y}" for m, y in per_year.columns]
    per_year = per_year.reset_index()

    # 6-year aggregates
    agg = df3.groupby("college").agg(
        n=("applications", "sum"),
        k=("acceptances", "sum"),
        n_suppressed=("acceptances", lambda x: x.isna().sum()),
    ).reset_index()

    oxford_n = df3["applications"].sum()
    oxford_k = df3["acceptances"].sum()
    oxford_mean = float(oxford_k / oxford_n)

    K = 20
    alpha_0 = oxford_mean * K
    beta_0 = (1 - oxford_mean) * K

    def wilson_ci(k, n, z=1.96):
        if n == 0 or np.isnan(n) or np.isnan(k):
            return np.nan, np.nan
        if k == 0:
            return 0.0, float(z**2 / (n + z**2))
        p = k / n
        denom = 1 + z**2 / n
        c = (p + z**2 / (2 * n)) / denom
        m = (z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))) / denom
        return float(max(0, c - m)), float(c + m)

    def bayes_ci(k, n):
        if np.isnan(k) or np.isnan(n):
            return np.nan, np.nan
        a, b = k + alpha_0, n - k + beta_0
        return float(beta_dist.ppf(0.025, a, b)), float(beta_dist.ppf(0.975, a, b))

    agg["raw_rate"] = agg["k"] / agg["n"]
    agg["shrunk_rate"] = (agg["k"] + alpha_0) / (agg["n"] + K)
    agg[["w_lo", "w_hi"]] = agg.apply(
        lambda r: wilson_ci(r["k"], r["n"]), axis=1, result_type="expand"
    )
    agg[["b_lo", "b_hi"]] = agg.apply(
        lambda r: bayes_ci(r["k"], r["n"]), axis=1, result_type="expand"
    )
    agg["rank"] = agg["shrunk_rate"].rank(ascending=False, method="min").astype(int)

    # PREFER/AVOID: symmetric shrunk-only rule (equal-quality assumption)
    # PREFER: shrunk > mean+2pp
    agg["PREFER"] = agg["shrunk_rate"] > (oxford_mean + 0.02)
    # AVOID: shrunk < mean-2pp
    agg["AVOID"] = agg["shrunk_rate"] < (oxford_mean - 0.02)
    agg["data_quality"] = agg["n_suppressed"].apply(
        lambda x: "complete" if x == 0 else ("all suppressed" if x == 6 else f"{int(x)} yr suppressed")
    )

    agg = agg.merge(per_year, on="college", how="left")
    agg = agg.sort_values("rank").reset_index(drop=True)

    return agg, oxford_mean, oxford_n, oxford_k, df3

agg, oxford_mean, oxford_n, oxford_k, df3_raw = load_and_process()

# ── Header ─────────────────────────────────────────────────────────────────────

st.title("Oxford Physics — College Selector")
st.caption(
    "Statistical analysis of per-college Physics acceptance rates using FOI data "
    "(WhatDoTheyKnow, July 2025). Covers UCAS cycles 2019–2024, direct applicants only."
)

# ── Key metrics ────────────────────────────────────────────────────────────────

c1, c2, c3, c4 = st.columns(4)
c1.metric("Oxford-wide acceptance rate", f"{oxford_mean:.1%}",
          help="Direct-applicant acceptance rate, all colleges, 2019–2024")
c2.metric("Direct applicants (6yr)", f"{int(oxford_n):,}")
c3.metric("Acceptances (6yr)", f"{int(oxford_k):,}")
c4.metric("Colleges flagged AVOID", str(int(agg["AVOID"].sum())),
          help="Shrunk rate > 2pp below Oxford mean (equal-quality-pool assumption)")

c5, c6 = st.columns(2)
c5.metric("Colleges flagged PREFER", str(int(agg["PREFER"].sum())),
          help="Shrunk rate > 2pp above Oxford mean (equal-quality-pool assumption)")
c6.metric("Oxford mean (shrunk baseline)", f"{oxford_mean:.1%}")

st.divider()

# ── Formatting helpers (used by both chart and table) ──────────────────────────

def _fmt_acc(row):
    if row["n_suppressed"] == 6:
        return "— (all suppressed)"
    if row["n_suppressed"] > 0:
        return f"≥ {int(row['k'])}"
    return str(int(row["k"]))

def _fmt_raw(row):
    if row["n_suppressed"] == 6:
        return "—"
    if row["n_suppressed"] > 0:
        return f"≥ {row['k'] / row['n']:.1%}"
    return f"{row['k'] / row['n']:.1%}"

# ── Ranked bar chart ───────────────────────────────────────────────────────────

st.subheader("Acceptance rate by college (direct applicants, 2019–2024)")
st.caption(
    "Bars show Bayesian-shrunk acceptance rate (prior = Oxford mean, K=20). "
    "Error bars = 95% Wilson CI. Red dashed line = Oxford mean. "
    "Green = PREFER (shrunk > mean+2pp). Red = AVOID (shrunk < mean−2pp). Blue = neutral. Both use equal-quality assumption."
)

def _bar_color(row):
    if row["AVOID"]:
        return "#d32f2f"
    if row["PREFER"]:
        return "#388e3c"
    return "#1976d2"

colors = agg.apply(_bar_color, axis=1).tolist()

fig = go.Figure()

fig.add_trace(go.Bar(
    x=agg["college"],
    y=agg["shrunk_rate"],
    error_y=dict(
        type="data",
        symmetric=False,
        array=agg["w_hi"] - agg["shrunk_rate"],
        arrayminus=agg["shrunk_rate"] - agg["w_lo"],
        color="rgba(0,0,0,0.35)",
        thickness=1.5,
        width=4,
    ),
    marker_color=colors,
    customdata=np.stack([
        agg["n"],
        agg.apply(_fmt_acc, axis=1),
        agg.apply(_fmt_raw, axis=1),
        agg["data_quality"],
        agg["AVOID"].astype(str),
        agg["rank"],
        agg["PREFER"].astype(str),
    ], axis=-1),
    hovertemplate=(
        "<b>%{x}</b><br>"
        "Rank: #%{customdata[5]}<br>"
        "Shrunk rate: %{y:.1%}<br>"
        "Raw rate: %{customdata[2]}<br>"
        "Applications: %{customdata[0]}<br>"
        "Acceptances: %{customdata[1]}<br>"
        "Data: %{customdata[3]}<br>"
        "PREFER: %{customdata[6]}<br>"
        "AVOID: %{customdata[4]}<extra></extra>"
    ),
))

fig.add_hline(
    y=oxford_mean,
    line_dash="dash",
    line_color="red",
    line_width=1.5,
    annotation_text=f"Oxford mean {oxford_mean:.1%}",
    annotation_position="top right",
    annotation_font_color="red",
)

fig.update_layout(
    xaxis_tickangle=-45,
    yaxis_tickformat=".0%",
    yaxis_title="Shrunk acceptance rate",
    plot_bgcolor="white",
    height=460,
    margin=dict(t=20, b=10),
    showlegend=False,
)
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=True, gridcolor="rgba(0,0,0,0.08)")

st.plotly_chart(fig, use_container_width=True)

# ── Full data table ────────────────────────────────────────────────────────────

st.subheader("Full ranked table")

display = agg[[
    "rank", "college", "n", "k", "raw_rate", "shrunk_rate",
    "w_lo", "w_hi", "PREFER", "AVOID", "data_quality"
]].copy()
display.columns = [
    "Rank", "College", "Apps (6yr)", "Known acc", "Raw rate",
    "Shrunk rate", "Wilson lo", "Wilson hi", "PREFER", "AVOID", "Data quality"
]

def style_table(row):
    if row["AVOID"]:
        return ["background-color: #ffebee"] * len(row)
    if row["PREFER"]:
        return ["background-color: #e8f5e9"] * len(row)
    return [""] * len(row)

display["Known acc"] = agg.apply(_fmt_acc, axis=1)
display["Raw rate"] = agg.apply(_fmt_raw, axis=1)

pct_cols = ["Shrunk rate", "Wilson lo", "Wilson hi"]
styled = (
    display.style
    .apply(style_table, axis=1)
    .format({c: "{:.1%}" for c in pct_cols})
    .format({"Apps (6yr)": lambda x: f"{x:.0f}"})
    .format({"Raw rate": lambda x: x})
    .format({"Known acc": lambda x: x})
)

st.dataframe(styled, use_container_width=True, hide_index=True)

st.caption(
    "† Known acc is a lower bound when cells are suppressed (Oxford suppresses counts ≤ 5). "
    "Raw rate = k_known / n. Shrunk rate = Bayesian posterior mean with Beta(2.37, 17.63) prior. "
    "Wilson CI uses k_known as lower bound for suppressed colleges."
)

# ── College detail ─────────────────────────────────────────────────────────────

st.divider()
st.subheader("Per-college detail")

selected = st.selectbox(
    "Select a college",
    options=agg["college"].tolist(),
    index=int(agg[agg["college"] == "Keble College"].index[0]),
)

row = agg[agg["college"] == selected].iloc[0]
yr_data = df3_raw[df3_raw["college"] == selected].sort_values("cycle")

col_l, col_r = st.columns([1, 2])

with col_l:
    if row["AVOID"]:
        flag = "🔴 **AVOID** — shrunk rate > 2pp below Oxford mean"
    elif row["PREFER"]:
        flag = "🟢 **PREFER** — shrunk rate above Oxford mean (equal-quality assumption)"
    else:
        flag = "🔵 **Neutral** — within statistical noise of Oxford mean"
    st.markdown(f"### {selected}")
    st.markdown(flag)
    st.metric("Rank", f"#{int(row['rank'])} of 29")
    st.metric("6yr direct applicants", f"{int(row['n'])}")
    fully_suppressed = row["n_suppressed"] == 6
    partial_suppressed = 0 < row["n_suppressed"] < 6
    if fully_suppressed:
        st.metric("Known acceptances (6yr)", "— (all suppressed)",
                  help="All 6 years suppressed by Oxford (count ≤5 each year).")
        st.metric("Raw acceptance rate", "—",
                  help="Cannot compute: no confirmed acceptance counts.")
    elif partial_suppressed:
        st.metric("Known acceptances (6yr)", f"≥ {int(row['k'])}",
                  help=f"{int(row['n_suppressed'])} year(s) suppressed. Shown value is a lower bound.")
        st.metric("Raw acceptance rate", f"≥ {row['raw_rate']:.1%}",
                  help="Lower bound — suppressed years counted as 0.")
    else:
        st.metric("Known acceptances (6yr)", f"{int(row['k'])}")
        st.metric("Raw acceptance rate", f"{row['raw_rate']:.1%}")
    st.metric("Shrunk acceptance rate", f"{row['shrunk_rate']:.1%}",
              delta=f"{row['shrunk_rate'] - oxford_mean:+.1%} vs Oxford mean",
              delta_color="normal" if not row["AVOID"] else "inverse")
    st.metric("Wilson 95% CI", f"[{row['w_lo']:.1%}, {row['w_hi']:.1%}]")
    st.caption(f"Data quality: {row['data_quality']}")

with col_r:
    fig2 = go.Figure()

    for _, yr_row in yr_data.iterrows():
        yr = int(yr_row["cycle"])
        apps = yr_row["applications"]
        acc = yr_row["acceptances"]
        suppressed = pd.isna(acc)
        label = "suppressed" if suppressed else f"{int(acc)}/{int(apps)} = {acc/apps:.0%}"
        fig2.add_annotation(
            x=yr, y=0, text=label,
            showarrow=False, yshift=15, font=dict(size=11)
        )

    yr_data_plot = yr_data[yr_data["acceptances"].notna()].copy()
    yr_data_plot["rate"] = yr_data_plot["acceptances"] / yr_data_plot["applications"]

    if len(yr_data_plot) > 0:
        fig2.add_trace(go.Scatter(
            x=yr_data_plot["cycle"],
            y=yr_data_plot["rate"],
            mode="markers+lines",
            marker=dict(size=10, color="#1976d2"),
            line=dict(color="#1976d2", dash="dot"),
            name=selected,
        ))

    fig2.add_hline(
        y=oxford_mean, line_dash="dash", line_color="red", line_width=1.5,
        annotation_text=f"Oxford mean {oxford_mean:.1%}",
        annotation_position="top right",
        annotation_font_color="red",
    )

    fig2.update_layout(
        xaxis=dict(tickvals=[2019, 2020, 2021, 2022, 2023, 2024], title="UCAS cycle"),
        yaxis=dict(tickformat=".0%", title="Acceptance rate"),
        plot_bgcolor="white",
        height=300,
        margin=dict(t=20, b=10),
        showlegend=False,
    )
    fig2.update_yaxes(showgrid=True, gridcolor="rgba(0,0,0,0.08)")
    st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(
        yr_data[["cycle", "applications", "acceptances"]].rename(
            columns={"cycle": "UCAS cycle", "applications": "Direct apps",
                     "acceptances": "Accepted"}
        ).set_index("UCAS cycle"),
        use_container_width=True,
    )

# ── Data sources ───────────────────────────────────────────────────────────────

st.divider()
st.subheader("Data sources")
st.markdown("""
| # | Source | Link | What it contains |
|---|--------|------|-----------------|
| 1 | **FOI disclosure — University of Oxford, July 2025** | [WhatDoTheyKnow request](https://www.whatdotheyknow.com/request/physics_admissions_data_by_colle) | Per-college Physics direct-applicant application and acceptance counts, UCAS cycles 2019–2024. Acceptances attributed to the originally-applied college (reallocation absorbed). All 29 colleges. |
| 2 | **Analysis code & raw data file** | [github.com/dmitry-goryunov/oxford_physics](https://github.com/dmitry-goryunov/oxford_physics) | Full source code for this app and the downloaded FOI spreadsheet (`data/foi_physics_college_2025.xlsx`). |

The FOI response was submitted to Oxford via WhatDoTheyKnow and disclosed July 2025.
All UCAS cycles **2019–2024** are used for the analysis (6-year aggregate).
Oxford suppresses cell counts of 5 or fewer — those cells appear as asterisks in the raw data and are treated as lower bounds here.
""")

# ── Methodology ────────────────────────────────────────────────────────────────

st.divider()
with st.expander("Methodology and caveats"):
    st.markdown("""
**Data source**: [WhatDoTheyKnow FOI response](https://www.whatdotheyknow.com/request/physics_admissions_data_by_colle) to the University of Oxford, July 2025.
Physics undergraduate admissions, UCAS cycles 2019–2024. All 6 cycles used here.

**Metric**: *Acceptance rate for direct applicants, attributed to the initially-applied college.*
If a student applies to college X, gets reallocated to college Y at shortlisting, and is eventually
accepted — that acceptance is attributed back to college X. This means **reallocation is already
absorbed** in the numbers. This is the most useful metric for deciding which college to apply to.

**Why this beats shortlist rates**: Shortlist rates (e.g., from Keble's own feedback PDFs)
capture only the pre-reallocation stage. Keble shortlists fewer of its applicants (it's
oversubscribed), but those applicants get reallocated and accepted elsewhere. The FOI metric
captures the full pipeline.

**Statistical adjustments**:
- *Wilson score confidence intervals* at 95% level, using k_known as a lower bound
  for colleges with suppressed (≤5) cells.
- *Bayesian shrinkage*: Beta prior equivalent to 20 pseudo-observations at the Oxford mean
  (11.9%). Pulls small-sample colleges toward the overall mean.
- *AVOID flag criteria (equal-quality assumption)*: shrunk rate > 2pp below Oxford mean.
  Symmetric with PREFER. Assumes applicant pools are identical; in practice AVOID colleges
  may attract weaker self-selected pools, so the penalty may be partly applicant-pool effect.
- *PREFER flag criteria (equal-quality assumption)*: shrunk rate > 2pp above Oxford mean.
  In practice, PREFER colleges may attract stronger self-selected pools — the observed advantage
  is likely partly applicant-pool effect, not a college-specific acceptance premium.

**Limitations**:
1. Direct applicants only. Open applicants (~20% of total) are excluded from both numerator and
   denominator.
2. Suppressed cells (Oxford suppresses counts ≤5) introduce uncertainty for thin-data colleges.
3. Applicant-pool quality is not observable. A low acceptance rate at a college could reflect
   weaker self-selection, not a college-specific penalty. Philip as a strong candidate would
   likely face a higher conditional rate than the pool average.
4. Wolfson College is absent from the FOI data.

**Key revision from previous analysis**: The earlier analysis flagged Keble as AVOID based on
shortlist rates. FOI acceptance-rate data shows Keble direct applicants succeed at 12.1% ≈
Oxford mean 11.9%. Keble's pre-reallocation shortlist disadvantage is fully corrected by Oxford's
reallocation system. **Keble is not AVOID.**

**Bottom line**: College choice has a small effect on admissions outcomes. Only Worcester is
robustly below average. ESAT score is the dominant variable.
    """)

st.caption(
    "Analysis by Philip's application project · Data: FOI 2025 (Oxford) · "
    "Code: [github.com/dmitry-goryunov/oxford_physics](https://github.com/dmitry-goryunov/oxford_physics)"
)
