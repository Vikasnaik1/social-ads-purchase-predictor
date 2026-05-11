import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

st.set_page_config(
    page_title="Data Intelligence Terminal",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0f172a;
        color: #f8fafc;
    }

    .main {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    }

    .header-section {
        padding: 4rem 0 2rem 0;
        text-align: center;
        animation: fadeIn 1.2s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .title-text {
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }

    .subtitle-text {
        color: #94a3b8;
        font-size: 1.1rem;
        font-weight: 300;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-top: 10px;
    }

    .input-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 3rem;
        backdrop-filter: blur(12px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
    }

    .stButton>button {
        width: 100%;
        height: 3.5rem;
        background: #38bdf8;
        color: #0f172a;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .stButton>button:hover {
        background: #0ea5e9;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(56, 189, 248, 0.3);
    }

    .prediction-output {
        margin-top: 2.5rem;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
</style>
""", unsafe_allow_html=True)

def initialize_model():
    base_path = os.path.dirname(__file__) if '__file__' in locals() else os.getcwd()
    candidate_files = [f for f in os.listdir(base_path) if f.endswith('.pkl')]
    
    if candidate_files:
        try:
            with open(os.path.join(base_path, candidate_files[0]), 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
    return None

model_instance = initialize_model()

st.markdown("""
    <div class="header-section">
        <h1 class="title-text">Predictive Analysis System</h1>
        <p class="subtitle-text">High Performance Vector Classification</p>
    </div>
""", unsafe_allow_html=True)

if model_instance is None:
    st.error("Model Error: The system could not locate a valid .pkl file in the repository root directory.")
else:
    left, center, right = st.columns([1, 1.5, 1])

    with center:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        
        user_gender = st.radio("Select Gender Profile", options=["Male", "Female"], horizontal=True)
        user_age = st.slider("Subject Age", 18, 65, 30)
        user_salary = st.number_input("Subject Annual Salary", 10000, 200000, 50000, step=500)
        
        encoded_gender = 1 if user_gender == "Male" else 0
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("RUN DIAGNOSTIC"):
            input_features = np.array([[encoded_gender, user_age, user_salary]])
            prediction_result = model_instance.predict(input_features)
            
            st.markdown('<div class="prediction-output">', unsafe_allow_html=True)
            if prediction_result[0] == 1:
                st.markdown('<h2 style="color: #4ade80; margin:0;">CLASSIFICATION: POSITIVE</h2>', unsafe_allow_html=True)
                st.markdown('<p style="color: #94a3b8;">High engagement probability detected.</p>', unsafe_allow_html=True)
            else:
                st.markdown('<h2 style="color: #f87171; margin:0;">CLASSIFICATION: NEGATIVE</h2>', unsafe_allow_html=True)
                st.markdown('<p style="color: #94a3b8;">Low engagement probability detected.</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; margin-top: 6rem; color: #475569; font-size: 0.75rem; letter-spacing: 2px;">
        ENCRYPTED DEPLOYMENT | SYSTEM READY | V2.0.1
    </div>
""", unsafe_allow_html=True)
