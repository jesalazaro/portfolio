import streamlit as st
import random
import time


st.title("Order to Disorder")
st.write(
    "One of the most important features of the macroscopic systems is the tendency to disorder. An example  of this trend can be seen with the addition of water ink; assuming we have an ink with the same density as water, we add it to the latter carefully, after some time we know that the ink and water mixed; if we have recorded this and we reproduce it backwards we will see that the movement random of the ink molecules is going to return towards the surface of the water, our intuitive thinking tells us How nature works and we will know that something is wrong. From our experience we can say that the trend natural movement of microscopic systems towards disorder defines the direction of time, the water-ink mixture can from being described as a microscopic state. If the process continues without interruption, we will notice that the mixture has become completely homogeneous, when that state arrives,we will be talking about a state of balance"
)

st.image("images/box-particles.png", caption="Box schema")

st.write(
    r"""Let us consider an ideal gas of $N$ identical particles in where the interaction between them is negligible, which is finds himself confined in a box and isolated in such a way  that is not affected by external influences, the box is divided It is made into two sections, and this one has a hole with a grate which can be moved to allow the gas to move from one place to another as illustrated in figure, initially $n$ particles are on the left side of thebox and $n′$ on the right side of the box such that $n + n^{\prime} = N$, when the grid is removed it leaves a  space, the probability that each particle passes through thehole is the same, since the movement of each particle is independent of the others, it is assumed as a condition that only one particle passes through the hole per unit of time."""
)
st.latex(
    r"""
   \begin{equation}
\begin{aligned}
&P(8,2)=\frac{9}{10}\\
&P(10,2)=\frac{1}{10}
\end{aligned}
\end{equation}
    """
)

st.write(
    r"""
Then at $t = 2$ the average number of particles in
the left is:
"""
)

st.latex(
    r"""
\begin{equation}
\langle n\rangle=8 P(8,2)+10 P(10,2)=8,2
\end{equation}
         """
)

st.write(
    r"""
the next step of time we have $P (7, 3) =
8/10P (8, 2) = 72/100$, corresponding to even movement
of the eight particles to the left, the same
consideration applies for $P (9, 3) = 10/10P (10, 2) +
2/10P(8, 2) = 28/100$. for $t = 3$ we obtain
         """
)

st.latex(
    r""" 
\begin{equation}
\langle n\rangle=7 P(7,3)+9 P(9,3)=7,56
\end{equation}"""
)

st.write(
    r"""To solve this problem, the Monte Carlo method was used since
It is applicable for large systems and long times, in
The method generates a sample of random movements.
rios and it is assumed that the sample is representative for the
set of all possible movements, the larger
the number of particles, the more accurate the result will be,
The method requires that the probability be defined with the
that a particle passes from the left side to the right side
of the box, the probability per unit of time of a
movement from left to right equals the number of
particles on the left side in time divided by the
total number of particles, then the probability of
that the particle from left to right:"""
)
st.latex(
    r""" 
\begin{equation}
\frac{n}{N}
\end{equation}"""
)


code = """
    N = 10
    tries = 10

    tmax = 10 * N
    particles = [[0] * tries for _ in range(tmax)]
    Addition = [0] * tmax
    parti = [0] * tmax

    for v in range(1, tries + 1):
        nl = N
        for i in range(1, tmax + 1):
            probability = nl / N
            randomValues = random.random()
            if randomValues <= probability:
                nl -= 1
            else:
                nl += 1
            parti[i - 1] = nl
            particles[i - 1][v - 1] = nl

    probability_data = []

    for i in range(tmax):
        Addition[i] = sum(particles[i][:tries])
        Pro = Addition[i] / tries
        probability_data.append(Pro)"""

st.code(code, language="python")

st.write(
    r"""
    After implementing the code we have the next graph, after increasing the number of tries and particles most of the time the number between the sides of the box is
    almost the same, achieving order.
"""
)


def main():
    random.seed(time.time())
    N = st.slider("Number of particles?", 10, 500, 25)
    tries = st.slider("Number of tries?", 5, 100, 25)

    tmax = 10 * N
    particles = [[0] * tries for _ in range(tmax)]
    Addition = [0] * tmax
    parti = [0] * tmax

    for v in range(1, tries + 1):
        nl = N
        for i in range(1, tmax + 1):
            probability = nl / N
            randomValues = random.random()
            if randomValues <= probability:
                nl -= 1
            else:
                nl += 1
            parti[i - 1] = nl
            particles[i - 1][v - 1] = nl

    probability_data = []

    for i in range(tmax):
        Addition[i] = sum(particles[i][:tries])
        Pro = Addition[i] / tries
        probability_data.append(Pro)
        # st.write(f"{Pro}   {particles[i][0]}  {particles[i][1]}  {particles[i][2]}  {particles[i][3]}  {particles[i][4]}")

    st.line_chart(probability_data)


if __name__ == "__main__":
    main()
