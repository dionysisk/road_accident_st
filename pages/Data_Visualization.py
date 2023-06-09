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


components.iframe("https://dionysisk.eu/RSA/report.html",height = 700, width="80%",scrolling =True)

# components.html(
# '''
#  <iframe id="idIframe" onload="iframeLoaded()" frameborder="0" src="https://dionysisk.eu/RSA/report.html" height="100%" width="100%" scrolling="no"></iframe>
#  ''')


# <script type="text/javascript">
#                       function iframeLoaded() {
#                           var iFrameID = document.getElementById('idIframe');
#                           if(iFrameID) {
#                                 // here you can make the height, I delete it first, then I make it again
#                                 iFrameID.height = "";
#                                 iFrameID.height = iFrameID.contentWindow.document.body.scrollHeight + "px";
#                           }   
#                       }
#                     </script> 
# components.html(
# '''
# <iframe src="https://dionysisk.eu/RSA/report.html"  width="100%"></iframe>
# '''
# )
# components.html(
# '''
# <div class='iframe-parent'>
#   <iframe src="https://dionysisk.eu/RSA/report.html">
#     <p>Hi SOF</p>
#   </iframe>
# </div>

# .iframe-parent{
#   width: 100vw;
#   height: 500vh;
# }

# iframe{
#   width: 100%;
#   height: 100%;
# }
# '''
# )
