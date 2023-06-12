import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import streamlit as st
import xgboost as xgb
from xgboost import XGBClassifier
import joblib

#df = pd.read_csv('https://drive.google.com/file/d/1dLzhkMdx58uzJIjhqyFSQBFPKAIiZXhT/view?usp=sharing')
choices = ['Random Forest','SVC','KNN','XGBOOST','Gradient Boosting']
BGC=joblib.load('GradientBoostingClassifier.joblib')


def prediction(classifier):
   if classifier == 'Gradient Boosting':
      st.write(BGC.score(X_test, y_test))
      st.dataframe(confusion_matrix(y_test, BGC.predict(X_test)))
      st.text(classification_report(y_test, BGC.predict(X_test)))
      #st.write('RMSE Score test=',np.sqrt(MSE(y_test, model.predict(X_test))))
         
def display_model(choice)
   if choice=='Gradient Boosting':
      st.write('Gradient Boosting score train 74.286 rmse train 0.507')
         
st.title('Our model prediction page')
   
option = st.selectbox(
     'Which model do you want to try ?',
     choices)

display_model(option)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
   df = pd.read_csv(uploaded_file)
   y_test =df['severity']
   X_test = df.drop(['severity','gravMerged'], axis = 1)
   prediction(option)
#    st.write(model.score(X_test, y_test))
#    st.dataframe(confusion_matrix(y_test, model.predict(X_test)))
#    st.text(classification_report(y_test, model.predict(X_test))
#    st.write('RMSE Score test=',np.sqrt(MSE(y_test, model.predict(X_test))) )





# #result = loaded_model.score(X_test, Y_test)
# #print(result)

# def prediction(classifier):
#     if classifier == 'Random Forest':
#         clf = RandomForestClassifier()
#     elif classifier == 'SVC':
#         clf = SVC()
#     elif classifier == 'KNN':
#         clf = KNeighborsClassifier()
#     elif classifier == 'XGBOOST':
#         clf = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
#         #clf = joblib.load("xgb_model.sav")
#     elif classifier == 'Gradient Boosting':
#         clf = GradientBoostingClassifier()
#         #clf = joblib.load('gbc_model.sav')
        
#     clf.fit(X_train, y_train)
#     return clf
    
# def scores(clf, choice):
#         if choice == 'Accuracy':
#              return clf.score(X_test, y_test)
#         elif choice == 'Confusion matrix':
#             return confusion_matrix(y_test, clf.predict(X_test))
#         elif choice == 'Classification report':
#             return classification_report(y_test, clf.predict(X_test))
