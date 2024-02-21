import streamlit as st
import numpy
from bokeh.plotting import figure
import pandas as pd
import random

st.title("Random walk")

st.write(r"""A random walk is a mathematical concept that describes a path consisting of a succession of random steps. It has applications in various fields such as physics, economics, finance, and computer science.
In its simplest form, a one-dimensional random walk takes place on a line, where at each step, the walker randomly moves either left or right with equal probability. This can be represented as a sequence of steps, where each step is determined by a random variable.
Random walks can be generalized to higher dimensions and can involve different types of steps with various probabilities. They are often used to model phenomena where randomness plays a significant role, such as the movement of particles in a fluid, the stock market fluctuations, or the behavior of a gambler.
Random walks have interesting properties, such as the tendency to spread out over time, the possibility of returning to the starting point (depending on the dimensionality and other factors), and the emergence of patterns despite the randomness of individual steps. They are extensively studied in probability theory and have practical applications in modeling real-world processes.""")


steps = st.slider("Number of steps?", 10, 1000, 25)

position = 0
trajectory = [position]

for _ in range(steps):
    # Randomly choose whether to move left or right
    step = random.choice([-1, 1])
    position += step
    trajectory.append(position)


st.line_chart(trajectory)


stepsTwo = st.slider("Number of steps two dimensions?", 10, 1000, 25)

x = 0
y = 0
trajectory_x = [x]
trajectory_y = [y]

for _ in range(stepsTwo):
    # Randomly choose a direction (up, down, left, or right)
    direction = random.choice(['up', 'down', 'left', 'right'])
    
    if direction == 'up':
        y += 1
    elif direction == 'down':
        y -= 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1
    
    trajectory_x.append(x)
    trajectory_y.append(y)

df = pd.DataFrame({'x':trajectory_x, 'y':trajectory_y})
st.scatter_chart(
df,
x='x',
y='y',
height= 700,
use_container_width  = True,)    