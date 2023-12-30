import numpy as np
import pickle
import streamlit as st

import warnings
warnings.filterwarnings("ignore")

# loading the saved model
loaded_model = pickle.load(open('trained_adb_model.sav', 'rb')) 

# create function for prediction
def sleep_disorder_prediction(input_data):
    
    input_data_as_np_array = np.asarray(input_data) 

    input_data_reshaped = input_data_as_np_array.reshape(1,-1) 

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'the person is not at a risk of sleep disorder'
    else:
        return 'the person is at a risk of sleep disorder'
    
    
    
# UI

def main():
    # title for webpage
    st.set_page_config(page_title="Sleep Disorder", page_icon=":zzz:", layout="wide")
    st.title('Sleep Disorder Risk Prediction')
    st.markdown('<style>div.block-container{padding-top:1rem;}<style>', unsafe_allow_html=True)
    # creating input data fields to get data from user
    
    #'Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep',
    #'Physical Activity Level', 'Stress Level', 'BMI Category', 'Heart Rate',
    #'Daily Steps', 'Sleep Disorder', 'bp_upper', 'bp_lower'
    
    age = st.slider('Age', 0,100,1)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    occupation = st.selectbox('Occupation',['Other', 'Doctor', 'Teacher', 'Nurse', 'Engineer', 'Accountant',
       'Lawyer', 'Salesperson'])
    bmi = st.selectbox('BMI Category',['Overweight', 'Normal', 'Obese'])
    sleepDuration = st.text_input('Average Sleep Duration in hours')
    qualityOfSleep = st.text_input('Quality of sleep on a scale of 1 to 10')
    phyActivityLevel = st.text_input('Physical Activity on a scale of 0 to 100')
    stressLevel = st.text_input('Stress Level on a scale of 1 to 10')
    heartRate = st.text_input('Heart Rate')
    dailySteps = st.text_input('Daily Steps')
    bpUpper = st.text_input('Systolic (upper number)')
    bpLower = st.text_input('Diastolic (lower number)')
    
    
    # encoding the categorical inputs
    if (gender=='Male'):
        Gender = 1
    elif (gender=='Female'):
        Gender = 0
        
    if (occupation=='Accountant'):
        Occupation = 0
    elif (occupation=='Doctor'):
        Occupation = 1
    elif (occupation=='Engineer'):
        Occupation = 2
    elif (occupation=='Lawyer'):
        Occupation = 3
    elif (occupation=='Nurse'):
        Occupation = 4
    elif (occupation=='Other'):
        Occupation = 5
    elif (occupation=='Salesperson'):
        Occupation = 6
    elif (occupation=='Teacher'):
        Occupation = 7
        
        
    if (bmi=='Overweight'):
        BMI = 2
    elif (bmi=='Normal'):
        BMI = 0
    elif (bmi=='Obese'):
        BMI = 1
        
        
        
    # code for prediction
    diagnosis = '' # creating an empty string to store the result
    
    # creating button for predicting
    if st.button('Risk Prediction'):
        diagnosis = sleep_disorder_prediction([Gender, age, Occupation, sleepDuration, qualityOfSleep, phyActivityLevel, stressLevel, BMI, heartRate, dailySteps, bpUpper, bpLower])
        
    st.success(diagnosis)
    


if __name__ == '__main__':
    main() # doing this makes the code work as a stand-alone file. importing this file would not work. 