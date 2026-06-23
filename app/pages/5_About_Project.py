import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from theme import inject_css, render_sidebar, section_header, section_divider, page_hero

st.set_page_config(
    page_title="About Project · AI Driving Suite",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
render_sidebar()

# ── Page Hero ────────────────────────────────────────────────────────────────
page_hero(
    badge="ℹ️ Portfolio Project · IIT Guwahati",
    title="About the Project",
    subtitle=(
        "AI Autonomous Driving Suite is a portfolio-grade artificial intelligence "
        "project that brings together computer vision, object detection, and "
        "real-world safety data analytics into a single, unified platform."
    )
)

# ── Problem Statement ─────────────────────────────────────────────────────────
section_header("Problem Statement", "What challenge does this project address?")

st.markdown(
    """
    <div style="
      background: var(--white);
      border-radius: 16px;
      padding: 1.75rem 2rem;
      box-shadow: 0 4px 20px rgba(3,4,94,.08);
      border: 1px solid #e8f4fb;
      margin-bottom: 1.5rem;
    ">
      <p style="font-size:0.9rem;color:#334e68;line-height:1.8;margin:0 0 1rem 0;">
        Modern transportation systems generate enormous volumes of visual and safety-related data,
        yet the tools to extract actionable intelligence from that data remain scattered and inaccessible.
        This project aims to bridge that gap by building an end-to-end AI platform that addresses four objectives:
      </p>
      <div class="findings-list">
        <div class="finding-item">
          <div class="finding-num">1</div>
          <p class="finding-text">Detect and classify vehicles from road images using a trained YOLOv8 deep learning model.</p>
        </div>
        <div class="finding-item">
          <div class="finding-num">2</div>
          <p class="finding-text">Analyze Tesla fatal incident data spanning 294 cases across 23 countries.</p>
        </div>
        <div class="finding-item">
          <div class="finding-num">3</div>
          <p class="finding-text">Identify temporal safety trends, geographic patterns, and model-specific risks.</p>
        </div>
        <div class="finding-item">
          <div class="finding-num">4</div>
          <p class="finding-text">Visualize all insights through an interactive, investor-grade analytics dashboard.</p>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

section_divider()

# ── Project Modules ───────────────────────────────────────────────────────────
section_header("Project Modules", "Four integrated components of the platform")

mc1, mc2, mc3, mc4 = st.columns(4)

modules = [
    (mc1, "🚘", "Vehicle Detection",
     "YOLOv8 model trained on 5,626 images to detect 11 vehicle classes from real-world road scenes."),
    (mc2, "📊", "Tesla Analytics",
     "Exploratory analysis of 294 fatal cases, revealing year-wise trends, country distribution, and model breakdown."),
    (mc3, "📈", "Model Performance",
     "Comprehensive evaluation: Precision 72.6%, Recall 64.0%, mAP50 69.2%, mAP50-95 51.4%."),
    (mc4, "🖥️", "Streamlit Dashboard",
     "Multi-page interactive dashboard with premium design, custom navigation, and real-time inference capability."),
]

for col, icon, title, desc in modules:
    with col:
        st.markdown(
            f"""
            <div class="module-card">
              <div class="module-icon">{icon}</div>
              <div class="module-title">{title}</div>
              <p class="module-desc">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

section_divider()

# ── Technologies ──────────────────────────────────────────────────────────────
section_header("Technologies Used", "The full stack behind the platform")

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown(
        """
        <div class="tech-card">
          <div class="tech-card-icon">💻</div>
          <div class="tech-card-title">Programming</div>
          <div class="tech-item"><span class="tech-dot"></span>Python 3.x</div>
          <div class="tech-item"><span class="tech-dot"></span>NumPy</div>
          <div class="tech-item"><span class="tech-dot"></span>Pandas</div>
          <div class="tech-item"><span class="tech-dot"></span>Pillow (PIL)</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with t2:
    st.markdown(
        """
        <div class="tech-card">
          <div class="tech-card-icon">🤖</div>
          <div class="tech-card-title">Machine Learning</div>
          <div class="tech-item"><span class="tech-dot"></span>YOLOv8 (Ultralytics)</div>
          <div class="tech-item"><span class="tech-dot"></span>Computer Vision</div>
          <div class="tech-item"><span class="tech-dot"></span>Object Detection</div>
          <div class="tech-item"><span class="tech-dot"></span>Google Colab / T4 GPU</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with t3:
    st.markdown(
        """
        <div class="tech-card">
          <div class="tech-card-icon">📊</div>
          <div class="tech-card-title">Visualization</div>
          <div class="tech-item"><span class="tech-dot"></span>Streamlit</div>
          <div class="tech-item"><span class="tech-dot"></span>Matplotlib</div>
          <div class="tech-item"><span class="tech-dot"></span>Custom CSS / HTML</div>
          <div class="tech-item"><span class="tech-dot"></span>GitHub</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Project Workflow Timeline ─────────────────────────────────────────────────
section_header("Project Workflow", "Step-by-step development timeline")

timeline_steps = [
    ("Phase 1", "Dataset Acquisition",
     "Sourced the vehicle detection dataset with 5,626 images and 351,549 bounding box annotations across 11 vehicle classes."),
    ("Phase 2", "Data Processing",
     "Cleaned, validated, and converted annotations to YOLO format. Structured train / val / test splits."),
    ("Phase 3", "YOLOv8 Training",
     "Trained YOLOv8s for 50 epochs on Tesla T4 GPU using the Ultralytics framework in Google Colab."),
    ("Phase 4", "Model Evaluation",
     "Evaluated on held-out test set: Precision 72.6%, Recall 64.0%, mAP50 69.2%, mAP50-95 51.4%."),
    ("Phase 5", "Vehicle Detection Deployment",
     "Integrated the trained model into a real-time inference pipeline with Streamlit file uploader."),
    ("Phase 6", "Tesla Safety Analytics",
     "Analyzed 294 fatal incident records across 23 countries, producing charts on year-wise trends, countries, models, and Autopilot involvement."),
    ("Phase 7", "Interactive Dashboard",
     "Built this multi-page Streamlit dashboard with premium UI, custom navigation, and responsive layout."),
]

tl_html = '<div class="timeline">'
for step_label, step_title, step_desc in timeline_steps:
    tl_html += f"""<div class="timeline-item">
  <div class="timeline-dot"></div>
  <div class="timeline-step">{step_label}</div>
  <div class="timeline-title">{step_title}</div>
  <p class="timeline-desc">{step_desc}</p>
</div>"""
tl_html += "</div>"
st.markdown(tl_html, unsafe_allow_html=True)

section_divider()

# ── Key Results ───────────────────────────────────────────────────────────────
section_header("Key Results", "Headline metrics from the completed project")

r1, r2, r3, r4 = st.columns(4)
results = [
    (r1, "69.2%", "mAP50"),
    (r2, "72.6%", "Precision"),
    (r3, "64.0%", "Recall"),
    (r4, "11",    "Vehicle Classes"),
]
for col, val, label in results:
    with col:
        st.markdown(
            f"""
            <div class="result-tile">
              <div class="result-value">{val}</div>
              <div class="result-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

section_divider()

# ── Future Enhancements Roadmap ───────────────────────────────────────────────
section_header("Future Enhancements", "What comes next for the platform")

roadmap_items = [
    ("🎥", "Video Stream Detection",
     "Extend inference pipeline to support real-time video streams and webcam input for continuous monitoring."),
    ("📡", "Real-Time Monitoring",
     "Deploy the model as a live API service with websocket-based streaming and edge device support."),
    ("📊", "Advanced Tesla Analytics",
     "Incorporate richer datasets, geospatial mapping, and causal analysis of Autopilot involvement."),
    ("🎛️", "Interactive Filtering",
     "Add dynamic filter controls — date ranges, countries, models — for fully exploratory data analysis."),
    ("☁️", "Cloud Deployment",
     "Host the complete platform on cloud infrastructure (AWS / GCP) with authentication and multi-user support."),
    ("🚗", "AV Simulation Integration",
     "Integrate with CARLA or SUMO autonomous vehicle simulators to validate detection in synthetic environments."),
]

r1c, r2c = st.columns(2)
for i, (icon, title, desc) in enumerate(roadmap_items):
    col = r1c if i % 2 == 0 else r2c
    with col:
        st.markdown(
            f"""
            <div class="roadmap-card" style="margin-bottom:0.75rem;">
              <div class="roadmap-badge">{icon} Planned</div>
              <div class="roadmap-title">{title}</div>
              <p class="roadmap-desc">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

section_divider()

# ── Closing Banner ────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="closing-banner">
      <p>
        AI Autonomous Driving Suite demonstrates the complete lifecycle of an AI product —
        from data ingestion and model training, through evaluation and safety analytics,
        to a polished interactive dashboard. Built as a portfolio-grade project to reflect
        the standard of work expected in AI research and product teams.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)
