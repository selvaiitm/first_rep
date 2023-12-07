import matplotlib.pyplot as plt
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
data = []
data.append(a)
data.append(b)
data.append(product)

# st.write( f'{data}' )
st.line_chart(data)
st.bar_chart(data)


plt.plot(a, b)

# Customize the plot
plt.xlabel('A')
plt.ylabel('B')
plt.title('Simple Line Plot')

# Display the plot in Streamlit
st.pyplot(plt)
