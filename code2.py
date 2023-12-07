
import streamlit as st
st.title('Hai welcome to my first streamlit app - Tamilselvan.N')
st.title("Multiplying two numbers")
def multiplication(a,b):
  return a*b
a = st.number_input('a:')
b = st.number_input('b:')

product = multiplication(a,b)
st.write(f"The product of {a} and {b} is: {product}")
