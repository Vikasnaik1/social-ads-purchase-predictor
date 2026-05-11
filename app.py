import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Predictive Analytics Pro",
    page_icon="None",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0e1117;
    }

    .main {
        background: linear-gradient(135deg, #0e1117 0%, #161b22 100%);
    }

    .stApp {
        background: transparent;
    }

    .header-container {
        padding: 3rem 1rem;
        text-align: center;
        animation: fadeInDown 1s ease-out;
    }

    .main-title {
        color: #ffffff;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: -0.05rem;
        margin-bottom: 0.5rem;
    }

    .sub-title {
        color: #8b949e;
        font-size: 1.2rem;
        font-weight: 300;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2.5rem;
        margin-top: 2rem;
        animation: fadeInUp 1.2s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #238636 0%, #2ea043 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.05rem;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(46, 160, 67, 0.4);
        background: linear-gradient(90deg, #2ea043 0%, #3fb950 100%);
    }

    .result-container {
        margin-top: 2rem;
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
        animation: zoomIn 0.5s ease-out;
    }

    @keyframes zoomIn {
        0% { opacity: 0; scale: 0.95; }
        100% { opacity: 1; scale: 1; }
    }

    .prediction-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def load_model():
    with open('model_v2 (2) .pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Intelligence Engine</h1>
        <p class="sub-title">Advanced Support Vector Classification for Strategic Insights</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    gender = st.selectbox("Gender Selection", options=["Male", "Female"])
    age = st.slider("Target Age", min_value=18, max_value=65, value=30)
    salary = st.number_input("Estimated Annual Salary", min_value=10000, max_value=200000, value=50000, step=1000)
    
    gender_numeric = 1 if gender == "Male" else 0
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Generate Prediction"):
        input_data = np.array([[gender_numeric, age, salary]])
        prediction = model.predict(input_data)
        
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        if prediction[0] == 1:
            st.markdown('<p style="color: #3fb950; font-size: 1.2rem;">Classification Result</p>', unsafe_allow_html=True)
            st.markdown('<h2 class="prediction-value" style="color: #3fb950;">POSITIVE</h2>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color: #f85149; font-size: 1.2rem;">Classification Result</p>', unsafe_allow_html=True)
            st.markdown('<h2 class="prediction-value" style="color: #f85149;">NEGATIVE</h2>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; margin-top: 5rem; color: #484f58; font-size: 0.8rem;">
        Engineered with scikit-learn 1.3.0 | Deployment Grade v2.1.0
    </div>
""", unsafe_allow_html=True)
