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


components.iframe("https://dionysisk.eu/RSA/report.html",height = 700, width=1000,scrolling =True)

# components.html(
# '''
#  <iframe id="idIframe" onload="iframeLoaded()" frameborder="0" src="https://dionysisk.eu/RSA/report.html" height=700 width="100%" scrolling="no"></iframe>
#  ''')



# components.html(
# '''
# <html>
#    <head>
#       <script>
#          window.onload = function() {
#             var iframe = document.getElementById("myiframe");
#             iframe.width = iframe.contentWindow.document.body.scrollWidth;
#             iframe.height = iframe.contentWindow.document.body.scrollHeight;
#          }
#       </script>
#    </head>
#    <body>
#       <iframe id="myiframe" src=""https://dionysisk.eu/RSA/report.html""></iframe>
#    </body>
# </html>
# '''
# )
