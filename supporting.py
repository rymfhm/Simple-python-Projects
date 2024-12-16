import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMI Calculator", page_icon=None, layout="centered")
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and determine your health category based on the result.")

st.sidebar.header("Settings")
units = st.sidebar.radio("Choose units:", ["Metric (cm, kg)", "Imperial (inches, pounds)"])

with st.form("bmi_form"):
    st.subheader("Enter Your Details")
    if units == "Metric (cm, kg)":
        height = st.number_input("Enter your height (in cm):", min_value=100, max_value=250, value=175)
        weight = st.number_input("Enter your weight (in kg):", min_value=30.0, max_value=200.0, value=70.0)
    else:
        height = st.number_input("Enter your height (in inches):", min_value=40.0, max_value=100.0, value=65.0)
        weight = st.number_input("Enter your weight (in pounds):", min_value=80.0, max_value=400.0, value=150.0)
    
    submit = st.form_submit_button("Calculate BMI")

def calculate_bmi(weight, height, units):
    if units == "Metric (cm, kg)":
        return weight / ((height / 100) ** 2)
    else:
        height_m = height * 0.0254
        weight_kg = weight * 0.453592
        return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if submit:
    bmi = calculate_bmi(weight, height, units)
    category = bmi_category(bmi)
    st.subheader("Your BMI Results:")
    st.success(f"Your BMI is {bmi:.2f} ({category})")
    st.progress(min(bmi / 40, 1.0))
    
    st.subheader("Health Advice:")
    if category == "Underweight":
        st.warning("You are underweight.")
    elif category == "Normal Weight":
        st.info("You are maintaining a healthy weight.")
    elif category == "Overweight":
        st.warning("You are slightly overweight.")
    else:
        st.error("You are in the obese range.")

st.subheader("BMI Categories:")
bmi_data = {
    "Category": ["Underweight", "Normal Weight", "Overweight", "Obese"],
    "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", "30+"]
}
df = pd.DataFrame(bmi_data)
st.table(df)
