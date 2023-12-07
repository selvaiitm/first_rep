
import streamlit as st
st.title('Hai welcome to my first streamlit app - Tamilselvan.N')
st.title("adding two numbers")
def addition(a,b):
  product = a+b
  return product
a = st.number_input('first:')
b = st.number_input('second:')


st.write(f"The product of {a} and {b} is: {product}")
