import streamlit as st
from joblib import load

model = load('salary_food_model.joblib')

# create Streamlit app
st.title('Salary vs Food Expense Prediction')

# Add input fields for income
income = st.number_input('Enter your monthly income', min_value=0, max_value=100000)

# Add prediction button
predict_button = st.button('Predict')

# Add prediction logic
if predict_button:
    #input data into 2d array
    input_data = [[income/1000]]
    #predict the food expense
    prediction = model.predict(input_data)[0]
    #display the prediction
    st.write('Predicted food expense:',round(prediction*100,2),'THB')