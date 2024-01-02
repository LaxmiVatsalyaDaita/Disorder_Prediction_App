# Disorder_Prediction_App

The web application has been deployed [here](https://sleepdisorderpredictionapp-c9bz3wggwq9jkata4qfvez.streamlit.app/) using *streamlit.io*

## To run the code on local machine:
1. Clone the Git Repository.
2. Install the required libraries by running `pip install -r requirements.txt` in terminal.
3. Use `streamlit run app.py` to run the app on localhost.
4. Incase the port is busy and an exception occurs, try running `streamlit run app.py --server.port 8080`.

## Description of the files included:
1. **Sleep_health_dataset.csv**: This is the dataset used for EDA and to train the model.
2. **sleep_disorders.ipynb**: This jupyter notebook contains code for the data preprocessing and for training and testing various ML algorithms. It was found that using *AdaBoost Algorithm* gave the best test accuracy (92.92%) for the dataset.
3. **trained_adb_model.sav**: The trained adaboost model has been saved in this file using pickle.
4. **pred.py**: This is a sample file for loading and testing the predictive adaboost model before integrating it into the app.
5. **app.py**: This file contains the code for the web app built using the Streamlit library.
6. **requirements.txt**: This file contains the required libraries.

## Description of possible errors:
* The version of pickle used for pickling the file and depickling the file must be the same to avoid any code breakage while building the app.
