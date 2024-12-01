write a program for a use
-ask for the name and -age - use a radio to ask for gender
-use a selectbox to ask to choose best color - use a type to ask best game
-use a type to ask to type best movie - use a type to ask best friend
create a submit button and show this in a success bar
Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe
import streamlit as st

st.(qeustion app)

name = st.text_input("Please enter your name")

age = st.number_input("Please enter your age")

gender = st.radio("enter your gender,["male"",""female"], horizontal = true")

coluor = st.selectbox("enter your favourite colour")

game = st.text_input("Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe")

("Hi", name, "Your age     is",age," you love the character", favorite_character, "and your favorite part is" ,favorite_part)