import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page Configuration
st.set_page_config(page_title="Poll Insights Pro", layout="wide")

# 1. Load Data Function (Smart Path)
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, 'data', 'poll_data.csv')
    
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return None

# Title
st.title("📊 Advanced Poll Results Visualizer")
st.markdown("Industry-ready dashboard for survey analysis.")

df = load_data()

if df is not None:
    # --- KPIs ---
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Responses", len(df))
    c2.metric("Top Choice", df['Language'].value_counts().idxmax())
    c3.metric("Avg Satisfaction", f"{round(df['Satisfaction'].mean(), 2)}/5")

    # --- Charts ---
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.pie(df, names='Language', title="Popularity %", hole=0.3)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.histogram(df, x='Region', color='Language', barmode='group', title="Regional Trends")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("User Satisfaction Analysis")
    fig3 = px.box(df, x='User_Type', y='Satisfaction', color='User_Type')
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.error("❌ 'data/poll_data.csv' nahi mili!")
    st.info("Pehle 'python data_generator.py' chalayein taaki data generate ho sake.")