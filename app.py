import streamlit as st
import numpy as np

st.set_page_config(page_title="Hemp GHG Stimulator", layout="centered")

st.title(" N₂O Emissions Stimulator")

# Input widgets
soil = st.selectbox("Select Soil Type", ["Loamy", "Sandy", "Clayey"])
cover_crop = st.radio("Cover Crop Used?", ["Yes", "No"])
n_rate = st.slider("Nitrogen Fertilizer (lbs/ac)", 0, 225, 75)
rainfall = st.slider("Total Rainfall (mm)", 0, 300, 120)
WPFS = st.slider ("WFPS (%)", 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
temperature = st.slider("Average Temperature (°C)", 5, 35, 20)

# Simple model
alpha = 0.5
beta1 = 0.015
beta2 = 0.002
beta3 = -0.1 if cover_crop == "Yes" else 0

n2o = alpha + beta1 * n_rate + beta2 * WFPS * rainfall + beta3

st.metric("Estimated N₂O Emissions", f"{round(n2o, 3)} kg/ha")

st.markdown("This tool estimates emissions based on simplified field model assumptions. For advanced modeling, integrate DSSAT or trained ML models.")
