import streamlit as st

colour ='Blue'
# how you store muliple item in one varable"?
#Data collections
# -list
games = ['minecraft','Roblox','Gta 5'] #store multiple item in a varable

st.write(games)

#Selectionbox
#this is used to give users mulitple option in a box to select from

animal = st.selectbox("Choose any animal",['cat', 'dog', 'loin'])

st.write("The animal you selected was",animal)

#RADID
#this is used to give users multiple options to select from. doesn't show in box, so used with little options
gender = st.radio("Choose gender",['male','female'],horizontal=True)

st.write("You are a", gender)

 #EMU
 #this is used to select from one page to another
 menu = st.slidebar.selectbox("Choose menu",['Homepage''Contact us ','Database'])
 
 if menu == 'homepage':
    st.subheader("Homepage")

elif menu == 'Contact us':
    st.subheader("Contact us")

elif menu == 'Database':
    st.subheader("Database")    