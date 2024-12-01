name = input ("Please enter your name ")
pencil_pack_cost = input ("Please enter your amount of pencil_pack_cost:")
sketchbook_cost = input("Please enter your amount of stetchbook_cost:")
marker_pack_cost = input ("Please enter your amount of marker_pack_cost:")
coupon = input ("please enter your amount of coupons")
total_spent = ("please enter your amount of things total_spent")










































import streamlit as st

#how to run: click terminal, click + sign and type this: streamlit run filename.py

st.title('Age calculatorApp') #big text

name = st.text_input("Please enter your name") #text_input is to ask for text/ string

yob = st.number_input("Please enter your year of birth", 0) #number_input is when you want to ask for a

currentyear = st.number_input("Please enter your currrent year",0)

age = currentyear = yob

if st. button("Cheack Age"): #check if this button called check age is clicked
   st.write(name,'you will be',age,'in', currentyear)#do this
    # the space in front is indentation (only run this when code above is true)
