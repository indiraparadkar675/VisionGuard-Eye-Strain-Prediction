import streamlit as st
import numpy as np
import joblib

model = joblib.load("eye_strain_model.pkl")

st.title("👁️ VisionGuard: Eye Strain Risk Predictor")

st.write("Predict your eye strain risk based on screen usage habits.")

# Inputs
screen_time = st.slider("Screen time per day (hours)", 1, 14, 6)
brightness = st.slider("Screen brightness (%)", 10, 100, 60)
breaks = st.slider("Breaks per hour", 0.0, 4.0, 1.0, step=0.25)
font_size = st.slider("Font size (px)", 10, 32, 14)
blue_filter = st.selectbox("Blue light filter ON?", ("No", "Yes"))
blue_filter = 1 if blue_filter == "Yes" else 0

# Predict button
if st.button("Predict Eye Strain Risk"):
    input_data = np.array([[screen_time, brightness, breaks, font_size, blue_filter]])
    prediction = model.predict(input_data)[0]

    st.subheader(f"Predicted Eye Strain Level: **{prediction}**")

    # Recommendations
    st.write("---")
    st.subheader("Suggestions")
    if prediction == "High":
        st.write("""
        - Reduce screen time
        - Use blue light filter
        - Increase font size
        - Follow 20-20-20 rule
        - Take frequent breaks
        """)
    elif prediction == "Medium":
        st.write("""
        - Take regular breaks
        - Adjust brightness to comfortable level
        - Consider slightly larger font size
        """)
    else:
        st.write("✅ Good habits, keep maintaining a healthy screen routine!")
