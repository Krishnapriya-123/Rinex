import streamlit as st
import joblib

#load the joblib model
model_nb=joblib.load('googlplaystore')

st.title('googleplaystore')
ip=st.text_input('Enter:')

op=model_nb.predict([ip])
if st.button('PREDICT'):
   st.title(op[0])
   
   
       
      
      
