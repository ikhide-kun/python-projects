import streamlit as st
st.set_page_config(layout='wide')


st.title('Eletronic order App')
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Ffr.123rf.com%2Fphoto_43149221_d%25C3%25A9finir-des-appareils-%25C3%25A9lectrom%25C3%25A9nagers-et-des-appareils-%25C3%25A9lectroniques-ic%25C3%25B4nes-isol%25C3%25A9s-vector.html&psig=AOvVaw2aZh3nQyj4xqWRyWyKRGVb&ust=1727387232821000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCODYqYeJ34gDFQAAAAAdAAAAABAR")
bill = 0
st.subheader("Home Category")
Home1,Home2,Home3,Home4= st.columns(4)


with Home1:
   if st.checkbox("gas: $60"):
    bill += 60
   st.write("Ok Done")


with Home2:
    if st.checkbox("oven: $49"):
      bill += 49
      st.write("Ok Done")


with Home3:
    if st.checkbox("tv: $85"):
      bill += 85
      st.write("Ok Done")


with Home4:
  if st.checkbox("TV : $98"):
     bill +=98
     st.write("Ok Done")