"""
theme.py — Shared Design System for AI Autonomous Driving Suite
Inject via: from theme import inject_css, render_sidebar
"""

import streamlit as st


# ─── CSS Design System ────────────────────────────────────────────────────────

GLOBAL_CSS = """
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

/* ── CSS Tokens ── */
:root {
  --navy:   #03045E;
  --blue:   #0077B6;
  --cyan:   #00B4D8;
  --aqua:   #90E0EF;
  --light:  #CAF0F8;
  --white:  #FFFFFF;
  --grey:   #64748b;
  --grey-light: #f1f5f9;
  --radius-sm:  10px;
  --radius-md:  16px;
  --radius-lg:  24px;
  --shadow-sm: 0 1px 4px rgba(3,4,94,.06), 0 2px 12px rgba(3,4,94,.04);
  --shadow-md: 0 4px 20px rgba(3,4,94,.08), 0 1px 4px rgba(3,4,94,.04);
  --shadow-lg: 0 8px 40px rgba(3,4,94,.12), 0 2px 8px rgba(3,4,94,.06);
  --transition: 0.22s cubic-bezier(.4,0,.2,1);
}

/* ── Base Reset ── */
html, body, [class*="css"] {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

/* ── Hide default Streamlit chrome (keep header visible for sidebar toggle) ── */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }

/* Hide the text/branding inside the header but keep the header container
   so the sidebar collapse/expand button (hamburger) stays accessible */
header[data-testid="stHeader"] {
  background: transparent !important;
  border-bottom: none !important;
  box-shadow: none !important;
}

/* Hide deploy button, toolbar action items, and app menu text */
.stDeployButton                           { display: none !important; }
[data-testid="stToolbarActions"]          { display: none !important; }
[data-testid="stMainMenuPopover"]         { display: none !important; }

/* Keep sidebar collapse button visible */
[data-testid="collapsedControl"] {
  display: flex !important;
  visibility: visible !important;
  background: white !important;
  border-radius: 0 8px 8px 0 !important;
  border: 1px solid #e8f4fb !important;
  border-left: none !important;
  box-shadow: 2px 0 8px rgba(3,4,94,.08) !important;
  padding: 0.5rem 0.4rem !important;
}
[data-testid="collapsedControl"] svg {
  color: #0077B6 !important;
  fill: #0077B6 !important;
}
.stApp {
  background: #f8fbff;
}

/* ── Sidebar chrome ── */
section[data-testid="stSidebar"] {
  background: var(--white) !important;
  border-right: 1px solid #e8f4fb !important;
  box-shadow: 2px 0 20px rgba(3,4,94,.05) !important;
}
section[data-testid="stSidebar"] > div:first-child {
  padding-top: 1.5rem !important;
}

/* ── Sidebar brand mark ── */
.sidebar-brand {
  padding: 0 1.2rem 1.5rem 1.2rem;
  border-bottom: 1px solid #e8f4fb;
  margin-bottom: 0.5rem;
}
.sidebar-brand h3 {
  font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 700 !important;
  color: var(--navy) !important;
  margin: 0 0 2px 0 !important;
  letter-spacing: -0.02em;
}
.sidebar-brand p {
  font-size: 0.72rem !important;
  color: var(--grey) !important;
  margin: 0 !important;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

/* ── option_menu overrides ── */
.nav-link {
  font-size: 0.85rem !important;
  font-weight: 500 !important;
  color: var(--grey) !important;
  border-radius: var(--radius-sm) !important;
  margin: 2px 0 !important;
  transition: background var(--transition), color var(--transition) !important;
}
.nav-link:hover {
  background: var(--light) !important;
  color: var(--blue) !important;
}
.nav-link-selected {
  background: linear-gradient(135deg, #e0f4fc 0%, #caf0f8 100%) !important;
  color: var(--navy) !important;
  font-weight: 600 !important;
  border-left: 3px solid var(--cyan) !important;
}
.nav-link-selected .icon { color: var(--cyan) !important; }

/* ── Main content area ── */
.main .block-container {
  padding: 2rem 3rem 4rem 3rem !important;
  max-width: 1200px !important;
}

/* ── Page fade-in ── */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.page-enter {
  animation: fadeInUp 0.45s ease forwards;
}

/* ── Hero section ── */
.hero-section {
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 40%, #caf0f8 100%);
  border-radius: var(--radius-lg);
  padding: 3.5rem 3rem;
  margin-bottom: 2.5rem;
  position: relative;
  overflow: hidden;
  animation: fadeInUp 0.5s ease forwards;
}
.hero-section::before {
  content: '';
  position: absolute; top: -40px; right: -40px;
  width: 280px; height: 280px;
  background: radial-gradient(circle, rgba(0,180,216,.12) 0%, transparent 70%);
  border-radius: 50%;
}
.hero-section::after {
  content: '';
  position: absolute; bottom: -60px; left: 20%;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(144,224,239,.18) 0%, transparent 70%);
  border-radius: 50%;
}
.hero-title {
  font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
  font-size: 2.6rem !important;
  font-weight: 800 !important;
  color: var(--navy) !important;
  letter-spacing: -0.04em;
  line-height: 1.15;
  margin: 0 0 0.75rem 0 !important;
}
.hero-subtitle {
  font-size: 1.05rem !important;
  color: #334e68 !important;
  font-weight: 400;
  line-height: 1.7;
  max-width: 640px;
  margin: 0 !important;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0,119,182,.1);
  color: var(--blue);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: 100px;
  padding: 4px 12px;
  margin-bottom: 1.2rem;
}

/* ── Section headings ── */
.section-heading {
  font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
  font-size: 1.35rem !important;
  font-weight: 700 !important;
  color: var(--navy) !important;
  letter-spacing: -0.02em;
  margin: 0 0 0.3rem 0 !important;
}
.section-sub {
  font-size: 0.88rem;
  color: var(--grey);
  margin: 0 0 1.5rem 0 !important;
}
.section-divider {
  border: none;
  border-top: 1px solid #e8f4fb;
  margin: 2.5rem 0 !important;
}

/* ── KPI Cards ── */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 2.5rem;
}
.kpi-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.5rem 1.25rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(144,224,239,.3);
  transition: transform var(--transition), box-shadow var(--transition);
  position: relative;
  overflow: hidden;
  animation: fadeInUp 0.5s ease forwards;
}
.kpi-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}
.kpi-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--cyan), var(--blue));
}
.kpi-label {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--grey);
  margin: 0 0 0.5rem 0;
}
.kpi-value {
  font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--navy);
  line-height: 1;
  margin: 0 0 0.25rem 0;
}
.kpi-sub {
  font-size: 0.75rem;
  color: var(--grey);
}
.kpi-icon {
  position: absolute; top: 1.2rem; right: 1.2rem;
  width: 36px; height: 36px;
  background: linear-gradient(135deg, var(--light), var(--aqua));
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1rem;
}

/* ── Insight Cards ── */
.insight-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}
.insight-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.25rem 1.25rem 1.25rem 1.5rem;
  border-left: 4px solid var(--cyan);
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition), box-shadow var(--transition);
  animation: fadeInUp 0.5s ease forwards;
}
.insight-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}
.insight-tag {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cyan);
  margin: 0 0 0.4rem 0;
}
.insight-text {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--navy);
  line-height: 1.5;
  margin: 0;
}

/* ── Pipeline Component ── */
.pipeline-wrap {
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: 2rem 2.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid #e8f4fb;
  margin-bottom: 2rem;
  overflow-x: auto;
  animation: fadeInUp 0.5s ease forwards;
}
.pipeline-flow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  flex-wrap: nowrap;
  min-width: max-content;
}
.pipeline-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.pipeline-icon {
  width: 52px; height: 52px;
  border-radius: 14px;
  background: linear-gradient(135deg, var(--light), var(--aqua));
  display: flex; align-items: center; justify-content: center;
  font-size: 1.3rem;
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition);
}
.pipeline-icon:hover { transform: scale(1.08); }
.pipeline-label {
  font-size: 0.7rem;
  font-weight: 600;
  color: var(--navy);
  text-align: center;
  letter-spacing: 0.02em;
  max-width: 72px;
  line-height: 1.3;
}
.pipeline-arrow {
  width: 40px;
  display: flex; align-items: center; justify-content: center;
  color: var(--cyan);
  font-size: 1.2rem;
  flex-shrink: 0;
}
@keyframes arrowPulse {
  0%,100% { opacity: 0.5; transform: translateX(0); }
  50%      { opacity: 1;   transform: translateX(3px); }
}
.pipeline-arrow span {
  display: inline-block;
  animation: arrowPulse 1.8s ease infinite;
}

/* ── Tech Stack Cards ── */
.tech-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid #e8f4fb;
  transition: transform var(--transition), box-shadow var(--transition);
  height: 100%;
  animation: fadeInUp 0.5s ease forwards;
}
.tech-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.tech-card-icon {
  width: 44px; height: 44px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--light), var(--aqua));
  display: flex; align-items: center; justify-content: center;
  font-size: 1.3rem;
  margin-bottom: 0.9rem;
}
.tech-card-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--navy);
  margin: 0 0 0.75rem 0;
  letter-spacing: -0.01em;
}
.tech-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  color: var(--grey);
  padding: 4px 0;
  font-weight: 400;
}
.tech-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--cyan);
  flex-shrink: 0;
}

/* ── Stat Panel Cards ── */
.stat-panel {
  background: linear-gradient(135deg, #f0f9ff 0%, #e8f4fb 100%);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  border: 1px solid rgba(144,224,239,.4);
  box-shadow: var(--shadow-sm);
  animation: fadeInUp 0.5s ease forwards;
}
.stat-panel-title {
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--blue);
  margin: 0 0 1rem 0;
}
.stat-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.4rem 0;
  border-bottom: 1px solid rgba(144,224,239,.3);
}
.stat-row:last-child { border-bottom: none; }
.stat-row-key {
  font-size: 0.82rem;
  color: var(--grey);
  font-weight: 400;
}
.stat-row-val {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--navy);
}

/* ── Goal Banner ── */
.goal-banner {
  background: linear-gradient(135deg, var(--navy) 0%, #023e8a 100%);
  border-radius: var(--radius-lg);
  padding: 2rem 2.5rem;
  color: var(--white);
  position: relative;
  overflow: hidden;
  animation: fadeInUp 0.5s ease forwards;
}
.goal-banner::before {
  content: '';
  position: absolute; top: -30px; right: -30px;
  width: 180px; height: 180px;
  background: radial-gradient(circle, rgba(0,180,216,.2) 0%, transparent 70%);
  border-radius: 50%;
}
.goal-banner p {
  font-size: 1rem;
  line-height: 1.75;
  opacity: 0.92;
  max-width: 800px;
  margin: 0;
  position: relative; z-index: 1;
}
.goal-banner h4 {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cyan);
  margin: 0 0 0.6rem 0;
  position: relative; z-index: 1;
}

/* ── Analytics Image Frame ── */
.chart-frame {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  box-shadow: var(--shadow-md);
  border: 1px solid #e8f4fb;
  margin-bottom: 1rem;
  transition: transform var(--transition), box-shadow var(--transition);
  animation: fadeInUp 0.5s ease forwards;
}
.chart-frame:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
.chart-caption {
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--blue);
  margin: 0.75rem 0 0.3rem 0;
}
.chart-insight {
  font-size: 0.84rem;
  color: var(--grey);
  line-height: 1.6;
  margin: 0;
}

/* ── Finding Tags ── */
.findings-list {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.finding-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  background: var(--white);
  border-radius: var(--radius-sm);
  padding: 0.9rem 1rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid #e8f4fb;
  transition: transform var(--transition);
  animation: fadeInUp 0.5s ease forwards;
}
.finding-item:hover { transform: translateX(4px); }
.finding-num {
  width: 26px; height: 26px;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--cyan), var(--blue));
  color: white;
  font-size: 0.72rem;
  font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.finding-text {
  font-size: 0.87rem;
  color: var(--navy);
  font-weight: 500;
  line-height: 1.5;
  margin: 0; padding-top: 2px;
}

/* ── Upload Zone ── */
.upload-zone {
  border: 2px dashed var(--aqua);
  border-radius: var(--radius-lg);
  background: linear-gradient(135deg, #f0f9ff, #e8f4fb);
  padding: 2.5rem;
  text-align: center;
  transition: border-color var(--transition), background var(--transition);
}
.upload-zone:hover {
  border-color: var(--cyan);
  background: linear-gradient(135deg, #e0f4fc, #caf0f8);
}
.upload-icon { font-size: 2.5rem; margin-bottom: 0.5rem; }
.upload-title {
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--navy);
  margin: 0 0 0.3rem 0;
}
.upload-sub {
  font-size: 0.82rem;
  color: var(--grey);
}

/* ── Primary Button ── */
div.stButton > button {
  background: linear-gradient(135deg, var(--blue), #005f8e) !important;
  color: white !important;
  border: none !important;
  border-radius: 100px !important;
  padding: 0.65rem 2rem !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.02em;
  box-shadow: 0 4px 14px rgba(0,119,182,.35) !important;
  transition: transform var(--transition), box-shadow var(--transition), background var(--transition) !important;
  cursor: pointer;
}
div.stButton > button:hover {
  background: linear-gradient(135deg, var(--navy), #023e8a) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(3,4,94,.35) !important;
}
div.stButton > button:active {
  transform: translateY(0) !important;
}

/* ── Detection Result Frame ── */
.detection-frame {
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid #e8f4fb;
  animation: fadeInUp 0.45s ease forwards;
}
.detection-frame-label {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cyan);
  margin: 0 0 0.8rem 0;
}

/* ── Vehicle Count Cards ── */
.vehicle-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}
.vehicle-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid #e8f4fb;
  text-align: center;
  transition: transform var(--transition), box-shadow var(--transition);
  animation: fadeInUp 0.4s ease forwards;
}
.vehicle-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.vehicle-icon { font-size: 1.5rem; margin-bottom: 0.4rem; }
.vehicle-name {
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--grey);
  text-transform: capitalize;
  margin: 0 0 0.2rem 0;
  line-height: 1.3;
}
.vehicle-count {
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--navy);
  line-height: 1;
}

/* ── Confidence Bars ── */
.conf-list { display: flex; flex-direction: column; gap: 0.5rem; }
.conf-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background: var(--white);
  border-radius: var(--radius-sm);
  padding: 0.6rem 0.9rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid #e8f4fb;
}
.conf-name {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--navy);
  min-width: 140px;
  flex-shrink: 0;
  text-transform: capitalize;
}
.conf-bar-wrap {
  flex: 1;
  height: 8px;
  background: var(--light);
  border-radius: 100px;
  overflow: hidden;
}
.conf-bar {
  height: 100%;
  border-radius: 100px;
  transition: width 0.8s cubic-bezier(.4,0,.2,1);
}
.conf-pct {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--navy);
  min-width: 38px;
  text-align: right;
}

/* ── Total Card ── */
.total-card {
  background: linear-gradient(135deg, var(--navy), #023e8a);
  border-radius: var(--radius-md);
  padding: 1.5rem 2rem;
  color: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-lg);
  animation: fadeInUp 0.5s ease forwards;
}
.total-label {
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--aqua);
  margin: 0 0 0.25rem 0;
}
.total-value {
  font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
  font-size: 2.6rem;
  font-weight: 800;
  color: white;
  line-height: 1;
}
.total-icon {
  font-size: 3rem;
  opacity: 0.3;
}

/* ── Metric Cards (Model Performance) ── */
.metric-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.75rem 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(144,224,239,.3);
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: transform var(--transition), box-shadow var(--transition);
  animation: fadeInUp 0.5s ease forwards;
}
.metric-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
.metric-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--cyan), var(--blue));
}
.metric-ring-wrap {
  position: relative;
  width: 80px; height: 80px;
  margin: 0 auto 0.8rem auto;
}
.metric-ring-wrap svg {
  transform: rotate(-90deg);
}
.metric-ring-bg { fill: none; stroke: var(--light); stroke-width: 6; }
.metric-ring-fg {
  fill: none;
  stroke: url(#ringGrad);
  stroke-width: 6;
  stroke-linecap: round;
  transition: stroke-dasharray 1s cubic-bezier(.4,0,.2,1);
}
.metric-ring-text {
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--navy);
  line-height: 1;
}
.metric-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--grey);
  margin: 0;
}
.metric-value-large {
  font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
  font-size: 2.4rem;
  font-weight: 800;
  color: var(--navy);
  line-height: 1;
  margin: 0 0 0.3rem 0;
}

/* ── Pill Tags ── */
.pill-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}
.pill {
  background: linear-gradient(135deg, var(--light), #d6edf9);
  color: var(--navy);
  border-radius: 100px;
  padding: 5px 14px;
  font-size: 0.78rem;
  font-weight: 600;
  border: 1px solid rgba(144,224,239,.5);
  transition: transform var(--transition), box-shadow var(--transition);
  cursor: default;
}
.pill:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-sm);
  background: linear-gradient(135deg, var(--aqua), var(--cyan));
  color: white;
}

/* ── Checklist / Achievement Steps ── */
.checklist { display: flex; flex-direction: column; gap: 0.5rem; }
.check-item {
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--white);
  border-radius: var(--radius-sm);
  padding: 0.8rem 1rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid #e8f4fb;
  transition: transform var(--transition);
  animation: fadeInUp 0.5s ease forwards;
}
.check-item:hover { transform: translateX(4px); }
.check-icon {
  width: 28px; height: 28px;
  border-radius: 8px;
  background: linear-gradient(135deg, #d1fae5, #6ee7b7);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.85rem;
  flex-shrink: 0;
}
.check-text {
  font-size: 0.87rem;
  font-weight: 500;
  color: var(--navy);
  margin: 0;
}

/* ── Module Cards ── */
.module-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(144,224,239,.3);
  border-top: 4px solid var(--cyan);
  transition: transform var(--transition), box-shadow var(--transition);
  height: 100%;
  animation: fadeInUp 0.5s ease forwards;
}
.module-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
.module-icon { font-size: 1.8rem; margin-bottom: 0.7rem; }
.module-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--navy);
  margin: 0 0 0.4rem 0;
  letter-spacing: -0.01em;
}
.module-desc {
  font-size: 0.8rem;
  color: var(--grey);
  line-height: 1.6;
  margin: 0;
}

/* ── Timeline ── */
.timeline { position: relative; padding-left: 2rem; }
.timeline::before {
  content: '';
  position: absolute; left: 10px; top: 0; bottom: 0;
  width: 2px;
  background: linear-gradient(to bottom, var(--cyan), var(--blue), var(--navy));
}
.timeline-item {
  position: relative;
  padding: 0 0 1.5rem 1.5rem;
  animation: fadeInUp 0.5s ease forwards;
}
.timeline-item:last-child { padding-bottom: 0; }
.timeline-dot {
  position: absolute; left: -2rem; top: 4px;
  width: 20px; height: 20px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--cyan), var(--blue));
  border: 3px solid white;
  box-shadow: 0 0 0 2px var(--aqua);
}
.timeline-step {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cyan);
  margin: 0 0 0.2rem 0;
}
.timeline-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--navy);
  margin: 0 0 0.3rem 0;
}
.timeline-desc {
  font-size: 0.82rem;
  color: var(--grey);
  line-height: 1.6;
  margin: 0;
}

/* ── Result Tiles ── */
.result-tile {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  text-align: center;
  box-shadow: var(--shadow-md);
  border: 1px solid rgba(144,224,239,.3);
  position: relative;
  overflow: hidden;
  transition: transform var(--transition), box-shadow var(--transition);
  animation: fadeInUp 0.5s ease forwards;
}
.result-tile:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}
.result-tile::before {
  content: '';
  position: absolute; bottom: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--cyan), var(--blue));
}
.result-value {
  font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
  font-size: 2rem;
  font-weight: 800;
  color: var(--navy);
  line-height: 1;
  margin: 0 0 0.3rem 0;
}
.result-label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--grey);
  margin: 0;
}

/* ── Roadmap Cards ── */
.roadmap-card {
  background: var(--white);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid #e8f4fb;
  transition: transform var(--transition), box-shadow var(--transition);
  animation: fadeInUp 0.5s ease forwards;
}
.roadmap-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.roadmap-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  background: rgba(0,180,216,.1);
  color: var(--blue);
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: 100px;
  padding: 3px 9px;
  margin-bottom: 0.6rem;
}
.roadmap-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--navy);
  margin: 0 0 0.3rem 0;
}
.roadmap-desc {
  font-size: 0.78rem;
  color: var(--grey);
  line-height: 1.5;
  margin: 0;
}

/* ── Closing Banner ── */
.closing-banner {
  background: linear-gradient(135deg, #f0f9ff 0%, #caf0f8 100%);
  border-radius: var(--radius-lg);
  padding: 2rem 2.5rem;
  border: 1px solid rgba(0,180,216,.2);
  text-align: center;
  animation: fadeInUp 0.5s ease forwards;
}
.closing-banner p {
  font-size: 1.05rem;
  font-weight: 500;
  color: var(--navy);
  line-height: 1.75;
  max-width: 700px;
  margin: 0 auto;
}

/* ── Streamlit widget cleanup ── */
div[data-testid="stFileUploader"] {
  border: none !important;
  background: transparent !important;
}
div[data-testid="stFileUploader"] > div {
  border: 2px dashed var(--aqua) !important;
  border-radius: var(--radius-lg) !important;
  background: linear-gradient(135deg, #f0f9ff, #e8f4fb) !important;
  transition: all var(--transition) !important;
  padding: 1.5rem !important;
}
div[data-testid="stFileUploader"] > div:hover {
  border-color: var(--cyan) !important;
  background: linear-gradient(135deg, #e0f4fc, #caf0f8) !important;
}

/* ── Expander cleanup ── */
.streamlit-expanderHeader {
  background: var(--white) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--navy) !important;
  font-weight: 600 !important;
}

/* ── Custom scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #f0f9ff; }
::-webkit-scrollbar-thumb {
  background: var(--aqua);
  border-radius: 100px;
}
::-webkit-scrollbar-thumb:hover { background: var(--cyan); }

/* ── SVG gradient def for rings (hidden element) ── */
.svg-defs { position: absolute; width: 0; height: 0; overflow: hidden; }
</style>
"""


def inject_css():
    """Inject the full shared design system CSS."""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


def render_sidebar():
    """
    Renders the branded sidebar with st.page_link navigation.
    Uses Streamlit's native page routing - no redirect loops.
    """
    # Hide the default Streamlit multipage nav; style page_link buttons
    st.markdown(
        """
        <style>
        /* Hide only the default auto-generated nav, not our custom one */
        [data-testid="stSidebarNav"] { display: none !important; }

        /* Style our page_link nav items */
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {
            display: flex !important;
            align-items: center !important;
            padding: 0.55rem 1rem !important;
            border-radius: 10px !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            color: #64748b !important;
            text-decoration: none !important;
            transition: background 0.2s ease, color 0.2s ease !important;
            margin: 2px 0 !important;
        }
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"]:hover {
            background: #e0f4fc !important;
            color: #0077B6 !important;
        }
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"][aria-current="page"] {
            background: linear-gradient(135deg, #e0f4fc, #caf0f8) !important;
            color: #03045E !important;
            font-weight: 600 !important;
            border-left: 3px solid #00B4D8 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
              <h3>AI Driving Suite</h3>
              <p>Autonomous Intelligence Platform</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.page_link("dashboard.py",                   label="  Overview",           icon="🏠")
        st.page_link("pages/2_Tesla_Analytics.py",     label="  Tesla Analytics",    icon="📊")
        st.page_link("pages/3_Vehicle_Detection.py",   label="  Vehicle Detection",  icon="🔍")
        st.page_link("pages/4_Model_Performance.py",   label="  Model Performance",  icon="📈")
        st.page_link("pages/5_About_Project.py",       label="  About Project",      icon="ℹ️")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="
              padding: 0.75rem 1rem;
              background: linear-gradient(135deg, #f0f9ff, #caf0f8);
              border-radius: 10px;
              border: 1px solid rgba(144,224,239,.4);
            ">
              <div style="font-size:0.68rem;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#0077B6;margin-bottom:0.3rem;">Model Status</div>
              <div style="font-size:0.8rem;font-weight:600;color:#03045E;">✓ YOLOv8s · mAP50 69.2%</div>
              <div style="font-size:0.72rem;color:#64748b;margin-top:2px;">Ready for inference</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def kpi_cards(items):
    """
    Render a row of KPI cards.
    items: list of (label, value, icon, sub_label)
    """
    cols = st.columns(len(items))
    for col, (label, value, icon, sub) in zip(cols, items):
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                  <div class="kpi-icon">{icon}</div>
                  <div class="kpi-label">{label}</div>
                  <div class="kpi-value">{value}</div>
                  <div class="kpi-sub">{sub}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def section_header(title, sub=""):
    """Render a styled section heading."""
    st.markdown(
        f'<h2 class="section-heading">{title}</h2>'
        + (f'<p class="section-sub">{sub}</p>' if sub else ""),
        unsafe_allow_html=True,
    )


def section_divider():
    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


def page_hero(badge, title, subtitle):
    """Render the standard page hero section."""
    st.markdown(
        f"""
        <div class="hero-section">
          <div class="hero-badge">{badge}</div>
          <h1 class="hero-title">{title}</h1>
          <p class="hero-subtitle">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


import base64
from io import BytesIO
import numpy as np
from PIL import Image

def render_image_frame(image_source, caption=None, frame_class="chart-frame", caption_class="chart-caption"):
    """
    Renders an image fully encapsulated inside a styled HTML div container.
    Fixes the issue where st.markdown('<div ...>') and st.image() break apart in Streamlit.
    """
    if isinstance(image_source, str):
        img = Image.open(image_source)
    elif isinstance(image_source, np.ndarray):
        # Ultralytics returns BGR arrays, convert to RGB for PIL
        img = Image.fromarray(image_source[..., ::-1])
    else:
        img = image_source  # Assume PIL Image

    # Handle RGBA to RGB if saving as JPEG, but we'll use PNG to be safe
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    caption_html = f'<div class="{caption_class}">{caption}</div>' if caption else ""
    
    html = f'''
    <div class="{frame_class}">
      <img src="data:image/png;base64,{img_str}" style="width: 100%; height: auto; border-radius: var(--radius-sm); display: block;">
      {caption_html}
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)
