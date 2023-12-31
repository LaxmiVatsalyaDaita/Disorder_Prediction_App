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
    percent = loaded_model.predict_proba(input_data_reshaped)
    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    print(risk_percent)
    
    if (prediction[0] == 0):
        return 'the person is not at a risk of sleep disorder' 
    else:
        return 'the person is at a risk of sleep disorder'
    
# function to find probability of risk of a disorder    
def percentage_of_risk(input_data):
    
    input_data_as_np_array = np.asarray(input_data) 

    input_data_reshaped = input_data_as_np_array.reshape(1,-1) 

    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    
    print(risk_percent)
    
    return str(risk_percent)
    
    
# UI

def main():
    
    #Gender, age, Occupation, sleepDuration, qualityOfSleep, phyActivityLevel, stressLevel, BMI, heartRate, dailySteps, bpUpper, bpLower = 0,0,0,0,0,0,0,0,0,0,0,0    
    
    # title for webpage
    st.set_page_config(page_title="Sleep Disorder", page_icon=":zzz:", layout="wide")
    st.title(':sleeping: Sleep Disorder Risk Prediction')
    st.markdown('<style>div.block-container{padding-top:1rem;}<style>', unsafe_allow_html=True)
    # creating input data fields to get data from user
    
    #'Gender', 'Age', 'Occupation', 'Sleep Duration', 'Quality of Sleep',
    #'Physical Activity Level', 'Stress Level', 'BMI Category', 'Heart Rate',
    #'Daily Steps', 'Sleep Disorder', 'bp_upper', 'bp_lower'
    
    col1, col2 = st.columns((2))
    
    with col1:
        st.subheader(':spiral_note_pad: General Information ')
        age = st.slider('Age', 0,100,1)
        
        button1, button2 = st.columns((2))
        with button1:
            gender = st.selectbox('Gender', ['Male', 'Female'])
        with button2:
            occupation = st.selectbox('Occupation',['Other', 'Doctor', 'Teacher', 'Nurse', 'Engineer', 'Accountant',
       'Lawyer', 'Salesperson'])
               
        st.subheader(':zzz: Sleeping Conditions ')
        sleepDuration = st.text_input('Average Sleep Duration in hours')
        if sleepDuration.isalpha():
            st.write('Please enter a number')
            sleepDuration = 0
        qualityOfSleep = st.slider('Quality of Sleep', 0.0,10.0,step=0.5)
        stressLevel = st.slider('Average Stress Level', 0,10,1)
    
    
    with col2:
        st.subheader(':muscle: Fitness Conditions')
        bmi = st.selectbox('BMI Category',['Overweight', 'Normal', 'Obese'])
        phyActivityLevel = st.slider('Level of Physical Activity', 0,100,1)
        heartRate = st.text_input('Heart Rate')
        if heartRate.isalpha():
            st.write('Please enter a number')
            heartRate = 0
        dailySteps = st.text_input('Daily Steps')
        if dailySteps.isalpha():
            st.write('Please enter a number')
            dailySteps = 0
        bpUpper = st.text_input('Systolic (upper Blood Pressure)')
        if bpUpper.isalpha():
            st.write('Please enter a number')
            bpUpper = 0
        bpLower = st.text_input('Diastolic (lower Blood Pressure)')
        if bpLower.isalpha():
            st.write('Please enter a number')
            bpLower = 0
                 
    
        
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
        
    input_features = [Gender, age, Occupation, sleepDuration, qualityOfSleep, phyActivityLevel, stressLevel, BMI, heartRate, dailySteps, bpUpper, bpLower]
        
    # code for prediction
    diagnosis = '' # creating an empty string to store the result
    percent_of_risk = ''
    
    # creating button for predicting
    col1, col2 = st.columns((2))
    
    with col1:
        if st.button('Risk Prediction'):
            diagnosis = sleep_disorder_prediction(input_features)
        
        st.write(diagnosis)
        
        if st.button('Risk Estimation'):
            percent_of_risk = percentage_of_risk(input_features)
            
        st.write(percent_of_risk)
        
        st.write(':triangular_flag_on_post: Nearly everyone has an occasional sleepless night. However, if you often have trouble sleeping, contact your health care provider.')
        
    with col2:
        with st.expander("Tips for Better Sleep Health"):
            st.markdown('* Stick to a sleep schedule' )
            st.markdown('* Pay attention to what you eat and drink')
            st.markdown('* Create a restful environment')
            st.markdown('* Limit daytime naps')
            st.markdown('* Include physical activity in your daily routine')
            st.markdown('* Manage worries')
        
    
    
          
            
    

if __name__ == '__main__':
    main() # doing this makes the code work as a stand-alone file. importing this file would not work. 
