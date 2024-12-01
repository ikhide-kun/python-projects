 import streamlit as st

st.title(' book app')

name = st.text_input("Please enter your name")

favorite_book = st.text_input("Please enter your amount of favorite_book:")

favorite_character = st.text_input("Please enter your amount of favorite_character:")

favorite_part= st.text_input("Please enter your amount of favorite_part:")

("Hi", name, "Your favorite book is",favorite_book," you love the character", favorite_character, "and your favorite part is" ,favorite_part)