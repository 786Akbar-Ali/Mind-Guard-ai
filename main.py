# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  MINDGUARD AI — Student Mental Health Burnout Prediction System          ║
# ║  Developer : Akbar Ali  |  NAVTTC / Corvit Systems Rawalpindi            ║
# ║  ✨ Clean & Beautiful UI — Guaranteed to Render                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

import warnings
import os
import time
import streamlit as st
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import joblib
import streamlit as st
from PIL import Image
import os


# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MindGuard AI | Burnout Predictor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ──────────────────────────────────────────────────────────────────────────────
# 🎨 CLEAN & MODERN CSS (Tested, No Errors)
def load_css():
    st.markdown("""
    <style>
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Reset */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0B1120 0%, #0A0F1A 100%);
    }

    /* Hide Streamlit branding */
    #MainMenu, footer, header {
        visibility: hidden;
    }
    div[data-testid="stToolbar"] {
        display: none;
    }
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    .block-container {
        padding: 0 2rem !important;
        max-width: 1300px !important;
        margin: 0 auto !important;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #1E293B;
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #4F46E5;
        border-radius: 10px;
    }

    /* Color variables */
    :root {
        --primary: #4F46E5;
        --primary-light: #818CF8;
        --secondary: #10B981;
        --warning: #F59E0B;
        --danger: #EF4444;
        --card-bg: rgba(17, 24, 39, 0.7);
        --border-color: rgba(79, 70, 229, 0.2);
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --radius: 20px;
    }

    /* Navbar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background: rgba(11, 17, 32, 0.8);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid var(--border-color);
        margin-bottom: 2rem;
        border-radius: 0 0 20px 20px;
    }
    .nav-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .nav-logo {
        background: linear-gradient(135deg, var(--primary), var(--primary-light));
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
    }
    .nav-title {
        font-size: 1.3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #fff, var(--primary-light));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    .nav-stats {
        display: flex;
        gap: 12px;
    }
    .stat-pill {
        background: rgba(255,255,255,0.05);
        padding: 6px 14px;
        border-radius: 40px;
        font-size: 0.75rem;
        font-weight: 500;
        color: var(--text-secondary);
        border: 1px solid rgba(255,255,255,0.1);
    }
    .online-badge {
        background: rgba(16, 185, 129, 0.1);
        border-color: rgba(16, 185, 129, 0.3);
        color: var(--secondary);
    }

    /* Hero */
    .hero {
        text-align: center;
        margin: 2rem 0 3rem;
    }
    .hero h1 {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff, var(--primary-light));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin-bottom: 1rem;
    }
    .hero p {
        color: var(--text-secondary);
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* Metrics */
    .metrics {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        margin: 2rem 0;
    }
    .metric-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s;
    }
    .metric-card:hover {
        transform: translateY(-4px);
        border-color: var(--primary);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        color: var(--primary-light);
    }
    .metric-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--text-secondary);
        margin-top: 0.5rem;
    }

    /* Input cards */
    .input-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .section-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: var(--primary-light);
        margin-bottom: 1.5rem;
    }

    /* Result banner */
    .result-banner {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border-left: 6px solid;
        border-radius: var(--radius);
        padding: 1.5rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    .risk-low { border-left-color: var(--secondary); }
    .risk-medium { border-left-color: var(--warning); }
    .risk-high { border-left-color: var(--danger); }
    .risk-badge {
        font-size: 1.8rem;
        font-weight: 800;
    }
    .risk-score {
        font-size: 2rem;
        font-weight: 800;
        color: white;
    }

    /* Charts */
    .chart-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1rem;
        margin-bottom: 1.5rem;
    }

    /* Recommendations */
    .rec-card {
        background: var(--card-bg);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1rem;
        display: flex;
        gap: 1rem;
        transition: all 0.3s;
    }
    .rec-card:hover {
        transform: translateY(-2px);
        border-color: var(--primary);
    }
    .rec-icon {
        font-size: 1.8rem;
    }
    .rec-title {
        font-weight: 700;
        color: white;
        margin-bottom: 0.3rem;
    }
    .rec-desc {
        font-size: 0.8rem;
        color: var(--text-secondary);
    }

    /* Developer card (new design) */
    .dev-card {
        background: linear-gradient(135deg, #071a3a, #020617);
        border: 1px solid #1E3A8A;
        border-radius: 20px;
        padding: 30px;
        margin-top: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    .dev-header {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 25px;
    }
    .dev-avatar {
        width: 70px;
        height: 70px;
        border-radius: 18px;
        background: linear-gradient(135deg, #6366F1, #9333EA);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        font-weight: 700;
        color: white;
    }
    .dev-text h2 {
        margin: 0;
        color: white;
        font-size: 26px;
    }
    .dev-text p {
        margin: 0;
        color: #60A5FA;
        font-size: 13px;
        letter-spacing: 2px;
    }
    .dev-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
    }
    .pill {
        background: rgba(255,255,255,0.05);
        border: 1px solid #334155;
        padding: 10px 16px;
        border-radius: 12px;
        font-size: 14px;
        color: #CBD5F5;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 2rem;
        border-top: 1px solid var(--border-color);
        color: var(--text-secondary);
        font-size: 0.75rem;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .metrics { grid-template-columns: repeat(2, 1fr); }
        .hero h1 { font-size: 2rem; }
        .result-banner { flex-direction: column; text-align: center; gap: 1rem; }
        .dev-header { flex-direction: column; text-align: center; }
        .dev-pills { justify-content: center; }
    }
    </style>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# Load model
@st.cache_resource
def load_artifacts():
    errors = []
    model = scaler = None
    if not os.path.exists("mental_health_model.pkl"):
        errors.append("❌ mental_health_model.pkl not found")
    else:
        try:
            model = joblib.load("mental_health_model.pkl")
        except Exception as e:
            errors.append(f"Model error: {e}")
    if not os.path.exists("scaler.pkl"):
        errors.append("❌ scaler.pkl not found")
    else:
        try:
            scaler = joblib.load("scaler.pkl")
        except Exception as e:
            errors.append(f"Scaler error: {e}")
    if model and scaler and scaler.n_features_in_ != 9:
        errors.append(f"Feature mismatch: expected {scaler.n_features_in_}, got 9")
        model = scaler = None
    return model, scaler, errors


# ──────────────────────────────────────────────────────────────────────────────
def main():
    load_css()

    # Load model
    model, scaler, errors = load_artifacts()
    model_ok = model is not None and scaler is not None


    st.set_page_config(
        page_title="MindGuard AI | Burnout Predictor",
        page_icon="logo.png",
        layout="wide"
    )
    # Navbar
    st.markdown(f"""
    
    <div class="navbar">
        <div class="nav-brand">
            <div class="nav-logo">🧠</div>
            <span class="nav-title">MindGuard AI</span>
        </div>
        <div class="nav-stats">
            <div class="stat-pill">9 Features</div>
            <div class="stat-pill">Random Forest</div>
            <div class="stat-pill">3 Classes</div>
            {"<div class='stat-pill online-badge'>✅ Model Online</div>" if model_ok else "<div class='stat-pill' style='color:#EF4444;'>⚠️ Model Missing</div>"}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hero
    st.markdown("""
    <div class="hero">
        <h1>AI Student Burnout Detection System</h1>
        <p>Predict mental health burnout risk using machine learning — early intervention starts here.</p>
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    st.markdown("""
    <div class="metrics">
        <div class="metric-card"><div class="metric-value">9</div><div class="metric-label">Risk Features</div></div>
        <div class="metric-card"><div class="metric-value">Random Forest</div><div class="metric-label">Model Type</div></div>
        <div class="metric-card"><div class="metric-value">3</div><div class="metric-label">Risk Classes</div></div>
        <div class="metric-card"><div class="metric-value">⚡ Live</div><div class="metric-label">AI Inference</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Show errors if any
    if errors:
        for err in errors:
            st.error(err)
        st.info("Please run `python train_model.py` to generate the model files, then refresh.")
        model_ok = False

    # Input form
    with st.form("burnout_form"):
        # Academic Environment
        st.markdown('<div class="input-card"><div class="section-title">📚 Academic Environment</div>',
                    unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            study_hours = st.slider("Study Hours / Day", 0.0, 14.0, 5.0, 0.5, disabled=not model_ok)
        with col2:
            sleep_hours = st.slider("Sleep Hours / Night", 2.0, 12.0, 7.0, 0.5, disabled=not model_ok)
        with col3:
            academic_pressure = st.slider("Academic Pressure (1-10)", 1, 10, 5, disabled=not model_ok)
        st.markdown('</div>', unsafe_allow_html=True)

        # Mental Health
        st.markdown('<div class="input-card"><div class="section-title">🧠 Mental Health Indicators</div>',
                    unsafe_allow_html=True)
        col4, col5, col6, col7 = st.columns(4)
        with col4:
            stress_level = st.slider("Stress Level", 1, 10, 5, disabled=not model_ok)
        with col5:
            anxiety_score = st.slider("Anxiety Score", 1, 10, 4, disabled=not model_ok)
        with col6:
            age = st.slider("Age", 15, 35, 20, 1, disabled=not model_ok)
        with col7:
            gender = st.selectbox("Gender", ["Male", "Female"], disabled=not model_ok)
        st.markdown('</div>', unsafe_allow_html=True)

        # Lifestyle
        st.markdown('<div class="input-card"><div class="section-title">🏃 Lifestyle Factors</div>',
                    unsafe_allow_html=True)
        col8, col9 = st.columns(2)
        with col8:
            physical_activity = st.slider("Physical Activity (hrs/week)", 0.0, 20.0, 4.0, 0.5, disabled=not model_ok)
        with col9:
            social_hours = st.slider("Social Interaction (hrs/day)", 0.0, 10.0, 2.0, 0.5, disabled=not model_ok)
        st.markdown('</div>', unsafe_allow_html=True)

        submitted = st.form_submit_button("🔮 Analyze Burnout Risk", use_container_width=True, disabled=not model_ok)

    # Prediction
    if submitted and model_ok:
        # Prepare features
        gender_enc = 1 if gender == "Male" else 0
        features = np.array([[age, gender_enc, study_hours, sleep_hours, stress_level, anxiety_score, academic_pressure,
                              physical_activity, social_hours]])
        scaled = scaler.transform(features)
        pred = model.predict(scaled)[0]
        proba = model.predict_proba(scaled)[0]

        label_map = {0: "Low", 1: "Medium", 2: "High"}
        label = label_map[pred]
        score = round(proba[1] * 50 + proba[2] * 100, 1)

        # Result banner
        risk_class = f"risk-{label.lower()}"
        message = {"Low": "Balanced profile", "Medium": "Early warning signs", "High": "Critical — immediate action"}[
            label]
        st.markdown(f"""
        <div class="result-banner {risk_class}">
            <div>
                <div class="risk-badge">{label.upper()} RISK</div>
                <div style="color: #94A3B8; font-size:0.85rem;">{message}</div>
            </div>
            <div>
                <div class="risk-score">{score}%</div>
                <div style="color: #64748B; font-size:0.7rem;">Burnout Risk Score</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Charts
        st.markdown('<div class="section-title">📈 Analytics Dashboard</div>', unsafe_allow_html=True)

        # Gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            number={'suffix': "%", 'font': {'size': 32, 'color': "#4F46E5"}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': '#475569'},
                'bar': {'color': "#4F46E5", 'thickness': 0.3},
                'bgcolor': 'rgba(0,0,0,0)',
                'steps': [
                    {'range': [0, 35], 'color': 'rgba(16,185,129,0.1)'},
                    {'range': [35, 65], 'color': 'rgba(245,158,11,0.1)'},
                    {'range': [65, 100], 'color': 'rgba(239,68,68,0.1)'}
                ]
            }
        ))
        fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor='rgba(0,0,0,0)',
                                font_color='#94A3B8')

        # Probability bars
        fig_prob = go.Figure()
        colors = ["#10B981", "#F59E0B", "#EF4444"]
        labels = ["Low Risk", "Moderate Risk", "High Risk"]
        for lbl, col, p in zip(labels, colors, proba):
            fig_prob.add_trace(go.Bar(x=[p * 100], y=[lbl], orientation='h', marker_color=col, text=[f"{p * 100:.1f}%"],
                                      textposition='outside'))
        fig_prob.update_layout(height=200, margin=dict(l=10, r=40, t=20, b=10), paper_bgcolor='rgba(0,0,0,0)',
                               xaxis=dict(range=[0, 100], showgrid=False), yaxis=dict(showgrid=False))

        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_gauge, use_container_width=True, config={'displayModeBar': False})
        with col2:
            st.plotly_chart(fig_prob, use_container_width=True, config={'displayModeBar': False})

        # Recommendations
        recs = []
        if sleep_hours < 6: recs.append(("🌙", "Improve Sleep", "Target 7–9 hours nightly."))
        if stress_level >= 7: recs.append(("🧘", "Reduce Stress", "Practice box breathing daily."))
        if study_hours > 10: recs.append(("📖", "Study Strategy", "Use Pomodoro technique."))
        if physical_activity < 2: recs.append(("🏃", "Increase Exercise", "30 min walking 3x/week."))
        if social_hours < 1: recs.append(("💬", "Social Connection", "Schedule 1 hour daily."))
        if anxiety_score >= 7: recs.append(("🩺", "Professional Support", "Connect with a counsellor."))
        if academic_pressure >= 8: recs.append(("🎓", "Workload Balance", "Talk to academic advisor."))
        if not recs: recs.append(("⭐", "Keep Thriving", "All indicators healthy!"))

        st.markdown('<div class="section-title">✨ Personalized Recommendations</div>', unsafe_allow_html=True)
        rcols = st.columns(2)
        for i, (icon, title, desc) in enumerate(recs):
            with rcols[i % 2]:
                st.markdown(f"""
                <div class="rec-card">
                    <div class="rec-icon">{icon}</div>
                    <div>
                        <div class="rec-title">{title}</div>
                        <div class="rec-desc">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Developer card (new design)
    st.markdown("""
    <div class="dev-card">
        <div class="dev-header">
            <div class="dev-avatar">AA</div>
            <div class="dev-text">
                <h2>Akbar Ali</h2>
                <p>ML MODEL DEVELOPER & ENGINEER</p>
            </div>
        </div>
        <div class="dev-pills">
            <div class="pill">📋 <b>Project Mentor:</b> Engineer Aamir Jamil</div>
            <div class="pill">🎓 <b>Institute:</b> Corvit Systems Islamabad</div>
            <div class="pill">📘 <b>Program:</b> NAVTTC</div>
            <div class="pill">⚙ <b>Model:</b> Random Forest</div>
            <div class="pill">📊 <b>Dataset:</b> Kaggle</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Beautiful footer
    st.markdown("""
    <div class="footer">
        🧠 © 04/04/2026 Akbar Ali — AI-powered early burnout detection. ❤️ Not a substitute for professional medical advice.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
