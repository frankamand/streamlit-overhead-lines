import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def catenary(a, x):
    return a * np.cosh(x/a)

st.title("Catenary Curve Plotter")

temp = st.slider("Line Temperature", -20.0, 140.0, 40.0)

tension = 150 - temp
a = tension / 10

x = np.linspace(-10, 10, 100)
l = len(x)
l
y = catenary(a, x)
fixed_height = 10
y1 = y[0] #difference from 20



d = fixed_height/y1

y = y*d
x = x + 10

sag = (y[0] - y[int(l/2)]).round(2)

"Sag:"
sag 

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Catenary Curve')
ax.set_ylim(0, 20)
ax.grid()

st.pyplot(fig)

