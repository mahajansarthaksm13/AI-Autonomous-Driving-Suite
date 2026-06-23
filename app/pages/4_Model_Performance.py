import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from theme import inject_css, render_sidebar, section_header, section_divider, page_hero

st.set_page_config(
    page_title="Model Performance · AI Driving Suite",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
render_sidebar()

# ── Page Hero ────────────────────────────────────────────────────────────────
page_hero(
    badge="📈 YOLOv8s · 50 Epochs · Tesla T4 GPU",
    title="Model Performance",
    subtitle=(
        "Detailed evaluation of the trained YOLOv8 vehicle detection model — "
        "precision, recall, mAP scores, training setup, class distribution, "
        "and a full record of project milestones achieved."
    )
)

# ── Metric Cards ──────────────────────────────────────────────────────────────
section_header("Evaluation Metrics", "Model performance on the held-out test set")

# SVG defs for ring gradient
st.markdown(
    """
    <svg class="svg-defs" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:#00B4D8"/>
          <stop offset="100%" style="stop-color:#0077B6"/>
        </linearGradient>
      </defs>
    </svg>
    """,
    unsafe_allow_html=True,
)

metrics = [
    ("Precision",  72.6, "72.6%",  "Of all positive detections,<br>72.6% were correct."),
    ("Recall",     64.0, "64.0%",  "64% of actual vehicles<br>were successfully detected."),
    ("mAP50",      69.2, "69.2%",  "Mean Average Precision<br>at IoU threshold 0.50."),
    ("mAP50-95",   51.4, "51.4%",  "Mean AP across IoU<br>thresholds 0.50–0.95."),
]

cols = st.columns(4)
for col, (label, pct, display, desc) in zip(cols, metrics):
    circumference = 2 * 3.14159 * 34  # radius=34
    dash_val = (pct / 100) * circumference
    gap_val  = circumference - dash_val
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-ring-wrap">
                <svg viewBox="0 0 80 80" width="80" height="80">
                  <defs>
                    <linearGradient id="rg_{label}" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" style="stop-color:#00B4D8"/>
                      <stop offset="100%" style="stop-color:#0077B6"/>
                    </linearGradient>
                  </defs>
                  <circle class="metric-ring-bg" cx="40" cy="40" r="34"/>
                  <circle class="metric-ring-fg"
                    cx="40" cy="40" r="34"
                    stroke="url(#rg_{label})"
                    stroke-dasharray="{dash_val:.1f} {gap_val:.1f}"
                    transform="rotate(-90 40 40)"
                    fill="none"
                    stroke-width="6"
                    stroke-linecap="round"
                  />
                </svg>
                <div class="metric-ring-text">{int(pct)}%</div>
              </div>
              <div class="metric-value-large">{display}</div>
              <div class="metric-label">{label}</div>
              <div style="font-size:0.72rem;color:#64748b;margin-top:0.4rem;line-height:1.5;">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

section_divider()

# ── Dataset & Training Setup ──────────────────────────────────────────────────
section_header("Dataset & Training Setup", "How the model was built")

d1, d2 = st.columns(2)

with d1:
    st.markdown(
        """
        <div class="stat-panel">
          <div class="stat-panel-title">📦 Vehicle Detection Dataset</div>
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
            <span class="stat-row-key">Train / Val / Test Split</span>
            <span class="stat-row-val">70 / 15 / 15 %</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with d2:
    st.markdown(
        """
        <div class="stat-panel">
          <div class="stat-panel-title">⚙️ Training Configuration</div>
          <div class="stat-row">
            <span class="stat-row-key">Model Architecture</span>
            <span class="stat-row-val">YOLOv8s</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Training Epochs</span>
            <span class="stat-row-val">50</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">Framework</span>
            <span class="stat-row-val">Ultralytics</span>
          </div>
          <div class="stat-row">
            <span class="stat-row-key">GPU</span>
            <span class="stat-row-val">Tesla T4</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

section_divider()

# ── Vehicle Classes ───────────────────────────────────────────────────────────
section_header("Vehicle Classes", "All 11 categories the model detects")

classes = [
    "Articulated Truck",
    "Bicycle",
    "Bus",
    "Car",
    "Motorcycle",
    "Motorized Vehicle",
    "Non-motorized Vehicle",
    "Pedestrian",
    "Pickup Truck",
    "Single Unit Truck",
    "Work Van",
]

pills_html = '<div class="pill-grid">'
for cls in classes:
    pills_html += f'<span class="pill">{cls}</span>'
pills_html += "</div>"
st.markdown(pills_html, unsafe_allow_html=True)

section_divider()

# ── Performance Summary ───────────────────────────────────────────────────────
section_header("Performance Summary", "What the trained model delivers")

perf_items = [
    "Detects all 11 vehicle classes from real-world road images.",
    "Trained and evaluated end-to-end using the Ultralytics YOLOv8 pipeline.",
    "Achieved 69.2% mAP50 after 50 training epochs on Tesla T4 GPU.",
    "Inference confirmed successful on unseen, held-out test images.",
]

checklist_html = '<div class="checklist">'
for item in perf_items:
    checklist_html += f"""<div class="check-item">
<div class="check-icon">✓</div>
<p class="check-text">{item}</p>
</div>"""
checklist_html += "</div>"
st.markdown(checklist_html, unsafe_allow_html=True)

section_divider()

# ── Project Achievements ──────────────────────────────────────────────────────
section_header("Project Achievements", "End-to-end milestones completed")

achievements = [
    ("Dataset Analysis",           "Explored and profiled the 5,626-image vehicle detection dataset."),
    ("YOLO Label Conversion",      "Converted raw annotations to YOLO-compatible bounding box format."),
    ("Train / Val / Test Split",   "Structured dataset into clean splits for rigorous evaluation."),
    ("Vehicle Detection Training", "Trained YOLOv8s for 50 epochs on Tesla T4 GPU with Ultralytics."),
    ("Model Evaluation",           "Measured Precision (72.6%), Recall (64.0%), mAP50 (69.2%)."),
    ("Real-Time Inference",        "Deployed inference pipeline supporting live image upload and detection."),
    ("Tesla Safety Analytics",     "Analyzed 294 fatal cases across 23 countries for safety insights."),
    ("Streamlit Dashboard",        "Built this multi-page interactive analytics and detection platform."),
]

ach_html = '<div class="checklist">'
for title, desc in achievements:
    ach_html += f"""<div class="check-item">
<div class="check-icon">✓</div>
<div>
<p class="check-text" style="font-weight:700;margin-bottom:2px;">{title}</p>
<p style="font-size:0.78rem;color:#64748b;margin:0;">{desc}</p>
</div>
</div>"""
ach_html += "</div>"
st.markdown(ach_html, unsafe_allow_html=True)
