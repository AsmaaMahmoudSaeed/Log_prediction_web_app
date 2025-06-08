Well Log DT Prediction Web App
A Streamlit-based web application that uses machine learning to predict DT (sonic transit time) from well log data in the Oil & Gas industry. The app leverages a Random Forest model trained on well log features such as density (RHOB), gamma ray (GR), neutron porosity (NPHI), and photoelectric factor (PEF) to provide accurate predictions for petroleum engineers and geoscientists.
This project is ideal for analyzing well log data stored in Log ASCII Standard (LAS) files, performing quality control, and visualizing results to support reservoir characterization and exploration.

Table of Contents

Project Overview
Features
Installation
Usage
Model Details
File Structure
Dependencies
Troubleshooting
Contributing
License
Contact


Project Overview
In the Oil & Gas industry, well log data provides critical insights into subsurface formations, aiding in the identification of oil and gas reservoirs. The sonic transit time (DT) is a key measurement that indicates rock properties and porosity, but it may be missing or noisy in some datasets. This web app uses a pre-trained Random Forest model to predict DT values based on other well log measurements, offering a user-friendly interface built with Streamlit.
The app allows users to:

Upload LAS files or input well log data manually.
Predict DT values using a machine learning model.
Visualize predictions alongside actual data for quality control.
Explore clustering results (e.g., K-Means or DBSCAN) to identify rock types or anomalies.

This project builds on the Canadian Well Logging Society’s LAS file format, enabling seamless integration with industry-standard data.

Features

DT Prediction: Predict sonic transit time (DT) using well log features (RHOB, GR, NPHI, PEF).
LAS File Support: Load and process well log data from LAS files.
Data Visualization: Generate log plots and pairplots to compare predicted vs. actual DT values.
Clustering Analysis: Apply K-Means or DBSCAN to group similar rock types or detect outliers.
User-Friendly Interface: Intuitive Streamlit UI for non-programmers, including file uploads and interactive plots.
Model Caching: Efficient model loading using Streamlit’s @st.cache_resource.


Installation
Follow these steps to set up the project locally:

Clone the Repository:
git clone https://github.com/AsmaaMahmoudSaeed/Log_prediction_web_app2.git
cd Log_prediction_web_app2


Create a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

If requirements.txt is missing, install the following:
pip install streamlit pandas numpy scikit-learn joblib gdown lasio seaborn matplotlib


Download the Model:The pre-trained Random Forest model (cmodel.pkl) is hosted on Google Drive. The app automatically downloads it during execution. Ensure you have internet access and Google Drive permissions for the file ID: 1ySNUKWRAhq27DCdnt1t4-fM22XkIFeJ5.

Run the App:Start the Streamlit server:
streamlit run app.py

Open your browser at http://localhost:8501 to access the app.



Usage

Launch the App:Run streamlit run app.py and navigate to the provided URL.

Upload LAS File (if supported):

Use the Streamlit sidebar to upload a LAS file containing well log data (e.g., RHOB, GR, NPHI, PEF, DT).
The app processes the file and extracts relevant features.


Manual Input (alternative):

Enter well log values (e.g., RHOB, GR, NPHI, PEF) manually via input fields in the app.
Click “Predict” to generate DT predictions.


View Results:

The app displays predicted DT values in a table or log plot.
Compare predictions with actual DT (if available) using visualizations.
Explore clustering results (e.g., K-Means or DBSCAN) via pairplots.


Export Results:Save predictions or plots as CSV or image files using Streamlit’s download buttons.


Example:

Upload a LAS file like 15-9-19_SR_COMP.LAS.
Input RHOB=2.34, GR=54.8, NPHI=0.44, PEF=5.0.
Get predicted DT (e.g., 95.7 µs/ft) and visualize it alongside actual data.


Model Details

Algorithm: Random Forest Regressor (from scikit-learn).
Features: Density (RHOB), Gamma Ray (GR), Neutron Porosity (NPHI), Photoelectric Factor (PEF).
Target: Sonic Transit Time (DT, in microseconds per foot).
Training Data: The model was trained on well log data (details not specified in the repository).
Serialization: The model is saved as cmodel.pkl using joblib or pickle.
Preprocessing: Features are assumed to be scaled (e.g., using StandardScaler) for optimal performance.

Note: If your LAS file lacks PEF (e.g., 15-9-19_SR_COMP.LAS), you may need to impute or exclude this feature, or retrain the model without PEF.

File Structure
Log_prediction_web_app2/
├── app.py                # Main Streamlit application script
├── requirements.txt      # Python dependencies (create if missing)
├── cmodel.pkl            # Pre-trained Random Forest model (downloaded at runtime)
├── README.md             # Project documentation (this file)
└── data/                 # Optional: Directory for sample LAS files or test data


app.py: Contains the Streamlit app logic, including model loading, data processing, and visualization.
cmodel.pkl: Downloaded from Google Drive during execution.
data/: Placeholder for LAS files or test datasets (not included in the repository).


Dependencies

Python 3.8 or later
Libraries (install via pip):
streamlit: Web app framework
pandas: Data manipulation
numpy: Numerical computations
scikit-learn: Machine learning (Random Forest)
joblib: Model loading
gdown: Download model from Google Drive
lasio: Read LAS files
seaborn, matplotlib: Data visualization



Create a requirements.txt file with:
streamlit==1.32.0
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.0
joblib==1.4.2
gdown==5.2.0
lasio==0.31
seaborn==0.13.2
matplotlib==3.9.0


Troubleshooting

UnpicklingError: STACK_GLOBAL requires str:

Cause: Mismatch in Python or scikit-learn versions between training and runtime environments.
Fix:
Use the same Python version (e.g., 3.8) and scikit-learn version (e.g., 1.5.0) as the training environment.
Try loading the model with joblib instead of pickle:import joblib
model = joblib.load('cmodel.pkl')


Retrain the model in your current environment and update cmodel.pkl.




Google Drive Download Failure:

Ensure the file ID (1ySNUKWRAhq27DCdnt1t4-fM22XkIFeJ5) is accessible.
Manually download cmodel.pkl and place it in the project directory.


Missing PEF in LAS File:

If your LAS file lacks PEF, impute it (e.g., mean value) or retrain the model without PEF:from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train[['RHOB', 'GR', 'NPHI']], y_train)  # Exclude PEF
joblib.dump(model, 'cmodel.pkl')




Streamlit Errors:

Ensure all dependencies are installed.
Check app.py for syntax errors or missing imports.




Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

Please report issues or suggest features via the Issues tab.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact

Author: Asmaa Mahmoud Saeed
GitHub: AsmaaMahmoudSaeed
Email: [Add your email if desired]
LinkedIn: [Add your LinkedIn profile if desired]

For questions, feedback, or collaboration, please open an issue on GitHub or contact me directly.

Acknowledgments:

Inspired by the need for efficient well log analysis in the Oil & Gas industry.
Built with open-source tools like Streamlit, scikit-learn, and lasio.

