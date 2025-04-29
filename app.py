import streamlit as st
import numpy as np

st.set_page_config(page_title="Hemp GHG Estimator", layout="centered")

st.title("🌿 Hemp N₂O Emissions Estimator")

# Input widgets
soil = st.selectbox("Select Soil Type", ["Loamy", "Sandy", "Clayey"])
cover_crop = st.radio("Cover Crop Used?", ["Yes", "No"])
n_rate = st.slider("Nitrogen Fertilizer (lbs/ac)", 0, 225, 75)
rainfall = st.slider("Total Rainfall (mm)", 0, 300, 120)
temperature = st.slider("Average Temperature (°C)", 5, 35, 20)

# Simple model
alpha = 0.5
beta1 = 0.015
beta2 = 0.002
beta3 = -0.1 if cover_crop == "Yes" else 0

n2o = alpha + beta1 * n_rate + beta2 * rainfall + beta3

st.metric("Estimated N₂O Emissions", f"{round(n2o, 3)} kg/ha")

st.markdown("This tool estimates emissions based on simplified field model assumptions. For advanced modeling, integrate DSSAT or trained ML models.")
