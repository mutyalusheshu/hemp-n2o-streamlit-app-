import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hemp GHG Estimator v2", layout="centered")

st.title("🌿 Hemp N₂O Emissions Estimator (v2.0)")

# User Inputs
soil = st.selectbox("Select Soil Type", ["Loamy", "Sandy", "Clayey"])
cover_crop = st.radio("Cover Crop Used?", ["Yes", "No"])
n_rate = st.slider("Nitrogen Fertilizer (lbs/ac)", 0, 225, 75)
rainfall = st.slider("Total Rainfall (mm)", 0, 300, 120)
temperature = st.slider("Average Temperature (°C)", 5, 35, 20)

# Simple empirical model
alpha = 0.5
beta1 = 0.015
beta2 = 0.002
beta3 = -0.1 if cover_crop == "Yes" else 0
n2o = alpha + beta1 * n_rate + beta2 * rainfall + beta3

# Show results
st.metric("Estimated N₂O Emissions", f"{round(n2o, 3)} kg/ha")

# 🔍 Visualization
st.subheader("📈 Emission Simulation Overview")

n_range = np.arange(0, 226, 25)
emissions = alpha + beta1 * n_range + beta2 * rainfall + beta3

fig, ax = plt.subplots()
ax.plot(n_range, emissions, marker='o', color='green')
ax.set_xlabel("Nitrogen Rate (lbs/ac)")
ax.set_ylabel("Estimated N₂O Emissions (kg/ha)")
ax.set_title("Simulated N₂O Emissions vs. Fertilizer Rate")
st.pyplot(fig)

# 🧾 Technical Note
st.markdown("---")
st.markdown("### 📑 Technical Note")
st.markdown("""
This tool uses a simplified empirical model to estimate N₂O emissions from hemp cropping systems. It is based on observed relationships between nitrogen rate, rainfall, and management practices from experimental field trials and relevant literature.

**Model Equation:**
N2O = α + β₁ * N_rate + β₂ * Rainfall + β₃ * CoverCrop
with coefficients:  
- α = 0.5  
- β₁ = 0.015  
- β₂ = 0.002  
- β₃ = -0.1 (if cover crop is present)

For detailed methodology, see the [Technical Document (PDF)](https://github.com/yourrepo/hemp-n2o-streamlit-app-v2/blob/main/technical_doc_v2.pdf).
""")

# 📚 References
st.markdown("### 📚 References")
st.markdown("""
1. Ludwig, J., et al. (2001). *Soil–air exchange of nitric oxide*. Biogeochemistry.  
2. Firestone, M., & Davidson, E. (1989). *Microbial basis of NO and N₂O production*.  
3. IPCC (2006). *Guidelines for GHG Inventories: AFOLU*.  
4. COMET-Farm, USDA. [https://cometfarm.nrel.colostate.edu](https://cometfarm.nrel.colostate.edu)
""")

