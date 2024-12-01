import streamlit as st

st.title(' item app')

name = st.text_input("Please enter your name")

 book_cost = st.text_input("Please enter your amount of  book_cost:")

snacks_cost  = st.text_input("Please enter your amount of snacks_cost :")

toy_cost = st.text_input("Please enter your amount of toy_cost :")

("Hi", name, "Your snacks_cost is",favorite_book," you love the character", toy_cost , "and your favorite part is" ,snacks_cost)