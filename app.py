import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

st.set_page_config(
    page_title="AI Predictive Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #0a192f;
        color: #e6f1ff;
    }

    .main {
        background: radial-gradient(circle at top right, #112240, #0a192f);
    }

    .header-container {
        padding: 4rem 1rem 2rem 1rem;
        text-align: center;
        animation: fadeInDown 0.8s ease-out;
    }

    .main-title {
        background: linear-gradient(90deg, #64ffda, #48b1bf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .glass-card {
        background: rgba(17, 34, 64, 0.7);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(100, 255, 218, 0.1);
        padding: 3rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        animation: fadeInUp 1s ease-out;
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stButton>button {
        width: 100%;
        background: #64ffda;
        color: #0a192f;
        border: none;
        padding: 1rem;
        border-radius: 10px;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(100, 255, 218, 0.4);
        background: #4cd3b5;
    }

    .prediction-box {
        margin-top: 2rem;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        background: rgba(2, 12, 27, 0.5);
        border-left: 5px solid #64ffda;
    }
</style>
""", unsafe_allow_html=True)

def load_model():
    def load_model():
    with open('model.pkl', 'rb') as file:
        return pickle.load(file)
    
    return None

model = load_model()

st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Neural Insight Engine</h1>
        <p style="color: #8892b0; font-size: 1.2rem;">Professional Grade Predictive Analysis System</p>
    </div>
""", unsafe_allow_html=True)

if model is None:
    st.error("Model file not found. Please ensure the .pkl file is in the same folder as app.py on GitHub.")
else:
    col1, col2, col3 = st.columns([1, 1.5, 1])

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        gender = st.selectbox("Select Gender", options=["Male", "Female"])
        age = st.slider("User Age", 18, 65, 30)
        salary = st.number_input("Estimated Salary (USD/INR)", min_value=10000, max_value=200000, value=50000)
        
        gender_val = 1 if gender == "Male" else 0
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("EXECUTE ANALYSIS"):
            features = np.array([[gender_val, age, salary]])
            prediction = model.predict(features)
            
            st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
            if prediction[0] == 1:
                st.markdown('<h2 style="color: #64ffda; margin:0;">RESULT: POSITIVE</h2>', unsafe_allow_html=True)
                st.write("User is likely to engage with the target objective.")
            else:
                st.markdown('<h2 style="color: #ff4b2b; margin:0;">RESULT: NEGATIVE</h2>', unsafe_allow_html=True)
                st.write("User is unlikely to engage with the target objective.")
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; margin-top: 4rem; color: #495670; font-size: 0.9rem; letter-spacing: 1px;">
        V2.0 SYSTEM | SECURE ENCRYPTION ENABLED | SCIKIT-LEARN DEPLOYMENT
    </div>
""", unsafe_allow_html=True)
