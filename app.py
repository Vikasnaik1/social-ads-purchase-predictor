import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Purchase Predictor",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0f;
    font-family: 'DM Sans', sans-serif;
    color: #e8e4f0;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at 20% 20%, #1a0a2e 0%, #0a0a0f 50%, #0d0a1a 100%);
    min-height: 100vh;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stDecoration"] {
    display: none;
}

.main .block-container {
    max-width: 680px;
    padding: 3rem 2rem 4rem;
    margin: 0 auto;
}

@keyframes floatOrb {
    0%, 100% { transform: translateY(0px) translateX(0px) scale(1); opacity: 0.4; }
    33% { transform: translateY(-30px) translateX(15px) scale(1.05); opacity: 0.6; }
    66% { transform: translateY(15px) translateX(-10px) scale(0.95); opacity: 0.35; }
}

@keyframes scanline {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(100vh); }
}

@keyframes titleReveal {
    0% { opacity: 0; transform: translateY(30px) skewY(2deg); filter: blur(8px); }
    100% { opacity: 1; transform: translateY(0) skewY(0); filter: blur(0); }
}

@keyframes fadeSlideUp {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 20px rgba(139, 92, 246, 0.3), 0 0 60px rgba(139, 92, 246, 0.1); }
    50% { box-shadow: 0 0 30px rgba(139, 92, 246, 0.5), 0 0 80px rgba(139, 92, 246, 0.2); }
}

@keyframes shimmer {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}

@keyframes resultAppear {
    0% { opacity: 0; transform: scale(0.85) translateY(20px); filter: blur(4px); }
    60% { transform: scale(1.02) translateY(-4px); }
    100% { opacity: 1; transform: scale(1) translateY(0); filter: blur(0); }
}

@keyframes borderRotate {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    filter: blur(80px);
}

.orb-1 {
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(88, 28, 220, 0.35) 0%, transparent 70%);
    top: -100px;
    left: -150px;
    animation: floatOrb 12s ease-in-out infinite;
}

.orb-2 {
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(236, 72, 153, 0.2) 0%, transparent 70%);
    top: 60%;
    right: -100px;
    animation: floatOrb 16s ease-in-out infinite reverse;
}

.orb-3 {
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(6, 182, 212, 0.15) 0%, transparent 70%);
    bottom: 10%;
    left: 20%;
    animation: floatOrb 20s ease-in-out infinite;
    animation-delay: -5s;
}

.hero-section {
    text-align: center;
    padding: 2rem 0 3rem;
    animation: titleReveal 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    position: relative;
    z-index: 1;
}

.hero-badge {
    display: inline-block;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #a78bfa;
    background: rgba(139, 92, 246, 0.08);
    border: 1px solid rgba(139, 92, 246, 0.2);
    padding: 0.4rem 1.1rem;
    border-radius: 50px;
    margin-bottom: 1.5rem;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 6vw, 3.6rem);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #f8f4ff 0%, #c4b5fd 40%, #818cf8 70%, #38bdf8 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 6s linear infinite;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 300;
    color: rgba(200, 190, 230, 0.55);
    letter-spacing: 0.02em;
    max-width: 380px;
    margin: 0 auto;
    line-height: 1.7;
}

.card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 20px;
    padding: 2.2rem 2rem;
    margin-bottom: 1.2rem;
    backdrop-filter: blur(20px);
    position: relative;
    z-index: 1;
    animation: fadeSlideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
    transition: border-color 0.3s ease, background 0.3s ease;
}

.card:hover {
    border-color: rgba(139, 92, 246, 0.2);
    background: rgba(255, 255, 255, 0.045);
}

.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.2s; }
.card:nth-child(3) { animation-delay: 0.3s; }

.card-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(167, 139, 250, 0.7);
    margin-bottom: 0.5rem;
}

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #f0ebff;
    margin-bottom: 0.3rem;
}

.card-desc {
    font-size: 0.82rem;
    color: rgba(180, 170, 210, 0.5);
    line-height: 1.6;
    margin-bottom: 1.2rem;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.3), rgba(56, 189, 248, 0.2), transparent);
    margin: 2rem 0;
    position: relative;
    z-index: 1;
    animation: fadeSlideUp 1s ease both;
    animation-delay: 0.4s;
}

[data-testid="stSelectbox"] label,
[data-testid="stSlider"] label,
[data-testid="stNumberInput"] label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
    color: rgba(196, 181, 253, 0.7) !important;
    text-transform: uppercase !important;
}

[data-testid="stSelectbox"] > div > div {
    background: rgba(139, 92, 246, 0.05) !important;
    border: 1px solid rgba(139, 92, 246, 0.15) !important;
    border-radius: 12px !important;
    color: #e8e4f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: all 0.25s ease !important;
}

[data-testid="stSelectbox"] > div > div:hover {
    border-color: rgba(139, 92, 246, 0.4) !important;
    background: rgba(139, 92, 246, 0.08) !important;
}

[data-baseweb="slider"] {
    padding-top: 0.5rem !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] > div:nth-child(2) {
    background: rgba(139, 92, 246, 0.15) !important;
    height: 4px !important;
    border-radius: 4px !important;
}

[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background: linear-gradient(135deg, #8b5cf6, #818cf8) !important;
    border: 2px solid rgba(255,255,255,0.2) !important;
    box-shadow: 0 0 12px rgba(139, 92, 246, 0.6) !important;
    width: 18px !important;
    height: 18px !important;
}

[data-testid="stNumberInput"] input {
    background: rgba(139, 92, 246, 0.05) !important;
    border: 1px solid rgba(139, 92, 246, 0.15) !important;
    border-radius: 12px !important;
    color: #e8e4f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    transition: all 0.25s ease !important;
}

[data-testid="stNumberInput"] input:focus {
    border-color: rgba(139, 92, 246, 0.5) !important;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
}

[data-testid="stButton"] button {
    width: 100%;
    background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 50%, #5b21b6 100%) !important;
    color: #fff !important;
    border: 1px solid rgba(167, 139, 250, 0.3) !important;
    border-radius: 14px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    padding: 0.85rem 2rem !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    position: relative !important;
    overflow: hidden !important;
    animation: pulseGlow 3s ease-in-out infinite !important;
    margin-top: 0.5rem !important;
}

[data-testid="stButton"] button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 40px rgba(139, 92, 246, 0.5) !important;
    background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 50%, #6d28d9 100%) !important;
}

[data-testid="stButton"] button:active {
    transform: translateY(0) !important;
}

.result-card {
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-top: 1.5rem;
    position: relative;
    z-index: 1;
    overflow: hidden;
    animation: resultAppear 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.result-card-buy {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(6, 182, 212, 0.06) 100%);
    border: 1px solid rgba(16, 185, 129, 0.25);
}

.result-card-no-buy {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.08) 0%, rgba(236, 72, 153, 0.06) 100%);
    border: 1px solid rgba(239, 68, 68, 0.2);
}

.result-icon {
    font-size: 3rem;
    display: block;
    margin-bottom: 1rem;
    filter: drop-shadow(0 0 20px currentColor);
}

.result-headline {
    font-family: 'Syne', sans-serif;
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin-bottom: 0.6rem;
}

.result-headline-buy {
    background: linear-gradient(135deg, #10b981, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.result-headline-no-buy {
    background: linear-gradient(135deg, #f87171, #fb7185);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.result-sub {
    font-size: 0.88rem;
    font-weight: 300;
    letter-spacing: 0.03em;
    line-height: 1.6;
}

.result-sub-buy { color: rgba(110, 231, 183, 0.6); }
.result-sub-no-buy { color: rgba(252, 165, 165, 0.5); }

.result-card::before {
    content: '';
    position: absolute;
    inset: -2px;
    border-radius: 22px;
    padding: 2px;
    background: linear-gradient(135deg, transparent, rgba(255,255,255,0.05), transparent);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    pointer-events: none;
}

.stats-row {
    display: flex;
    gap: 0.8rem;
    margin-top: 1.5rem;
    position: relative;
    z-index: 1;
    animation: fadeSlideUp 1s ease both;
    animation-delay: 0.5s;
}

.stat-pill {
    flex: 1;
    background: rgba(255, 255, 255, 0.025);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 1rem 0.8rem;
    text-align: center;
}

.stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #c4b5fd;
    display: block;
}

.stat-label {
    font-size: 0.68rem;
    font-weight: 400;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: rgba(150, 140, 180, 0.45);
    display: block;
    margin-top: 0.2rem;
}

.footer-text {
    text-align: center;
    font-size: 0.72rem;
    color: rgba(140, 130, 170, 0.35);
    letter-spacing: 0.08em;
    margin-top: 3rem;
    position: relative;
    z-index: 1;
    animation: fadeSlideUp 1.2s ease both;
    animation-delay: 0.6s;
}

.footer-text span {
    color: rgba(139, 92, 246, 0.5);
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.3); border-radius: 4px; }

[data-testid="stMarkdownContainer"] p {
    color: inherit;
}
</style>

<div class="orb orb-1"></div>
<div class="orb orb-2"></div>
<div class="orb orb-3"></div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.markdown("""
<div class="hero-section">
    <div class="hero-badge">SVM · Binary Classification</div>
    <div class="hero-title">Purchase<br>Intelligence</div>
    <div class="hero-subtitle">Predict customer purchase likelihood using a trained Support Vector Machine model.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="card-label">Step 01</div>
    <div class="card-title">Demographic Profile</div>
    <div class="card-desc">Select the customer's gender to begin building the prediction profile.</div>
</div>
""", unsafe_allow_html=True)

gender_input = st.selectbox(
    "Gender",
    options=["Male", "Female"],
    index=0,
    label_visibility="visible"
)

st.markdown("""
<div class="card">
    <div class="card-label">Step 02</div>
    <div class="card-title">Age Signal</div>
    <div class="card-desc">Customer age is a strong behavioral indicator in this model.</div>
</div>
""", unsafe_allow_html=True)

age_input = st.slider(
    "Age",
    min_value=18,
    max_value=70,
    value=35,
    step=1,
    label_visibility="visible"
)

st.markdown("""
<div class="card">
    <div class="card-label">Step 03</div>
    <div class="card-title">Estimated Salary</div>
    <div class="card-desc">Annual estimated salary in base currency units.</div>
</div>
""", unsafe_allow_html=True)

salary_input = st.number_input(
    "Estimated Salary",
    min_value=10000,
    max_value=200000,
    value=50000,
    step=1000,
    label_visibility="visible"
)

st.markdown("""
<div class="stats-row">
    <div class="stat-pill">
        <span class="stat-value">SVM</span>
        <span class="stat-label">Algorithm</span>
    </div>
    <div class="stat-pill">
        <span class="stat-value">RBF</span>
        <span class="stat-label">Kernel</span>
    </div>
    <div class="stat-pill">
        <span class="stat-value">3</span>
        <span class="stat-label">Features</span>
    </div>
    <div class="stat-pill">
        <span class="stat-value">Binary</span>
        <span class="stat-label">Output</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

predict_clicked = st.button("Run Prediction")

if predict_clicked:
    gender_encoded = 1 if gender_input == "Male" else 0
    input_data = np.array([[gender_encoded, age_input, salary_input]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.markdown("""
        <div class="result-card result-card-buy">
            <span class="result-icon">◈</span>
            <div class="result-headline result-headline-buy">Will Purchase</div>
            <div class="result-sub result-sub-buy">
                This customer profile has a high propensity to convert.<br>
                Strong buying signals detected across all features.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="result-card result-card-no-buy">
            <span class="result-icon">◇</span>
            <div class="result-headline result-headline-no-buy">Will Not Purchase</div>
            <div class="result-sub result-sub-no-buy">
                This customer profile is unlikely to convert at this time.<br>
                Consider targeted engagement or re-evaluation criteria.
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer-text">
    Powered by <span>scikit-learn SVC</span> · Built with <span>Streamlit</span>
</div>
""", unsafe_allow_html=True)
