import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kilograms (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height in meters (m):", min_value=0.0, format="%.2f")


if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is {bmi:.2f}")
        
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25.0 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        st.write(f"Based on your BMI, you are classified as: {category}")
        
        
        bmi_data = {"Category": ["Underweight", "Normal weight", "Overweight", "Obesity"],
                    "BMI Range": [18.5, 24.9, 29.9, 40]}
        df = pd.DataFrame(bmi_data)
        
        fig, ax = plt.subplots()
        ax.bar(df['Category'], df['BMI Range'], color=['blue', 'green', 'yellow', 'red'])
        ax.axhline(bmi, color='purple', linestyle='--', label=f"Your BMI: {bmi:.2f}")
        ax.legend()
        st.pyplot(fig)
    else:
        st.write("Please enter valid weight and height values.")
