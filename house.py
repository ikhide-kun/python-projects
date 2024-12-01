import streamlit as st
bill = 0
st.title("House Buyer app")

col1, col2 = st.columns(2)


with col1:
     name = st.text_input('Please enter your name')

with col2:
    yearly_salary= st.number_input('Please your salary',0)
if st.checkbox("Check the house you can afford "):
      if yearly_salary < 10000:
        st.write("Sorry you can afford any houses yet")
elif  yearly_salary >= 10000 and yearly_salary <= 10000:
          st.write ("You can rent or buy an aprtment")
          if st.checkbox("Buy an apartment: $60,000"):
               st.write("Ok Done")
               bill +=60000
          if st.checkbox("Rent an apartment yearly: $4,000"):
               st.write("Ok Done")
               bill +=4000
elif yearly_salary > 100000 and yearly_salary <= 500000:
     st.write ("You can rent or buy a bungalow")
     if st.checkbox("Buy a Bungalow: $200,000"):
          st.write("Ok done")
          bill +=200000
     if st.cheakbox("Rent a Bunalow Yearly: $10,000"):
          st.write("Ok Done")
          bill +=10000
elif yearly_salary > 1000000 and yearly_salary <= 5000000:
     st.write("You can buy or rent a Mansion")
     if st.checkbox("Buy a Mansion: $3,000,000"):
        st.write("Ok Done")
        bill +=3000000
elif yearly_salary > 5000000:
     st.write("You can buy an estate")
     if st.write ("Ok Done"):
      bill +=8000000


if st.write("Ok Done"):
    st.write(name,'your total bill is', bill)