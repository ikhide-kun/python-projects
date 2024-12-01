import streamlit as st
bill=0
st.set_page_config(layout='wide')
st.title("book app")
boook_collections = st. selectbox("Choose any Category",["Children Books","Family Books","Christian Books","Science Books"])
st.subheader = ("Childerren boook")
child,teens,christains,family =st.columns(5)
with child:
 st.image("https://www.splashlearn.com/blog/wp-content/uploads/2024/06/jimmy-first-day-of-school.png")
 if st.checkbox("jimmys first day at school"):
 bill+=38
 st.write ('ok done')

with teens:
 st.image("https://www.google.com/aclk?sa=l&ai=DChcSEwjg1Lmw9ZOJAxVbB60GHfZgLIcYABAEGgJwdg&co=1&ase=2&gclid=Cj0KCQjwyL24BhCtARIsALo0fSCExwmgSGUD1qTRv5w6XX6BBGHcTVBEdzy3YUWAFmr73MoohMFIc2kaAmZjEALw_wcB&sig=AOD64_0DHI97DewYF9bWHKz_nG3ua3Svag&ctype=5&q=&nis=4&ved=2ahUKEwi95bWw9ZOJAxWxweYEHVs1ASMQww8oAnoECAIQEw&adurl=")
 if st.checkbox("wonder"):
 bill+=46
 st.write ('ok done')

with christains:
 st.image("https://api.bookbotkids.workers.dev/books/5f8b53ab-be71-4884-a3f5-a9b587186614/cover.jpg")
 if st.checkbox("where is my shoe?")
 bill+=67
 st.write ('ok done')

with family :
 st.image("")
 if st.checkbox("")
 bill+=58
 st.write ('ok done')