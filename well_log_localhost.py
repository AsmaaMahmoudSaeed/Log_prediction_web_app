import streamlit as st
import pandas as pd
import joblib
import pickle
import os

# Set page configuration
st.set_page_config(page_title="Well Log DT Prediction App", layout="wide")

# Title and description
st.title("Well Log DT Prediction App")
st.markdown("""
This application uses a Machine learning model to predict the DT (sonic log) value based on well log measurements (RHOB, GR, NPHI, PEF).
Enter the values for RHOB, GR, NPHI, and PEF below to get the predicted DT value.
""")

@st.cache_resource
def load_rf_model():
    try:
        # Path to the model file in the same directory
        output_path = 'cmodel.pkl'

        # Verify file exists and is not empty
        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            raise FileNotFoundError("Model file 'cmodel.pkl' not found or is empty. Ensure it is in the same directory as this script.")

        # Try loading with pickle
        try:
            with open(output_path, 'rb') as file:
                model = pickle.load(file)
            st.success("Model loaded successfully with pickle.")
            return model
        except (pickle.UnpicklingError, AttributeError) as e:
            # Fallback to joblib
            model = joblib.load(output_path)
            st.success("Model loaded successfully with joblib.")
            return model

    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load the model
regr = load_rf_model()
if regr is None:
    st.stop()

# User input for prediction
st.subheader("Predict DT")
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        rhob = st.number_input("RHOB (Density, g/cm³)", value=2.5, step=0.01)
        gr = st.number_input("GR (Gamma Ray, API)", value=50.0, step=0.1)
    with col2:
        nphi = st.number_input("NPHI (Neutron Porosity, v/v)", value=0.2, step=0.01)
        pef = st.number_input("PEF (Photoelectric Factor, b/e)", value=5.0, step=0.1)
    
    submitted = st.form_submit_button("Predict DT")
    
    if submitted:
        # Prepare input data
        input_data = pd.DataFrame([[rhob, gr, nphi, pef]], columns=['RHOB', 'GR', 'NPHI', 'PEF'])
        try:
            predicted_dt = regr.predict(input_data)[0]
            st.success(f"Predicted DT: {predicted_dt:.2f} µs/ft")
            
            # Display input and prediction in a table
            result_df = pd.DataFrame({
                'RHOB': [rhob],
                'GR': [gr],
                'NPHI': [nphi],
                'PEF': [pef],
                'Predicted DT': [predicted_dt]
            })
            st.table(result_df)
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")