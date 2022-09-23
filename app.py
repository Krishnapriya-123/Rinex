import streamlit as st
import joblib

#load the joblib model
model_nb=joblib.load('GooglPlayStore')

st.title('GOOGLE PLAYSTORE')
ip=st.text_input('Enter:')

op=model_nb.predict([ip])
if st.button('PREDICT'):
   st.title(op[0])
   
   
       
