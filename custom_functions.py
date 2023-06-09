import pandas as pd
import streamlit as st

def read_uploaded_file(uploaded_file):
  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file,low_memory=False).sample(n=100000)
    return df
