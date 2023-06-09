import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

st.set_page_config(
     page_title="Data visualization",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state ="auto",
 )


# components.iframe("https://dionysisk.eu/RSA/report.html",height = 700, width=800,scrolling =True)

# components.html(
# '''
#  <iframe id="idIframe" onload="iframeLoaded()" frameborder="0" src="https://dionysisk.eu/RSA/report.html" height=700 width="100%" scrolling="no"></iframe>
#  ''')



components.html(
'''
<iframe src="https://dionysisk.eu/RSA/report.html" height="800"></iframe>
'''
)
