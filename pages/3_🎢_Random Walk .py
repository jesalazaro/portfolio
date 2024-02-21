import streamlit as st
import numpy
import pandas as pd
import random

st.title("Random walk")

st.write(r"""A random walk is a mathematical concept that describes a path consisting of a succession of random steps. It has applications in various fields such as physics, economics, finance, and computer science.
In its simplest form, a one-dimensional random walk takes place on a line, where at each step, the walker randomly moves either left or right with equal probability. This can be represented as a sequence of steps, where each step is determined by a random variable.
Random walks can be generalized to higher dimensions and can involve different types of steps with various probabilities. They are often used to model phenomena where randomness plays a significant role, such as the movement of particles in a fluid, the stock market fluctuations, or the behavior of a gambler.
Random walks have interesting properties, such as the tendency to spread out over time, the possibility of returning to the starting point (depending on the dimensionality and other factors), and the emergence of patterns despite the randomness of individual steps. They are extensively studied in probability theory and have practical applications in modeling real-world processes.""")

st.header("One-dimensional random walk ")

st.write(r"""A one-dimensional random walk is a mathematical model that describes the movement of a particle along a straight line,
          where the particle can randomly move to the left or right with equal probability. """)

st.write("Here's a basic description of how a one-dimensional random walk works:")

st.markdown("- Starting Point: The particle starts at an initial position, often denoted as position $0$ on the line.")
st.markdown("- Random Steps: At each time step, the particle can move to the left (negative direction) or to the right (positive direction) with equal probability. The size of each step is usually assumed to be constant.") 
st.markdown("- Discrete Time: The process is typically modeled in discrete time, meaning that the particle makes its moves at distinct time intervals.")


st.write("The position of the particle after $n$ steps can be represented as a sum of random variables:")

st.latex(
    r""" 
\begin{equation}
X_n = X_0 + S_1 + S_2 + ... + S_n
\end{equation}"""
)

st.write("Where $X_n$ is the position after n steps. $X_0$ is the initial position. $S_n$ represents the n-th step taken by the particle.")
st.write("the $S_n$ are independent and identically distributed random variables, typically following a Bernoulli distribution with equal probability for left and right steps.")

st.write(r"""Properties of a one-dimensional random walk include the fact that it is recurrent (the particle will eventually return to any position with probability 1. And that the expected displacement grows linearly with the number of steps """)

st.latex(
    r""" 
\begin{equation}
E[X_n] = n \cdot E[S_n]
\end{equation}"""
)

st.write(r"""One interesting aspect of one-dimensional random walks is that although the expected displacement grows linearly, the mean square displacement grows proportionally to the square root of the number of steps""")

st.latex(
    r""" 
\begin{equation}
E[X_n^2] = n \cdot E[S_n^2]
\end{equation}"""
)

st.write(r""" leading to diffusive behavior. This diffusive behavior has connections to various physical phenomena, such as Brownian motion. """)
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