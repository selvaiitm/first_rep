
import streamlit as st
st.title('Hai welcome to my first streamlit app - Tamilselvan.N')
st.title("Multiplying two numbers")
def multiplication(a,b):
  return a*b
a = st.number_input('Enter the first number:')
b = st.number_input('Enter the second number:')

product = multiplication(a,b)
st.write(f'The first number is {a}')
st.write(f'The first number is {b}')

st.write(f"The product of {a} and {b} is: {product}")
st.line_chart(a)
