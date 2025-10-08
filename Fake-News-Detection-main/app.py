import streamlit as st
import joblib

# 🧩 Page setup
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🎨 Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        font-family: 'Poppins', sans-serif;
    }
    .main-title {
        text-align: center;
        color: #2E8B57;
        font-size: 50px;
        font-weight: 800;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #555;
        margin-bottom: 30px;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #2E8B57;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #2E8B57;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        height: 3em;
        width: 50%;
        display: block;
        margin: 0 auto;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .result-box {
        text-align: center;
        padding: 40px;
        border-radius: 15px;
        font-weight: bold;
        font-size: 36px;
        margin-top: 40px;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.1);
    }
    .real {
        background-color: #e8f5e9;
        color: #2E7D32;
        border: 3px solid #2E7D32;
    }
    .fake {
        background-color: #ffebee;
        color: #C62828;
        border: 3px solid #C62828;
    }
    footer {
        text-align: center;
        color: gray;
        font-size: 14px;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# 📰 Header
st.markdown("<h1 class='main-title'>📰 Fake News Detector</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Analyze any news article below to detect if it’s <b>Real</b> or <b>Fake</b>.</p>", unsafe_allow_html=True)

# 🧠 Load Model and Vectorizer
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

# 📝 Input
inputn = st.text_area("📝 Paste News Article Here:", "")

# 🚀 Button and Prediction
if st.button("Check News"):
    if inputn.strip():
        transform_input = vectorizer.transform([inputn])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.markdown(
                "<div class='result-box real'>✅ REAL NEWS</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-box fake'>🚨 FAKE NEWS</div>",
                unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter some text to analyze.")

# 👣 Footer
st.markdown("""
<footer>
    Developed by <b>Umesh Jadhav</b> 🧠 | Powered by Machine Learning & Streamlit
</footer>
""", unsafe_allow_html=True)
