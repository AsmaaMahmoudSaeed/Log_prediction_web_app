import streamlit as st
import pandas as pd
import joblib
import os
## to run -----> streamlit run your_script.py
# Set page configuration
# page_title="Well Log DT Prediction App": Sets the browser tab title to "Well Log DT Prediction App".
# layout="wide": Sets the page layout to "wide" mode, making the app use the full width of the browser window for a spacious UI.
st.set_page_config(page_title="Well Log DT Prediction App", layout="wide")

# Title and description
## Displays the main title of the app, "Well Log DT Prediction App", at the top of the web page in large, bold text.
st.title("Well Log DT Prediction App")
st.markdown("""
This application uses a pre-trained Random Forest model to predict the DT (sonic log) value based on well log measurements (RHOB, GR, NPHI, PEF).
Enter the values for RHOB, GR, NPHI, and PEF below to get the predicted DT value.
""")

# File path for the saved model
MODEL_PATH = "model.pkl"

# Load the model
def load_model():
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            return model
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None
    else:
        st.error(f"Model file '{MODEL_PATH}' not found in the current directory.")
        return None

# Load the model
regr = load_model()
if regr is None:
    # Stops the Streamlit app execution using st.stop() if the model could not be loaded, preventing the app from proceeding without a valid model.
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

