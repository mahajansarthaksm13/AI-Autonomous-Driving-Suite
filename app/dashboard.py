import streamlit as st
import sys
import os

# ── Path setup ──────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(__file__))
from theme import inject_css, render_sidebar, kpi_cards, section_header, section_divider, page_hero

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Autonomous Driving Suite",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

# ── Sidebar nav ─────────────────────────────────────────────────────────────
render_sidebar()

# ── Hero Section ─────────────────────────────────────────────────────────────
page_hero(
    badge="🚗 CAPSTONE PROJECT 1",
    title="AI Autonomous Driving Suite",
    subtitle=(
        "A unified intelligence platform combining YOLOv8 vehicle detection with "
        "Tesla safety analytics — built to turn raw road data into clear, "
        "actionable insights for the future of autonomous mobility."
    )
)

# ── KPI Row ──────────────────────────────────────────────────────────────────
section_header("Platform Overview", "Core numbers at a glance")

kpi_cards([
    ("Total Cases",    "294",  "⚠️", "Tesla fatal incidents"),
    ("Total Deaths",   "353",  "📋", "Recorded fatalities"),
    ("Countries",      "23",   "🌍", "Global coverage"),
    ("Vehicle Classes","11",   "🚘", "YOLOv8 detection classes"),
])

section_divider()

# ── Key Insights ─────────────────────────────────────────────────────────────
section_header("Key Insights", "What the data reveals")

st.markdown(
    """
    <div class="insight-grid">
      <div class="insight-card">
        <div class="insight-tag">📈 Trend</div>
        <p class="insight-text">Fatal incidents increased significantly after 2018, peaking between 2019–2022 as Tesla's fleet expanded globally.</p>
      </div>
      <div class="insight-card">
        <div class="insight-tag">🌎 Geography</div>
        <p class="insight-text">The USA accounts for the majority of recorded incidents, reflecting the highest Tesla adoption rate worldwide.</p>
      </div>
      <div class="insight-card">
        <div class="insight-tag">🚗 Model</div>
        <p class="insight-text">Model S appears most frequently among identified Tesla models in the fatal incident dataset.</p>
      </div>
      <div class="insight-card">
        <div class="insight-tag">🤖 Detection</div>
        <p class="insight-text">YOLOv8 achieved <strong>69.2% mAP50</strong> and <strong>72.6% Precision</strong> on 11 vehicle classes after 50 training epochs.</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

section_divider()

# ── System Architecture Pipeline ─────────────────────────────────────────────
section_header("System Architecture", "End-to-end processing pipeline")

st.markdown(
    """<div class="pipeline-wrap">
<div class="pipeline-flow">
<div class="pipeline-node"><div class="pipeline-icon">📦</div><div class="pipeline-label">Dataset Ingestion</div></div>
<div class="pipeline-arrow"><span>→</span></div>
<div class="pipeline-node"><div class="pipeline-icon">🧹</div><div class="pipeline-label">Data Cleaning</div></div>
<div class="pipeline-arrow"><span>→</span></div>
<div class="pipeline-node"><div class="pipeline-icon">🏋️</div><div class="pipeline-label">YOLOv8 Training</div></div>
<div class="pipeline-arrow"><span>→</span></div>
<div class="pipeline-node"><div class="pipeline-icon">🔍</div><div class="pipeline-label">Vehicle Detection</div></div>
<div class="pipeline-arrow"><span>→</span></div>
<div class="pipeline-node"><div class="pipeline-icon">📊</div><div class="pipeline-label">Tesla Analytics</div></div>
<div class="pipeline-arrow"><span>→</span></div>
<div class="pipeline-node"><div class="pipeline-icon">🖥️</div><div class="pipeline-label">Dashboard</div></div>
</div>
</div>""",
    unsafe_allow_html=True,
)

section_divider()

# ── Tech Stack ───────────────────────────────────────────────────────────────
section_header("Technology Stack", "Tools powering every layer")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="tech-card">
          <div class="tech-card-icon">🤖</div>
          <div class="tech-card-title">AI &amp; Machine Learning</div>
          <div class="tech-item"><span class="tech-dot"></span>YOLOv8 (Ultralytics)</div>
          <div class="tech-item"><span class="tech-dot"></span>Computer Vision</div>
          <div class="tech-item"><span class="tech-dot"></span>Object Detection</div>
          <div class="tech-item"><span class="tech-dot"></span>Tesla T4 GPU Training</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="tech-card">
          <div class="tech-card-icon">📊</div>
          <div class="tech-card-title">Data Analytics</div>
          <div class="tech-item"><span class="tech-dot"></span>Pandas</div>
          <div class="tech-item"><span class="tech-dot"></span>NumPy</div>
          <div class="tech-item"><span class="tech-dot"></span>Matplotlib</div>
          <div class="tech-item"><span class="tech-dot"></span>Statistical Analysis</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="tech-card">
          <div class="tech-card-icon">🚀</div>
          <div class="tech-card-title">Deployment</div>
          <div class="tech-item"><span class="tech-dot"></span>Streamlit</div>
          <div class="tech-item"><span class="tech-dot"></span>Python 3.x</div>
          <div class="tech-item"><span class="tech-dot"></span>GitHub</div>
          <div class="tech-item"><span class="tech-dot"></span>Google Colab</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Dataset Summary ───────────────────────────────────────────────────────────
section_header("Dataset Summary", "Data foundations of the platform")

d1, d2 = st.columns(2)

with d1:
    st.markdown(
        """
        <div class="stat-panel">
          <div class="stat-panel-title">🚘 Vehicle Detection Dataset</div>
          <div class="stat-row">
            <span class="stat-row-key">Total Images</span>
            <span class="stat-row-val">5,626</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Total Annotations</span>
            <span class="stat-row-val">351,549</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Vehicle Classes</span>
            <span class="stat-row-val">11</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Model Architecture</span>
            <span class="stat-row-val">YOLOv8s</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with d2:
    st.markdown(
        """
        <div class="stat-panel">
          <div class="stat-panel-title">⚠️ Tesla Safety Dataset</div>
          <div class="stat-row">
            <span class="stat-row-key">Fatal Cases</span>
            <span class="stat-row-val">294</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Recorded Deaths</span>
            <span class="stat-row-val">353</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Countries Covered</span>
            <span class="stat-row-val">23</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Top Country</span>
            <span class="stat-row-val">USA</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Project Goal Banner ───────────────────────────────────────────────────────
st.markdown(
    """
    <div class="goal-banner">
      <h4>Project Objective</h4>
      <p>
        Build an AI-powered Autonomous Driving Analytics Platform capable of detecting
        vehicles from traffic images using state-of-the-art computer vision, analyzing
        Tesla fatal incident data across 23 countries, visualizing safety trends over
        time, and delivering actionable insights through a unified, interactive dashboard.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)
