
import streamlit as st
st.title('Hai welcome to my first streamlit app - Tamilselvan.N')
st.title("Multiplying two numbers")
def multiplication(a,b):
  product = a*b
  return product
a = st.number_input('first:')
b = st.number_input('second:')


if product:
  st.write(f"The product of {a} and {b} is: {product}")
else:
  st.write("Please enter both numbers to calculate the product.")
