import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(
    page_title="Analytics Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        background-color: #050505;
        color: #ffffff;
    }

    .main {
        background: radial-gradient(circle at 50% -20%, #1a1a2e, #050505);
    }

    .header-container {
        padding: 4rem 0;
        text-align: center;
    }

    .main-title {
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(to right, #ffffff, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 50px;
        backdrop-filter: blur(20px);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }

    .stButton>button {
        width: 100%;
        height: 4rem;
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        color: #000;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.2rem;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(79, 172, 254, 0.4);
        color: #000;
    }

    .result-display {
        margin-top: 30px;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_prediction_engine():

    model_path = "model.pkl"

    if not os.path.exists(model_path):
        st.error("model.pkl file not found")
        return None

    try:
        model = joblib.load(model_path)
        return model

    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None

engine = load_prediction_engine()

st.markdown("""
<div class="header-container">
    <h1 class="main-title">Intelligence Hub</h1>
    <p style="color: #94a3b8; font-size: 1.2rem; letter-spacing: 2px;">
        SECURE ANALYTICS TERMINAL
    </p>
</div>
""", unsafe_allow_html=True)

if engine is None:
    st.stop()

col1, col2, col3 = st.columns([1, 1.8, 1])

with col2:

    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)

    selection_gender = st.selectbox(
        "Gender Classification",
        options=["Male", "Female"]
    )

    input_age = st.slider(
        "User Age",
        18,
        65,
        30
    )

    input_salary = st.number_input(
        "Estimated Annual Salary",
        min_value=10000,
        max_value=250000,
        value=50000
    )

    val_gender = 1 if selection_gender == "Male" else 0

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("EXECUTE ANALYSIS"):

        try:

            data_vector = np.array([
                [val_gender, input_age, input_salary]
            ])

            prediction = engine.predict(data_vector)

            st.markdown(
                '<div class="result-display">',
                unsafe_allow_html=True
            )

            if prediction[0] == 1:

                st.markdown("""
                <h2 style="color: #22c55e;">
                    POSITIVE PREDICTION
                </h2>

                <p style="color: #86efac;">
                    High engagement probability identified.
                </p>
                """, unsafe_allow_html=True)

            else:

                st.markdown("""
                <h2 style="color: #ef4444;">
                    NEGATIVE PREDICTION
                </h2>

                <p style="color: #fca5a5;">
                    Low engagement probability identified.
                </p>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:

            st.error(f"Prediction Error: {e}")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align:center;
    margin-top:6rem;
    color:#334155;
    font-size:0.8rem;
    font-weight:600;
    letter-spacing:1px;
">
    V2.0 SYSTEM DEPLOYMENT | SCIKIT-LEARN 1.3.0
</div>
""", unsafe_allow_html=True)
