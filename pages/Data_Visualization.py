import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import datetime as dt





#from pathlib import Path
#DATA_URL = Path(Training/Datascientist/Coursera).parents[1] / 'Motor_Vehicle_Collisions_-_Crashes.csv'
data_URL='https://ln5.sync.com/dl/295f1a2d0/zafid975-55tvqwxn-vju4dapn-ciqbhmu7'
df = pd.read_csv(data_URL)
# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#   DATA_URL = pd.read_csv(uploaded_file).sample(n=100000)

# df = DATA_URL

df.dropna(subset=['LATITUDE', 'LONGITUDE','CRASH_DATE','CRASH_TIME'], inplace=True)
st.title("Data Visualition of Road Accident")
st.markdown("This application is a Streamlit dashboard that can be use to analyze road accident in France🗼🥐🇫🇷🥖🚗💥🚙")

from PIL import Image


df['date/time'] =df['DateTime']
#pd.to_datetime(df['CRASH_DATE'] + ' ' + df['CRASH_TIME'])
data = df

#data = load_data(20000)

#original_data = data

st.header("Where are the most people injured in France?")
injured_people = st.slider("Number of person injured in road accident",0, 100)
st.map(data.query("INJURED_PERSONS >= @injured_people")[['LATITUDE', 'LONGITUDE']].dropna(how="any"))


st.header("How many road accident during a given time of the day?")
hour = st.slider("Hour to look at", 0, 23)
data = data[data['date/time'].dt.hour == hour]


st.markdown("road accident between %i:00 and %i:00" % (hour, (hour + 1) % 24))
midpoint = (np.average(data['LATITUDE']), np.average(data['LONGITUDE']))

st.pydeck_chart(pdk.Deck(map_style="mapbox://styles/mapbox/streets-v12", initial_view_state={"latitude": midpoint[0],"longitude": midpoint[1],"zoom": 11,"pitch": 50},
     layers=[pdk.Layer("HexagonLayer", data=data[['date/time','LATITUDE','LONGITUDE']], get_position=['LONGITUDE','LATITUDE'], radius=100, extruded=True, pickable=True,
         elevation_scale=4, elevation_range=[0,1000])]))

st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) %24))
filtered = data[
     (data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour +1))
]
hist = np.histogram(filtered['date/time'].dt.minute, bins=60, range=(0,60))[0]
chart_data = pd.DataFrame({'minute':range(60), 'crashes':hist})
fig = px.bar(chart_data, x='minute',y='crashes', hover_data=['minute','crashes'], height=400)
st.write(fig)



st.header("Top 5 dangerous city by injury type")
select = st.selectbox('Injured people', ['Pedestrian','Cyclists','Motorists'])

if select == 'Pedestrian':
    st.write(data.query("INJURED_PEDESTRIANS >= 1")[["ON_STREET_NAME","INJURED_PEDESTRIANS"]].sort_values(by=['INJURED_PEDESTRIANS'], ascending=False).dropna(how='any')[:5])

elif select == 'Cyclists':
    st.write(data.query("INJURED_CYCLISTS >= 1") [["ON_STREET_NAME","INJURED_CYCLISTS"]].sort_values(by=['INJURED_CYCLISTS'], ascending=False).dropna(how='any')[:5])

else:
    st.write(data.query("INJURED_MOTORISTS >= 1") [["ON_STREET_NAME","INJURED_MOTORISTS"]].sort_values(by=['INJURED_MOTORISTS'], ascending=False).dropna(how='any')[:5])





if st.checkbox("Show Raw Data", False):
   st.subheader('Raw Data')
   st.write(data)
