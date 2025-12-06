import streamlit as st
import pandas

## using streamlit
india = {
  "Players": ['Rohit','Dhawan','Virat','Rahul','Dhoni','Hardik','Jadeja','Ashwin','Kuldeep','Bumrah','Shami'],
  "Average": [120,130,170,130,145,117,126,70,66,55,14],
  "Runs" : [152,32,88,28,44,18,26,0,12,8,1]
}
SouthAfrica= {
  "Players": ['Rohit','Dhawan','Virat','Rahul','Dhoni','Hardik','Jadeja','Ashwin','Kuldeep','Bumrah','Shami'],
  "Average": [110,120,150,110,135,107,156,121,198,55,22],
  "Runs" : [152,32,88,28,44,18,26,0,12,8,1]
}
indiaData = pandas.DataFrame(india)
SouthAfricaData =pandas.DataFrame(SouthAfrica)
st.title("Welcome")
st.subheader("subhead")
st.write("Testing streamlit")
st.write(indiaData) #table
st.write(SouthAfricaData) #table
st.line_chart(indiaData)  #Graph
st.line_chart(SouthAfricaData)  #Graph
st.area_chart(indiaData) #AreaChart

myslider = st.slider('celsius')
st.write(myslider, ': in farenheit - ',myslider*9/5+32)

