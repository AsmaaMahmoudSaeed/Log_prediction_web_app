import streamlit as st
import pandas as pd
import joblib
import os
import gdown
import pickle
## to run -----> streamlit run your_script.py
# Set page configuration
# page_title="Well Log DT Prediction App": Sets the browser tab title to "Well Log DT Prediction App".
# layout="wide": Sets the page layout to "wide" mode, making the app use the full width of the browser window for a spacious UI.
st.set_page_config(page_title="Well Log DT Prediction App", layout="wide")

# Title and description
## Displays the main title of the app, "Well Log DT Prediction App", at the top of the web page in large, bold text.
st.title("Well Log DT Prediction App")
st.markdown("""
This application uses Machine Learning model to predict the DT (sonic log) value based on well log measurements (RHOB, GR, NPHI, PEF).
Enter the values for RHOB, GR, NPHI, and PEF below to get the predicted DT value.
""")


import streamlit as st
import pandas as pd
import joblib
import os
import gdown
import pickle

@st.cache_resource
def load_rf_model():
    try:
        # Correct Google Drive URL for direct download
        file_id = '1ySNUKWRAhq27DCdnt1t4-fM22XkIFeJ5'
        url = f'https://drive.google.com/uc?id={file_id}'
        output_path = 'cmodel.pkl'

        # Download the model file
        if not os.path.exists(output_path):
            st.write("Downloading model from Google Drive...")
            gdown.download(url, output_path, quiet=False)
        else:
            st.write("Using cached model file.")

        # Verify file exists and is not empty
        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            raise FileNotFoundError("Model file failed to download or is empty.")

        # Try loading with pickle
        try:
            with open(output_path, 'rb') as file:
                model = pickle.load(file)
            st.success("Model loaded successfully with pickle.")
            return model
        except (pickle.UnpicklingError, AttributeError) as e:
            #st.warning(f"Pickle failed: {e}. Trying joblib...")
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

