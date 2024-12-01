import streamlit as st
import pandas as pd
#ALSO GOAL ACHEVIEVED AND GOAL LEF


readcsv = pd.read_csv('vote.csv')
menu = st.sidebar.selectbox("Choose an option",['Vote','View vote',])
if menu == 'Vote':
    st.subheader  (':gold [Vote] ')
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
     voter = st.text_input ("Enter Name")
    with col2:
     Country = st.selectbox ("Pick Country"['Canada','America','Nigeria'])
    st.divider()
    col3,col4 = st.columns(2)
    if Country == 'Canada':
     with col3:
      Canada =st. selectbox ("Pick Party to vote for",['Liberal Party','Conservative Party','Green Party'])
    if Country == 'America':
      with col4: 
        st.number_input ("Please enter custom amount",0)
        st.divider()
    with col3:
      if st.button ("Create Campaign"):
        #this creates a dict which assigns the variables to their categories in csv
        donations_dict = {'Campaign Title':['cam_title'],'Campaign Email':['email'],'Campaign amount':['amount'],'Campaign Details':['cam_dit']}
        st.write(donations_dict)
        #this converts the dict to a tableform dataframe
        donations_table = pd.DataFrame(donations_dict)
        #st.table(donations_table)
        #this will join the two tables together existing in csv,new from input]
        donations_join = pd.concat([readcsv,donations_table],ignore_index=True)
        donations_join.to_csv('donations.csv',index = False)
        st.success("Donation Campaign created")
if menu =="View Donations":
  st.subheader(":orange[Campaign Details]")
  alltitles = readcsv['Campaign Title']
col1,col2 = st.columns(2)
with col1:
     voter = st.text_input ("Enter Name")
with col2:
     Country = st.selectbox ("Pick Country",['Nigeria'])
     st.divider()
col3,col4 = st.columns(2)
if Country == 'Nigeria':
 with col3:
    Nigeria =st. selectbox ("Pick Party to vote for",['Liberal Party','Conservative Party','Green Party'])
    st.divider()
    with col3:
      if st.button ("Cast vote"):
        #this creates a dict which assigns the variables to their categories in csv
        vote_dict = {'Name':[voter],'Country':[Country],'Nigeria':[Nigeria],}
        st.write(vote_dict)
        #this converts the dict to a tableform dataframe
        vote_table = pd.DataFrame(vote_dict)
        st.table(vote_table)
        #this will join the two tables together existing in csv,new from input]
        vote_join = pd.concat([readcsv,vote_table],ignore_index=True)
        vote_join.to_csv('vote.csv',index = False)
        st.success("Vote Casted")
    if menu =="View vote":
     st.subheader(":orange[Votes]")
    alltitles = readcsv['Name']
    col1,col2 = st.columns(2)

    filtertitle = readcsv[readcsv ['Name'] == 'selectitle']
    st.table(filtertitle)
    getcan = filtertitle ['Nigeria'].iloc[0]

with col1:
     voter = st.text_input ("Enter Name")
with col2:
    Country = st.selectbox ("Pick Country",['Nigeria'])
    st.divider()
    col3,col4 = st.columns(2)
    if Country == 'Nigeria':
     with col3:
      Nigeria =st. selectbox ("Pick Party to vote for",['Liberal Party','Conservative Party','Green Party'])
    st.divider()
    with col3:
      if st.button ("Cast vote"):
        #this creates a dict which assigns the variables to their categories in csv
        vote_dict = {'Name':[voter],'Country':[Country],'Nigeria':[Nigeria],}
        st.write(vote_dict)
        #this converts the dict to a tableform dataframe
        vote_table = pd.DataFrame(vote_dict)
        st.table(vote_table)
        #this will join the two tables together existing in csv,new from input]
        vote_join = pd.concat([readcsv,vote_table],ignore_index=True)
        vote_join.to_csv('vote.csv',index = False)
        st.success("Vote Casted")
    if menu =="View vote":
     st.subheader(":orange[Votes]")
    alltitles = readcsv['Name']
    col1,col2 = st.columns(2)
    with col1:
      selectitle = st.selectbox ("Choose your name",alltitles)


    filtertitle = readcsv[readcsv ['Name'] == selectitle]
    st.table(filtertitle)
    getcan = filtertitle ['Nigeria'].iloc[0]
