import numpy as np
import pickle

import warnings
warnings.filterwarnings("ignore")

loaded_model = pickle.load(open('trained_adb_model.sav', 'rb')) 

input_data = (0, 35, 2, 7.0, 8, 65, 5, 2, 73, 3000, 140, 90)

input_data_as_np_array = np.asarray(input_data) 

input_data_reshaped = input_data_as_np_array.reshape(1,-1) 

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
pred = loaded_model.predict_proba(input_data_reshaped)
risk = pred[:,1]
risk_percent = round(risk[0]*100, 2)
print(risk_percent)
if (prediction[0] == 0):
    print('the person is not at a risk of sleep disorder')
else:
    print('the person is at a risk of sleep disorder')
