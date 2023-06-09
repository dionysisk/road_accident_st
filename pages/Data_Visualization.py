import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')


HtmlFile = open("output.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
#components.html(source_code, height = 700, width=800,scrolling =True)
components.iframe("https://github.com/DimitrisPatros/streamlitRoadAccidents/blob/8dbd88619050fb110c1ed92314a93159f2a5df24/pages/output.html", height = 700, width=800,scrolling =True)

