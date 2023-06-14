import streamlit as st
import pandas as pd
#from model import prediction, scores
import numpy as np
import pydeck as pdk
import plotly.express as px
import datetime as dt
import streamlit.components.v1 as components
from PIL import Image


st.set_page_config(
    page_title="RA_France",
    page_icon="💥",
)

st.write("#      Road Accidents in France")

st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Multi_vehicle_accident_-_M4_Motorway%2C_Sydney%2C_NSW_%288076208846%29.jpg",
            width=700 # Manually Adjust the width of the image as per requirement
        )
st.markdown("""
        **👈 Select the page from the dropdown on the left** to select : EDA, Dataviz, Modelling 
        or Shap Interpretation!
        ### Summary of our main tasks done to use Streamlit /GitHub

            - we prepared the data set to gain some memory
            - we select the road accident from 2012-2015
            - we kept road accident 2016 seperately to compare with our prediction
            - we did run the classification non-linear models: GBC - RFC - KNN - SVC - (XGBOOST?)
            - EDA and Dataviz are using road accidents from 2012 to 2016 
            
        ### Team

        - Deepa
        - Fan
        - Sidi
        
        Tutoring : Francesco
        
    """
    )
st.markdown("![Alt Text](https://media.tenor.com/tuArNck3bKwAAAAC/car-crash.gif)")

