import streamlit as st

st.title('coins app')

name = st.text_input("Please enter your name")

gold_coins = st.number_input("Please enter your amount of gold_coins:")

silver_coins = st.number_input("Please enter your amount of silver_coins:")

bronze_coins = st.number_input("Please enter your amount of bronze_coins:")

total_spent = (gold_coins + silver_coins + bronze_coins)
("Hi", name," your total amount of coins is ", total_spent)