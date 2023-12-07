
import streamlit as st
st.title('Hai welcome to my first streamlit app - Tamilselvan.N')

def multiplication(a,b):
  return a,b

a = st.number_input('first:')
b = st.number_input('second:')

multiplication(a,b)
