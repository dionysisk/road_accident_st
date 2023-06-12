import streamlit as st
import pandas as pd
from model import prediction, scores

BGC=joblib.load('GradientBoostingClassifier.joblib')
def display_model(choice)
   if choice=='Gradient Boosting':
      st.write('Gradient Boosting score train 74.286 rmse train 0.507')

st.markdown('# Machine learning models')
st.write("""Generally speaking we can consider that accuracy scores:
    
                          - Over 90% - Very Good
                    - Between 70% and 90% - Good
                    - Between 60% and 70% - OK""")

choices = ['Random Forest','SVC','KNN','XGBOOST','Gradient Boosting']

option = st.selectbox(
         'Which model do you want to try ?',
         choices)

st.write('You selected :', option)


display_model(option)
