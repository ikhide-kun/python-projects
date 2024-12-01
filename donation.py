import streamlit as st
saved_amount=495954
st.title("sport term app")
name =st.text_input ("Please enter your name")

bill=0

if st.subheader("match_ticket",0):
 if st.checkbox("match_ticket",0):
  st.number_input('Enter amount spent for buying match ticket',0)
 st.write("ok done")
bill += 100

if st.subheader("season pass",0):
 if st.checkbox("season pass",0):
  st.number_input('Enter amount spent for buying season pass',0)
 st.write("ok done")
bill += 230

ticket_sales= st.number_input('Enter amount earned from selling Tickets',0)
Refreshment_sales= st.number_input('Enter amount earned from selling refreshments',0)
total_amount_spent = match_ticket + equipment_cost + prize_cost + refreshments_cost
total_amount_earned = ticket_sales + Refreshment_sales
total_earned = saved_amount + total_amount_earned
remaining_balance = total_earned - total_amount_spent
if remaining_balance > 0:
    st.write  (name,'your remaining amount is ',remaining_balance)
elif remaining_balance <= 0:
    st.write (name,"you have spent more than you have saved ")