# Well Log DT Prediction Web App

A Streamlit-based web application that uses a pre-trained Random Forest model to predict **DT (sonic transit time)** from well log measurements (RHOB, GR, NPHI, PEF) in the Oil & Gas industry. This tool enables petroleum engineers and geoscientists to input well log data manually and obtain DT predictions through an intuitive web interface, supporting reservoir characterization and exploration.

The app is deployed online via **Streamlit Cloud** at: [https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/](https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/).

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Model Details](#model-details)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview
In the Oil & Gas industry, well log data provides critical insights into subsurface formations. The **sonic transit time (DT)** is a key measurement indicating rock properties and porosity, but it may be missing or noisy in some datasets. This web application uses a pre-trained **Random Forest** model to predict DT values based on well log measurements:
- **RHOB**: Density (g/cm³)
- **GR**: Gamma Ray (API)
- **NPHI**: Neutron Porosity (v/v)
- **PEF**: Photoelectric Factor (b/e)

Built with **Streamlit**, the app offers a user-friendly interface for manual input of well log data and displays predicted DT values in a table. It is designed to work with data similar to **Log ASCII Standard (LAS)** files, commonly used in the industry, and can be extended to support LAS file uploads or clustering analysis (e.g., K-Means or DBSCAN).

---

## Features
- **DT Prediction**: Predict sonic transit time (DT) using RHOB, GR, NPHI, and PEF inputs.
- **User-Friendly Interface**: Streamlit UI with input forms and tabulated results..
- **Online Access**: Deployed on Streamlit Cloud for global accessibility.

---

## Installation
To run the application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AsmaaMahmoudSaeed/Log_prediction_web_app2.git
   cd Log_prediction_web_app2
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install the following:
   ```bash
   pip install streamlit pandas numpy scikit-learn joblib gdown
   ```

4. **Ensure Model Access**:
   The pre-trained Random Forest model (`cmodel.pkl`) is downloaded from Google Drive (file ID: `1ySNUKWRAhq27DCdnt1t4-fM22XkIFeJ5`) during execution. Ensure internet access and Google Drive permissions are available. Alternatively, manually download `cmodel.pkl` and place it in the project directory.

5. **Run the App**:
   Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
   Open your browser at `http://localhost:8501` to access the app.

---

## Usage
1. **Access Online**:
   Visit the deployed app: [https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/](https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/).

2. **Local Usage**:
   - Run `streamlit run app.py` and navigate to `http://localhost:8501`.
   - On the app’s interface:
     - Enter values for **RHOB**, **GR**, **NPHI**, and **PEF** in the input form.
     - Click **Predict DT** to generate the predicted DT value.
     - View the result in a table showing input values and the predicted DT (in µs/ft).

3. **Example Input**:
   - RHOB: 2.34 g/cm³
   - GR: 54.8 API
   - NPHI: 0.44 v/v
   - PEF: 5.0 b/e
   - Expected Output: Predicted DT (e.g., 95.7 µs/ft) displayed with a table.

4. **Extending the App**:
   - Add LAS file upload support using `lasio` (e.g., for files like `15-9-19_SR_COMP.LAS`).
   - Integrate clustering (e.g., K-Means or DBSCAN) to analyze rock types.
   - Include visualizations like log plots or pairplots (as in your previous work).

---

## Deployment
The app is hosted on **Streamlit Cloud** for online access:
- **URL**: [https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/](https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/)
- **Setup**:
  - The repository (`app.py`, `requirements.txt`) is linked to Streamlit Cloud.
  - The model (`cmodel.pkl`) is downloaded from Google Drive at runtime.
  - Streamlit Cloud manages dependencies and hosting.

To deploy your own version:
1. Fork or clone the repository.
2. Create a Streamlit Cloud account and link your GitHub repository.
3. Configure the app settings (e.g., Python version, `requirements.txt`).
4. Deploy and access the public URL provided by Streamlit Cloud.

---

## Model Details
- **Algorithm**: Random Forest Regressor (from `scikit-learn`).
- **Features**:
  - RHOB: Density (g/cm³)
  - GR: Gamma Ray (API)
  - NPHI: Neutron Porosity (v/v)
  - PEF: Photoelectric Factor (b/e)
- **Target**: Sonic Transit Time (DT, µs/ft).
- **Training Data**: part of volve_wells.csv file.
- **Serialization**: Model saved as `cmodel.pkl` using `pickle` .
- **Preprocessing**: Features are likely scaled (e.g., using `StandardScaler`) during training.


---

## File Structure
```
Log_prediction_web_app2/
├── app.py                # Main Streamlit application script
├── requirements.txt      # Python dependencies
├── cmodel.pkl            # Pre-trained Random Forest model (downloaded at runtime)
├── README.md             # Project documentation (this file)
└── data/                 # Optional: Directory for sample LAS files or test data
```

- **`app.py`**: Contains the Streamlit app logic for UI, model loading, and prediction.
- **`cmodel.pkl`**: Downloaded from Google Drive during execution.
- **`requirements.txt`**: Lists dependencies (create if missing).
- **`data/`**: Placeholder for LAS files (not included).

---

## Dependencies
- Python 3.8 or later
- Libraries (install via `pip`):
  - `streamlit`: Web app framework
  - `pandas`: Data manipulation
  - `numpy`: Numerical computations
  - `scikit-learn`: Machine learning
  - `joblib`: Model loading
  - `gdown`: Google Drive downloads

Create a `requirements.txt` file with:
```
streamlit==1.32.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.0
joblib==1.4.2
gdown==5.2.0
```

---

## Troubleshooting
- **UnpicklingError: STACK_GLOBAL requires str**:
  - **Cause**: Mismatch in Python or `scikit-learn` versions between training and runtime environments.
  - **Fix**:
    - Use the same Python (e.g., 3.8) and `scikit-learn` (e.g., 1.5.0) versions as the training environment.
    - Load the model with `joblib`:
      ```python
      import joblib
      model = joblib.load('cmodel.pkl')
      ```
    - Retrain the model:
      ```python
      from sklearn.ensemble import RandomForestRegressor
      model = RandomForestRegressor()
      model.fit(X_train, y_train)  # Your data
      joblib.dump(model, 'cmodel.pkl')
      ```

- **Google Drive Download Failure**:
  - Verify the file ID (`1ySNUKWRAhq27DCdnt1t4-fM22XkIFeJ5`) is accessible.
  - Manually download `cmodel.pkl` and place it in the project directory.
  - Update the Google Drive link if the file is moved.

- **Missing PEF in LAS Files**:
  - Impute PEF (e.g., mean value) or retrain the model without PEF:
    ```python
    model.fit(X_train[['RHOB', 'GR', 'NPHI']], y_train)  # Exclude PEF
    joblib.dump(model, 'cmodel.pkl')
    ```

- **Streamlit Cloud Issues**:
  - Ensure `requirements.txt` includes all dependencies.
  - Check Streamlit Cloud logs for errors (e.g., missing packages).
  - Verify Python version compatibility (e.g., 3.8).

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Report issues or suggest features via the [Issues](https://github.com/AsmaaMahmoudSaeed/Log_prediction_web_app2/issues) tab.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (create if missing).

---

## Contact
- **LinkedIn**: [[Add your LinkedIn profile if desired](https://www.linkedin.com/in/asmaa-m-491750194/)]

For questions, feedback, or collaboration, open a GitHub issue or contact me directly.

---

**Acknowledgments**:
- Built with open-source tools: Streamlit, scikit-learn, pandas.
- Inspired by the need for efficient well log analysis in the Oil & Gas industry.
- Supported by the Canadian Well Logging Society’s LAS file format.
