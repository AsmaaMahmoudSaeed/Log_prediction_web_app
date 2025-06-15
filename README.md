# Well Log DT Prediction Web App

A Streamlit-based web application that uses a Random Forest
model to predict **DT (sonic transit time)** from well log measurements
(RHOB, GR, NPHI, PEF) in the Oil & Gas industry. This tool enables
petroleum engineers and geoscientists to input well log data manually
and obtain DT predictions through an intuitive web interface.

The app is deployed online via **Streamlit Cloud** at:
<https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/>.
This code is based on <https://github.com/andymcdgeo/Petrophysics-Python-Series/blob/master/29%20-%20Random%20Forest%20for%20Regression%20-%20Prediction%20of%20Continuous%20Well%20Logs-Copy1.ipynb>
There is an Arabic explanation of the entire code on my YouTube channel via this link
<https://www.youtube.com/watch?v=Jo6HKazZyzU>

------------------------------------------------------------------------

## Table of Contents

-   [Project Overview](#project-overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Deployment](#deployment)
-   [Model Details](#model-details)
-   [File Structure](#file-structure)
-   [Dependencies](#dependencies)
-   [Troubleshooting](#troubleshooting)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

------------------------------------------------------------------------

## Project Overview

In the Oil & Gas industry, well log data provides critical insights into
subsurface formations. The **sonic transit time (DT)** is a key
measurement indicating rock properties and porosity, but it may be
missing or noisy in some datasets. This web application uses a
**Random Forest** model to predict DT values based on well
log measurements: - **RHOB**: Density (g/cm³) - **GR**: Gamma Ray
(API) - **NPHI**: Neutron Porosity (v/v) - **PEF**: Photoelectric Factor
(b/e)

Built with **Streamlit**, the app offers a user-friendly interface for
manual input of well log data and displays predicted DT values in a
table.

------------------------------------------------------------------------

## Features

-   **DT Prediction**: Predict sonic transit time (DT) using RHOB, GR,
    NPHI, and PEF inputs.
-   **User-Friendly Interface**: Streamlit UI with input forms and
    tabulated results.
-   **Model Caching**: Efficient model loading with Streamlit's
    `@st.cache_resource`.
-   **Online Access**: Deployed on Streamlit Cloud for global
    accessibility.
------------------------------------------------------------------------

## Installation

To run the application locally, follow these steps:

1.  **Clone the Repository**:

    ``` bash
    git clone https://github.com/AsmaaMahmoudSaeed/Log_prediction_web_app2.git
    cd Log_prediction_web_app2
    ```

2.  **Create a Virtual Environment** (recommended):

    ``` bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**: Install the required Python packages
    listed in `requirements.txt`:

    ``` bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` is missing, install the following:

    ``` bash
    pip install streamlit pandas numpy scikit-learn joblib gdown
    ```

4.  **Ensure Model Access**: The pre-trained Random Forest model
    (`cmodel.pkl`) is downloaded from Google Drive (file ID:
    `1ySNUKWRAhq27DCdnt1t4-fM22XkIFeJ5`) during execution. Ensure
    internet access and Google Drive permissions are available.
    Alternatively, manually download `cmodel.pkl` and place it in the
    project directory.

5.  **Run the App**: Start the Streamlit server:

    ``` bash
    streamlit run log_prediction_app.py
    ```

    Open your browser  to access the app.

------------------------------------------------------------------------

## Usage

1.  **Access Online**: Visit the deployed app:
    <https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/>.

2.  **Local Usage**:

    -   Run `streamlit run app.py` and navigate to
        `http://localhost:8501`.
    -   On the app's interface:
        -   Enter values for **RHOB**, **GR**, **NPHI**, and **PEF** in
            the input form.
        -   Click **Predict DT** to generate the predicted DT value.
        -   View the result in a table showing input values and the
            predicted DT (in µs/ft).

3.  **Example Input**:

    -   RHOB: 2.34 g/cm³
    -   GR: 54.8 API
    -   NPHI: 0.44 v/v
    -   PEF: 5.0 b/e
    -   Expected Output: Predicted DT (e.g., 95.7 µs/ft) displayed with
        a table.


------------------------------------------------------------------------

## Deployment

The app is hosted on **Streamlit Cloud** for online access: - **URL**:
<https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/> -
**Setup**: - The repository (`app.py`, `requirements.txt`) is linked to
Streamlit Cloud. - The model (`cmodel.pkl`) is downloaded from Google
Drive at runtime. - Streamlit Cloud manages dependencies and hosting.

To deploy your own version: 1. Fork or clone the repository. 2. Create a
Streamlit Cloud account and link your GitHub repository. 3. Configure
the app settings (e.g., Python version (3.12.9), `requirements.txt`). 4. Deploy
and access the public URL provided by Streamlit Cloud.

------------------------------------------------------------------------

## Model Details

-   **Algorithm**: Random Forest Regressor (from `scikit-learn`).
-   **Features**:
    -   RHOB: Density (g/cm³)
    -   GR: Gamma Ray (API)
    -   NPHI: Neutron Porosity (v/v)
    -   PEF: Photoelectric Factor (b/e)
-   **Target**: Sonic Transit Time (DT, µs/ft).
-   **Training Data**: part of volve_wells.csv file.
-   **Preprocessing**: Features are likely scaled (e.g., using
    `StandardScaler`) during training.

*
------------------------------------------------------------------------

## File Structure

    Log_prediction_web_app2/
    ├── log_prediction_app.py               # Main Streamlit application script
    ├── requirements.txt                    # Python dependencies
    ├── cmodel.pkl                          # Pre-trained Random Forest model (downloaded at runtime)
    ├── README.md                           # Project documentation (this file)
    └── volve_wells.csv                     # Optional: Directory for sample LAS files or test data

-   **`log_prediction_app.py  `**: Contains the Streamlit app logic for UI, model
    loading, and prediction.
-   **`cmodel.pkl`**: Downloaded from Google Drive during execution.
-   **`requirements.txt`**: Lists dependencies (create if missing).
-   **`volve_wells.csv `**: Dataset.

------------------------------------------------------------------------

## Dependencies

-   Python 3.12.9
-   Libraries (install via `pip`):
    -   `streamlit`: Web app framework
    -   `pandas`: Data manipulation
    -   `numpy`: Numerical computations
    -   `scikit-learn`: Machine learning
    -   `joblib`: Model loading
    -   `gdown`: Google Drive downloads

Create a `requirements.txt` file with:

    streamlit==1.32.0
    pandas==2.2.2
    numpy==1.26.4
    joblib==1.4.2
    gdown==5.2.0
    scikit-learn==1.7.0

------------------------------------------------------------------------

## Troubleshooting

-   **Google Drive Download Failure**:
    -   Verify the file ID (`1ySNUKWRAhq27DCdnt1t4-fM22XkIFeJ5`) is
        accessible.
    -   Manually download `cmodel.pkl` and place it in the project
        directory.
    -   Update the Google Drive link if the file is moved.
        ```
-   **Streamlit Cloud Issues**:
    -   Ensure `requirements.txt` includes all dependencies.
    -   Check Streamlit Cloud logs for errors (e.g., missing packages).
    -   Verify Python version compatibility (e.g., 3.8).

------------------------------------------------------------------------

## License

This project is licensed under the MIT License. See the
[LICENSE](LICENSE) file for details (create if missing).

------------------------------------------------------------------------

For questions, feedback, or collaboration, open a GitHub issue or
contact me directly.

------------------------------------------------------------------------

**Acknowledgments**: - Built with open-source tools: Streamlit,
scikit-learn, pandas. - Inspired by the need for efficient well log
analysis in the Oil & Gas industry. - Supported by the Canadian Well
Logging Society's LAS file format.
