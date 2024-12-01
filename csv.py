#allow the user to to csv
#allow user to upload and veiw an image or take a picture
#allow user to upload audio
#allow user upload aplaod audio
#allow user to upload voice
import streamlit as st
menu = st.sidebar.selectbox("Choose an option",["Upload Csv","Upload Audio","Upload Video","Upload Pictures"])
if menu == 'Upload Audio':
    UploadAudio = st.file_uploader("Upload file of choice")
    if UploadAudio:
        st.audio(UploadAudio,format="Audio/mp3")
if menu == 'Upload Video':
    UploadVideo = st.text_input("Copy and Paste video link of choice")
    if st.button('Upload It'):
     st.video(UploadVideo)
if menu == 'Upload Pictures':
   Uploadimage = st.file_uploader("Upload image of choice")
   if Uploadimage:
      st.image(Uploadimage)
import pandas as pd
if menu == 'Upload Csv':
   UploadCsv = st.file_uploader("Upload Csv of choice",type = "csv")
   if UploadCsv:
       readcsv = pd.read_csv(UploadCsv)
       st.table(readcsv)
