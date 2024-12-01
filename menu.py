import streamlit as st
name = st.text_input("Please eneter student name")
age = st.number_input('Enter your age')
year=st.selectbox("input your year,["year1","year2","year3"]")
if st.button ("send results"):
    dic = ("name")