from ultralytics import YOLO
import streamlit as st
from PIL import Image
import tempfile
from collections import Counter
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from theme import inject_css, render_sidebar, section_header, section_divider, render_image_frame, page_hero

st.set_page_config(
    page_title="Vehicle Detection · AI Driving Suite",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
render_sidebar()

@st.cache_resource
def load_yolo_model():
    return YOLO("best.pt")

# ── Page Hero ────────────────────────────────────────────────────────────────
page_hero(
    badge="🔍 YOLOv8 · Real-time Object Detection",
    title="Vehicle Detection",
    subtitle=(
        "Upload a road or traffic image and let the trained YOLOv8 model detect "
        "and classify up to 11 vehicle categories in real time. Visualize bounding "
        "boxes, per-class counts, and confidence scores — all in one workspace."
    )
)

# ── Upload Zone ───────────────────────────────────────────────────────────────
col_upload, col_preview = st.columns([1, 1], gap="large")

with col_upload:
    section_header("Upload Image", "Supports JPG, JPEG, PNG")

    uploaded_file = st.file_uploader(
        "Drag & drop an image or click to browse",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
    )

    if uploaded_file:
        st.markdown(
            '<p style="font-size:0.8rem;color:#64748b;margin-top:0.5rem;">✅ Image loaded — ready to detect</p>',
            unsafe_allow_html=True,
        )

with col_preview:
    if uploaded_file:
        section_header("Preview", "Original uploaded image")
        image = Image.open(uploaded_file)
        st.image(image, width="stretch")

section_divider()

# ── Detect Button + Results ───────────────────────────────────────────────────
if uploaded_file:

    # Re-open image (after the preview column consumed it)
    uploaded_file.seek(0)
    image = Image.open(uploaded_file)

    col_btn, _ = st.columns([1, 3])
    with col_btn:
        detect_clicked = st.button("🔍  Detect Vehicles", type="primary")

    if detect_clicked:

        with st.spinner("Running YOLOv8 inference…"):

            # ── Model inference (logic unchanged) ────────────────────────────
            model = load_yolo_model()

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg",
            )
            image.save(temp_file.name)

            results = model.predict(source=temp_file.name, conf=0.25)
            result  = results[0]
            plotted = result.plot()
            
            # Clean up the temporary file
            try:
                os.remove(temp_file.name)
            except Exception:
                pass

            names           = model.names
            detected_classes = [names[int(cls)] for cls in result.boxes.cls]
            counts          = Counter(detected_classes)
            total           = len(detected_classes)
            # ─────────────────────────────────────────────────────────────────

        section_divider()

        # ── Detection Result ──────────────────────────────────────────────
        section_header("Detection Result", "YOLOv8 bounding-box output")

        render_image_frame(plotted, "Annotated Output", frame_class="detection-frame", caption_class="detection-frame-label")

        section_divider()

        # ── Total Vehicles Banner ─────────────────────────────────────────
        st.markdown(
            f"""
            <div class="total-card">
              <div>
                <div class="total-label">Total Vehicles Detected</div>
                <div class="total-value">{total}</div>
              </div>
              <div class="total-icon">🚘</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Vehicle Class Counts Grid ─────────────────────────────────────
        if counts:
            section_header("Detected Vehicles", "Per-class breakdown")

            vehicle_icons = {
                "car": "🚗",
                "bus": "🚌",
                "truck": "🚛",
                "motorcycle": "🏍️",
                "bicycle": "🚲",
                "pedestrian": "🚶",
                "van": "🚐",
                "pickup_truck": "🛻",
                "articulated_truck": "🚚",
                "single_unit_truck": "🚛",
                "motorized_vehicle": "🚗",
                "non-motorized_vehicle": "🚲",
                "work_van": "🚐",
            }

            vehicle_cards_html = '<div class="vehicle-grid">'
            for vehicle, count in sorted(counts.items(), key=lambda x: -x[1]):
                icon = vehicle_icons.get(vehicle.lower(), "🚘")
                name = vehicle.replace("_", " ").title()
                vehicle_cards_html += f"""<div class="vehicle-card">
<div class="vehicle-icon">{icon}</div>
<div class="vehicle-name">{name}</div>
<div class="vehicle-count">{count}</div>
</div>"""
            vehicle_cards_html += "</div>"
            st.markdown(vehicle_cards_html, unsafe_allow_html=True)

        section_divider()

        # ── Confidence Scores ─────────────────────────────────────────────
        section_header("Confidence Scores", "Per-detection confidence levels")

        conf_html = '<div class="conf-list">'
        for box in sorted(result.boxes, key=lambda b: float(b.conf[0]), reverse=True):
            cls_id   = int(box.cls[0])
            conf_val = float(box.conf[0])
            name     = names[cls_id].replace("_", " ").title()
            pct      = int(conf_val * 100)

            # Color gradient: low conf → aqua, high conf → navy
            if pct >= 80:
                bar_color = "linear-gradient(90deg, #0077B6, #03045E)"
            elif pct >= 60:
                bar_color = "linear-gradient(90deg, #00B4D8, #0077B6)"
            else:
                bar_color = "linear-gradient(90deg, #90E0EF, #00B4D8)"

            conf_html += f"""<div class="conf-item">
<span class="conf-name">{name}</span>
<div class="conf-bar-wrap"><div class="conf-bar" style="width:{pct}%; background:{bar_color};"></div></div>
<span class="conf-pct">{pct}%</span>
</div>"""
        conf_html += "</div>"
        st.markdown(conf_html, unsafe_allow_html=True)

else:
    # Empty state
    st.markdown(
        """
        <div style="
          border: 2px dashed #90E0EF;
          border-radius: 24px;
          background: linear-gradient(135deg, #f0f9ff, #e8f4fb);
          padding: 4rem;
          text-align: center;
          margin-top: 1rem;
        ">
          <div style="font-size:3rem; margin-bottom:1rem;">📸</div>
          <div style="font-size:1.1rem; font-weight:600; color:#03045E; margin-bottom:0.5rem;">
            No image uploaded yet
          </div>
          <div style="font-size:0.85rem; color:#64748b;">
            Use the uploader above to provide a road or traffic image, then click <strong>Detect Vehicles</strong>.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
