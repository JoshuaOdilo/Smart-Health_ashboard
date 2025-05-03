
import streamlit as st
import pandas as pd
from models.predictor import HealthPredictor
from models.user_auth import UserAuth
from utils.data_cleaning import clean_data
from reports.export_logic import export_csv
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = "data/sample_data.csv"
df = pd.read_csv(DATA_PATH)
df = clean_data(df)

auth = UserAuth()
predictor = HealthPredictor()
accuracy = predictor.train(df)

st.markdown("""
    <style>
    .main-title {
        font-size:40px;
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
    }
    .section-header {
        font-size:24px;
        color: #16a085;
        margin-top: 30px;
    }
    .sidebar .sidebar-content {
        background-color: #f7f7f7;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("🔐 User Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
login = st.sidebar.button("Login")

if login:
    if auth.login(username, password):
        st.success(f"Welcome, {username}!")
    else:
        st.error("Invalid credentials")

if auth.login(username, password):
    st.markdown('<div class="main-title">🧠 Smart Health Data Visualization System</div>', unsafe_allow_html=True)
    section = st.sidebar.selectbox("Navigate", ["📊 Dashboard", "📈 Visualizations", "🧮 Predict Outcome", "📤 Export Data", "📚 About"])

    if section == "📊 Dashboard":
        st.markdown('<div class="section-header">Overview</div>', unsafe_allow_html=True)
        st.write("### Health Data Sample")
        st.dataframe(df.head())

    elif section == "📈 Visualizations":
        st.markdown('<div class="section-header">Data Visualizations</div>', unsafe_allow_html=True)
        fig1 = px.histogram(df, x="age", title="Age Distribution")
        st.plotly_chart(fig1)
        fig2 = px.box(df, y="blood_pressure", title="Blood Pressure Spread")
        st.plotly_chart(fig2)
        st.write("### Correlation Heatmap")
        corr = df[['age', 'heart_rate', 'blood_pressure', 'cholesterol']].corr()
        fig3, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig3)

    elif section == "🧮 Predict Outcome":
        st.markdown('<div class="section-header">Health Outcome Predictor</div>', unsafe_allow_html=True)
        age = st.slider("Age", 0, 100, 30)
        hr = st.slider("Heart Rate", 40, 180, 70)
        bp = st.slider("Blood Pressure", 80, 200, 120)
        chol = st.slider("Cholesterol", 100, 300, 180)
        if st.button("Predict"):
            result = predictor.predict({"age": age, "heart_rate": hr, "blood_pressure": bp, "cholesterol": chol})
            st.success(f"Predicted Outcome: {result}")

    elif section == "📤 Export Data":
        st.markdown('<div class="section-header">Export Section</div>', unsafe_allow_html=True)
        st.download_button("Download Clean Data as CSV", export_csv(df), file_name="clean_health_data.csv")

    elif section == "📚 About":
        st.markdown('<div class="section-header">About This System</div>', unsafe_allow_html=True)
        st.write("""
            - 📅 Project: Smart Health Data Visualization
            - 👨‍💻 Built with: Python, Streamlit, Plotly, Scikit-learn
            - 📊 Features: Interactive graphs, predictive modeling, login simulation
        """)
