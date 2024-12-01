import streamlit as st
st.title('bible Caculator App')
name = 'Sarah'
bible=68
account_username  = 'Godwinninggrace'
account_password = "33567"
account_login = account_username, account_password
bill = 0
st.subheader ("Devotion book Selection")
col1,col2,col3 = st.columns(3)
with col1:n 
     if st.checkbox("Daily Devotions : $69"):
       bill += 10
       st.write ("ok done")
with col2:
    if st.checkbox("Bible Study Guide : $43"):
      bill += 20
      st.write ("ok done")  
with col3:
    if st.checkbox("Prayer Journal : $34"):
      bill += 15
      st.write ("ok done")          
st.subheader ("Outfit")
out1,out2,out3 = st.columns(3)
with out1:
    if st.checkbox("Outfit 1 : $80"):
      bill += 30
      st.write ("ok done")
with out2:
    if st.checkbox("Outfit 2 : $23"):
      bill += 50
      st.write ("ok done")
with out3:
    if st.checkbox("Outfit 3 : $57"):
      bill += 70
      st.write ("ok done")
st.subheader ("Pet Purchase")
pet1,pet2,pet3 = st.columns(3)
with pet1:
    if st.checkbox("dog: $45"):
      bill += 25
      st.write ("ok done")
with pet2:
    if st.checkbox("mouse: $35"):
      bill += 25
      st.write ("ok done")
with pet3:
    if st.checkbox("chicken: $85"):
      bill += 25
      st.write ("ok done")
st.subheader ("Fancy Arifacts")
sub1,sub2,sub3 = st.columns(3)
with sub1:
     if st.checkbox("dimond necklace : $32"):
       bill += 20
       st.write ("ok done")
with sub2:
    if st.checkbox("ruby Necklace : $88"):
      bill += 10
      st.write ("ok done")    
with sub3:
    if st.checkbox("Icon : $69"):
      bill += 30
      st.write ("ok done")        
total = bill + bible
if st.button("Check amount"):
   st.write (name,"your total amount for your Christan journey is",total,"dollars")
