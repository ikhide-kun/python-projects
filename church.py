import streamlit as st

st.title("church app")

col1, col2 = st.columns(2)


with col1:
     name = st.text_input('Please enter the names of the people in the church ')

with col2:
    age= st.number_input('Please enter the age')
 
gen = st.text("Please eneter your gender")
if age > 3:

 st.write ("sorry your not old enough to to be in the children church ")

elif age > 3 and age < 13:

 st.write ('welcome to the kid church group')
elif age > 3 and age < 12:

 st.write ('welcome to the teens church group')
elif age > 13 and age < 19:

 st.write ('welcome to the youth church group')
elif age > 20 and age < 35:

 st.write ('welcome to the Adult church group')
elif age > 36 and age < 64:

 st.write ('welcome to the Elders church group')