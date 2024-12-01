import streamlit as st

st.title("food Order App")
fruit1,fruit2, fruit3,fruit4 =st.columns(4) #create 4 colmns called
st.image("food background ")

bill=0

if st.subheader("food category "):

 with fruit1:
  if st.checkbox("freid rice and crispy chicken: $30"):
   st.write("ok done")
  bill=0

 with fruit2:
  if st.checkbox("pounded yam and black soup:$46"):
   st.write("ok done")
  bill=0
 
 with fruit3:
  if st.checkbox("Garri and beans: $26"):
   st.write("ok done")
  bill=0
 
 with food4:
  if st.checkbox("Jollof and chicken: $57"):
   st.write("ok done")
  bill=0









  