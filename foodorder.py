import streamlit as st

st.title("food Order App")
food1,food2, food3,food4 =st.columns(4) #create 4 colmns called
st.image("https://wallpapers.com/images/hd/best-food-background-0neqcd9ozlv3js9y.jpg")

bill=0

if st.subheader("food category "):

 with food1:
  if st.checkbox("freid rice and crispy chicken: $30"):
   st.write("ok done")
   bill+=30

 with food2:
  if st.checkbox("pounded yam and black soup:$46"):
   bill += 46
   st.write("ok done")
   
 
 with food3:
  if st.checkbox("Garri and beans: $26"):
   st.write("ok done")
   bill += 26
 
 with food4:
  if st.checkbox("Jollof and chicken: $57"):
   st.write("ok done")
   bill += 57

if st.button("Check total bill"):
   st.write('Hi,your total bill is,')