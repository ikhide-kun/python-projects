import streamlit as st
st.title('saving app')
name = st.text_input("Please enter your name")
cash = 5000.
phone_cost = st.number_input ('Please enter the phone_cost',0)
clothes_cost = st.number_input ('please enter the clothes_cost',0)
book_cost = st.number_input ('please enter the book_cost',0)
decoration_cost = st.number_input ('please enter the decortion_cost',0)
dinner_cost = st.number_input ('please enter the dinner_cost',0)
remaining_amount = ("Your remaining amount of phone + clothes_cost + book_cost + decortion_cost + dinner_cost")
("Hi", name, "your total_cost + phone_cost + clothes_cost + book_cost + decortion_cost + dinner_cost.")