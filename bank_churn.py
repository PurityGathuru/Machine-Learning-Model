import streamlit as st

import pandas as pd

import pickle

pickled_model = pickle.load(open('C:/Users/Administrator/Desktop/flaskintro/bank.pkl','rb'))

def main():
    st.title('Bank Churn')

    CreditScore = st.text_input('CreditScore')
    Age = st.text_input('Age')
    Tenure = st.text_input('Tenure')
    Balance = st.text_input('Balance')
    NumofProducts = st.text_input('Numofproducts')
    HasCrCard = st.text_input('HasCrCard')
    IsActiveMember = st.text_input('IsActiveMember')
    EstimatedSalary = st.text_input('EstimatedSalary')
    Geography_Germany = st.text_input('Geography_Germany')
    Geography_Spain = st.text_input('Geography_Spain')
    Gender_Male = st.text_input('Gender_Male')

    #prediction

    if st.button('Predict'):
        makeprediction = pickled_model.predict([[CreditScore,Age,Tenure,Balance,
                                         NumofProducts,HasCrCard,IsActiveMember,
                                         EstimatedSalary,Geography_Germany,
                                                 Geography_Spain,Gender_Male]])
        if makeprediction[0] == 0:
            st.success('Customers will not churn')
        elif makeprediction[0] == 1:
            st.error('Customers will churn')

        #output = round(makeprediction[0],2)
        #st.success(format(output))




if __name__ == '__main__':
    main()

#joblib.dump(rf,'churn_predict_model')
#model = joblib.load('churn_predict_model')

#smodel.predict([[619,42,2,0.0,0,0,0,101348.88,0,0,0]])