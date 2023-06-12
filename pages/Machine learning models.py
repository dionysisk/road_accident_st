import streamlit as st
import pandas as pd
st.markdown(f'# {list(page_names_to_funcs.keys())[4]}')
from model import prediction, scores

st.write("""Generally speaking we can consider that accuracy scores:
    
                          - Over 90% - Very Good
                    - Between 70% and 90% - Good
                    - Between 60% and 70% - OK""")

choices = ['Random Forest','SVC','KNN','XGBOOST','Gradient Boosting']

prediction = st.cache(prediction,suppress_st_warning=True)
option = st.selectbox(
         'Which model do you want to try ?',
         choices)

st.write('You selected :', option)

clf = prediction(option)

display = st.selectbox(
         "What do you want to display ?",
         ('Accuracy', 'Confusion matrix','Classification report'))

if display == 'Accuracy':
        st.write(scores(clf, display))
elif display == 'Confusion matrix':
        st.dataframe(scores(clf, display))
elif display == 'Classification report':
        #st.table(classification_report(y_test, clf.predict(X_test)))
        st.text(scores(clf, display))
        
        
