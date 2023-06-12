import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import datetime as dt
import streamlit.components.v1 as components

st.set_page_config(
     page_title="Data visualization",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state ="auto",
 )

st.header('Data Visualization')

#from PIL import Image
# st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/Data_Visualization_Tools.jpg", width=700)
# @st.cache_data
st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/Data_Visualization_Tools.jpg")
@st.cache_data

#LOAD Data
def load_data(url):
 df = pd.read_csv(url)
 return df

df = load_data('https://bol.mondial-assistance.gr/Files/Eda_basic/Eda_basic_Dataviz_07_06_2023.csv')
 
#dropna
df.dropna(subset=['LATITUDE', 'LONGITUDE','CRASH_DATE','CRASH_TIME'], inplace=True)


df['date/time'] = pd.to_datetime(df['CRASH_DATE'] + ' ' + df['CRASH_TIME'])
data = df

#1. Visualization
st.header("Where are the most people injured in France?")
injured_people = st.slider("Number of person injured in road accident",0, 100)
st.map(data.query("INJURED_PERSONS >= @injured_people")[['LATITUDE', 'LONGITUDE']].dropna(how="any"))

#2. Visualization
st.header("How many road accident during a given time of the day?")
hour = st.slider("Hour to look at", 0, 23)
datahour = data[data['date/time'].dt.hour == hour]

st.markdown("road accident between %i:00 and %i:00" % (hour, (hour + 1) % 24))
midpoint = (np.average(datahour['LATITUDE']), np.average(datahour['LONGITUDE']))

visdata=datahour[['LATITUDE','LONGITUDE']]
st.pydeck_chart(pdk.Deck(
     map_style="mapbox://styles/mapbox/streets-v12",
     initial_view_state={"latitude": midpoint[0],"longitude": midpoint[1],"zoom": 8,"pitch": 50},
     layers=[
          pdk.Layer(
               "HexagonLayer",
               data=datahour,
               get_position=['LONGITUDE','LATITUDE'],
               radius=100,
               extruded=True,
               pickable=True,
               elevation_scale=4,
               elevation_range=[0,1000]
          ),
     ],
))



#4. Visualization
st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) %24))
# filtered = data[
#  (data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour +1))
# ]
hist = np.histogram(datahour['date/time'].dt.minute, bins=60, range=(0,60))[0]
chart_data = pd.DataFrame({'minute':range(60), 'crashes':hist})
fig = px.bar(chart_data, x='minute',y='crashes', hover_data=['minute','crashes'], height=400)
st.write(fig)

#5. Visualization
st.header("Top 8 dangerous area by zone")
#select = st.selectbox('Injured people', ['Pedestrian','Cyclists','Motorists'])
select = st.selectbox('Injured people', ['Department','Commune','Street'])

if select == 'Department':
     st.write(data.query("INJURED_PERSONS >= 1")[["dep","INJURED_PERSONS"]].sort_values(by=['INJURED_PERSONS'], ascending=False).dropna(how='any')[:8])
elif select == 'Commune':
     st.write(data.query("INJURED_PERSONS >= 1")[["com","INJURED_PERSONS"]].sort_values(by=['INJURED_PERSONS'], ascending=False).dropna(how='any')[:8])
else:
     st.write(data.query("INJURED_PERSONS >= 1")[["ON_STREET_NAME","INJURED_PERSONS"]].sort_values(by=['INJURED_PERSONS'], ascending=False).dropna(how='any')[:8])


if st.checkbox("Show Raw Data", False):
   st.subheader('Raw Data')
   st.write(data)

