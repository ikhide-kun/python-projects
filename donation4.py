import streamlit as st
import pandas as pd
readcsv = pd.read_csv ('donate.csv')
name = ("please enter name")
menu = st.sidebar.selectbox("choose an option",["Donations","view Donations","Donate"])
if menu == 'Donations':
    st.subheader (':blue [Create Donation]')
    st.divider()
    col1,col2 = st.columns(2)
with col1:
     cam_title = st.text_input ("State Campaign Title")
with col2:
     email = st.text_input ("Set Email")
st.divider()
cam_dit = st.text_area ("Campaign Details",height=200)
st.divider()
col3,col4, = st.columns(2)
with col3:
     amount =st. selectbox ("Goal amount",['$25','$40','$5','$60','$58''$40''Custom amount'],0)
if amount =='$25':
     amount = 25
if amount =='$40':
     amount = 40
if amount =='$5':
      amount = 5
if amount =='$60':
      amount = 60
if amount =='$58':
      amount = 58
if amount =='$40':
      amount = 40
if amount =='Custom amount':
   with col4:
       amount = st.number_input ("Please enter custom amount",0)
       st.divider()
with col3:
  if st.button ("Create Campaign"):
       #this creates a dict which assigns the variables to their categories in csv
       donations_dict = {'Campaign Title':[cam_title],'Campaign Email':[email],'Campaign amount':[amount]}
       st.write(donations_dict)
       #this converts the dict toa tableform dataframe
       donations_table = pd.DataFrame(donations_dict)
       st.table(donations_table)
       donations_join = pd.concat([readcsv ,donations_table])
       donations_join.to_csv('donate.csv')
       st.success("Donations campaign creatd")


if menu == "Veiw Donations":
      alltitles = readcsv['Campaign title']
      col1, col2, = st.columns(2)
      with col1
           selectitle = st.seceltbox("Choose donation to veiw",allititles)

           filtertitle = readcsv[readcsv["Campaign title"] == selectitle] #Filte
      st.table(filtertitle)
      getdetails =filtertitle ['campaign details'];loc[0]
      getemail = filtertitle['Campaign email']loc[0]

      st.div