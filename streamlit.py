import streamlit as st

def calculate_fold_change(experimental_value, control_value):
    # Avoid division by zero
    if control_value == 0:
        st.warning("Control value cannot be zero.")
        return None
    return experimental_value / control_value


st.title("Fold Change Calculator for Flow Cytometry")

experimental_value = st.number_input("Experimental Value (Mean Fluorescence Intensity):", min_value=0.0, step=0.1)
control_value = st.number_input("Control Value (Mean Fluorescence Intensity):", min_value=0.0, step=0.1)

if st.button("Calculate Fold Change"):
    fold_change = calculate_fold_change(experimental_value, control_value)
    if fold_change is not None:
        st.success(f"Fold Change: {fold_change:.2f}")
