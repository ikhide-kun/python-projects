import streamlit as st

st.title('sport app')

name = st.text_input("Please enter your name")

favorite_sport= st.text_input("Please enter your favorite_sport:")

favorite_team=st.text_input("Please enter your favorite_team:")

favorite_player=st.text_input("Please enter your favorite_player:")
st.write("Hi", name, "Your favorite sport is" ,favorite_sport, "you cheer for", favorite_team, "and your favorite player is" , favorite_player)