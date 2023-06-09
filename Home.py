import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="RA_France",
    page_icon="🚗💥🚙",
)

"""
# Welcome to IC team!

Bonsoir nia mouah !!!!! καλημέρα

"""
from PIL import Image
st.image("https://waterlust.com/cdn/shop/collections/SB_BG_016_1600x.jpg?v=1668631373",
            width=600 # Manually Adjust the width of the image as per requirement
        )

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    # Welcome to IC team!

    Bonsoir nia mouah !!!!! καλημέρα
    """
)

