import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from theme import inject_css, render_sidebar, kpi_cards, section_header, section_divider, render_image_frame, page_hero

st.set_page_config(
    page_title="Tesla Safety Analytics · AI Driving Suite",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
render_sidebar()

# ── Page Hero ────────────────────────────────────────────────────────────────
page_hero(
    badge="📊 Safety Intelligence · 294 Cases Analyzed",
    title="Tesla Safety Analytics",
    subtitle=(
        "A deep-dive into 294 Tesla-related fatal incidents spanning 23 countries. "
        "Explore year-wise trends, geographic distribution, model breakdown, and "
        "Autopilot involvement — all distilled into clear, investor-grade visuals."
    )
)

# ── KPI Row ──────────────────────────────────────────────────────────────────
section_header("Dashboard KPIs", "Headline numbers from the safety dataset")

kpi_cards([
    ("Total Cases",  "294", "⚠️", "Fatal incident records"),
    ("Total Deaths", "353", "📋", "Recorded fatalities"),
    ("Countries",    "23",  "🌍", "Global geographic span"),
    ("Top Country",  "USA", "🏆", "Highest incident share"),
])

section_divider()

# ── Year-wise Fatal Incidents ─────────────────────────────────────────────────
section_header("Year-wise Fatal Incidents", "Temporal trend of recorded incidents")

col_chart, col_insight = st.columns([3, 1])

with col_chart:
    render_image_frame("reports/year_trend.png", "Annual Incident Frequency")

with col_insight:
    st.markdown(
        """
        <div style="height:100%; display:flex; flex-direction:column; gap:0.75rem; padding-top:0.5rem;">
          <div class="insight-card" style="border-left-color:#0077B6;">
            <div class="insight-tag" style="color:#0077B6;">📈 Key Trend</div>
            <p class="insight-text">Fatal incidents rose sharply between 2019 and 2022, coinciding with rapid expansion of Tesla's global fleet.</p>
          </div>
          <div class="insight-card" style="border-left-color:#00B4D8;">
            <div class="insight-tag" style="color:#00B4D8;">📅 Peak Period</div>
            <p class="insight-text">The 2019–2022 window represents the most incident-dense period in the dataset.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Country Analysis ──────────────────────────────────────────────────────────
section_header("Country Analysis", "Geographic distribution of incidents")

col_chart2, col_insight2 = st.columns([3, 1])

with col_chart2:
    render_image_frame("reports/country_analysis.png", "Incident Distribution by Country")

with col_insight2:
    st.markdown(
        """
        <div style="height:100%; display:flex; flex-direction:column; gap:0.75rem; padding-top:0.5rem;">
          <div class="insight-card" style="border-left-color:#0077B6;">
            <div class="insight-tag" style="color:#0077B6;">🌎 Geography</div>
            <p class="insight-text">The USA dominates the dataset, accounting for the majority of all recorded Tesla-related fatal incidents.</p>
          </div>
          <div class="insight-card" style="border-left-color:#00B4D8;">
            <div class="insight-tag" style="color:#00B4D8;">🗺️ Coverage</div>
            <p class="insight-text">23 countries are represented, though data density is heavily skewed toward the US market.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Model Analysis ─────────────────────────────────────────────────────────────
section_header("Tesla Model Analysis", "Breakdown by vehicle model")

col_chart3, col_insight3 = st.columns([3, 1])

with col_chart3:
    render_image_frame("reports/model_analysis.png", "Incidents by Tesla Model")

with col_insight3:
    st.markdown(
        """
        <div style="height:100%; display:flex; flex-direction:column; gap:0.75rem; padding-top:0.5rem;">
          <div class="insight-card" style="border-left-color:#0077B6;">
            <div class="insight-tag" style="color:#0077B6;">🚗 Model S</div>
            <p class="insight-text">Among records with identified models, the Model S appears most frequently in the incident log.</p>
          </div>
          <div class="insight-card" style="border-left-color:#00B4D8;">
            <div class="insight-tag" style="color:#00B4D8;">⚠️ Data Quality</div>
            <p class="insight-text">A notable proportion of records have missing model information, underscoring the need for richer data collection.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Autopilot Analysis ─────────────────────────────────────────────────────────
section_header("Autopilot Analysis", "Involvement of autopilot features in incidents")

col_chart4, col_insight4 = st.columns([3, 1])

with col_chart4:
    render_image_frame("reports/autopilot_analysis.png", "Autopilot Involvement Status")

with col_insight4:
    st.markdown(
        """
        <div style="height:100%; display:flex; flex-direction:column; gap:0.75rem; padding-top:0.5rem;">
          <div class="insight-card" style="border-left-color:#0077B6;">
            <div class="insight-tag" style="color:#0077B6;">🤖 Autopilot</div>
            <p class="insight-text">Autopilot involvement data is incomplete for many records, limiting definitive conclusions.</p>
          </div>
          <div class="insight-card" style="border-left-color:#00B4D8;">
            <div class="insight-tag" style="color:#00B4D8;">🔬 Next Steps</div>
            <p class="insight-text">Additional data cleaning and sourcing would significantly improve analytical accuracy on Autopilot involvement.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Key Findings ──────────────────────────────────────────────────────────────
section_header("Key Findings", "Summary of the most important conclusions")

st.markdown(
    """
    <div class="findings-list">
      <div class="finding-item">
        <div class="finding-num">1</div>
        <p class="finding-text">Fatal incidents involving Tesla vehicles increased sharply after 2018, with the most concentrated rise between 2019 and 2022.</p>
      </div>
      <div class="finding-item">
        <div class="finding-num">2</div>
        <p class="finding-text">The United States is the dominant country in the dataset by a significant margin, reflecting Tesla's market concentration there.</p>
      </div>
      <div class="finding-item">
        <div class="finding-num">3</div>
        <p class="finding-text">Among Tesla models with available identification, the Model S appears most frequently in recorded fatal incidents.</p>
      </div>
      <div class="finding-item">
        <div class="finding-num">4</div>
        <p class="finding-text">Significant data quality issues were identified and documented regarding Autopilot involvement, requiring further investigation for robust analysis.</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
