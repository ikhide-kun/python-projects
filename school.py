import streamlit as st


st.title('Student database App')

menu = st.sidebar.selectbox('Menu',['Input scores', 'Scores Database'])

if menu == 'Input scores':

        name = st.text_input('please enter student name')

        col1, col2, = st.columns(2)

        with col1:
            phy = st.number_input("Enter your phy score",0)
            eng = st.number_input("Enter your eng score",0)
            math = st.number_input("Enter your math score",0)
            french = st.number_input("Enter your french score",0)
        with col2:    
            art = st.number_input("Enter your art score",0)
            his = st.number_input("Enter your his score",0)
            sci = st.number_input("Enter your sci score",0)
            geo = st.number_input("Enter your geo score",0)

        Total = phy + eng + math + french + art + his + sci + geo

        ave = Total/6

        if ave >= 90:
            grae = 'A'

        elif ave >= 85:
            grade = 'B+'

        elif ave >= 80:
            grade = 'B-'

        elif ave >= 75:
            grade = 'B'

        elif ave >= 70:
            grade = 'C+'

        elif ave >= 65:
            grade = 'C-'

        elif ave >= 60:
            grade = 'C'

        elif ave >= 50:
            grade = 'D'



        if st.button ("save student scores"):
            st.write ("name","your Total score is","Total","Average average is Good job!!!")
           