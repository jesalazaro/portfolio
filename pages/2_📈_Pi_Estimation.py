import streamlit as st
import numpy
from bokeh.plotting import figure
import pandas as pd

st.title("Estimating the value of $\pi$")

st.write(r"""
Estimating the value of $\pi$ using a Monte Carlo method involves randomly 
         sampling points within a square and determining how many fall within 
         a quarter circle inscribed within that square.
          The ratio of points within the quarter circle to the total 
         number of points can be used to estimate $\pi$ .
""")

st.write(r"""A step-by-step guide on how to do it:""")
st.markdown("- Consider a square with side length 2 centered at the origin (coordinates (-1, -1) to (1, 1)). Inscribe a quarter circle with radius 1 within this square, so it touches the square at the midpoint of each side.")
st.markdown("- Random Sampling: Generate a large number of random points within this square. Each point should have coordinates (x, y) where x and y are randomly chosen from the interval [-1, 1].")
st.markdown("- Check if Points Fall Within the Quarter Circle: For each generated point, check if it lies inside the quarter circle using the equation of the circle: $x^2 + y^2 <= 1$. If the point satisfies this condition, count it as inside the quarter circle.")
st.markdown("- Estimate $\pi$: Calculate the ratio of the number of points inside the quarter circle to the total number of generated points. This ratio is approximately equal to the ratio of the area of the quarter circle to the area of the square, which is π/4. Hence, multiplying this ratio by 4 gives an estimate of $\pi$.")

def main():
    N = st.slider("Number of dots?", 50, 10000, 100)
    xData = []
    yData = []
    for i in range(N):
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        if numpy.sqrt(x**2 + y**2) < 1:
            xData.append(x)
            yData.append(y)

    st.write("Value of pi: ", 4 * len(xData) / float(N))
    # p = figure(title="Pi estimation", x_axis_label="x", y_axis_label="y")
    # p.scatter(xData, yData, color="navy")
    # st.bokeh_chart(p, use_container_width=True)
    df = pd.DataFrame({'x':xData, 'y':yData})
    st.scatter_chart(
    df,
    x='x',
    y='y',
    height= 700,
    use_container_width  = True,
)

code = '''
    import pandas as pd
    
    xData = []
    yData = []
    for i in range(N):
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        if numpy.sqrt(x**2 + y**2) < 1:
            xData.append(x)
            yData.append(y)
        df = pd.DataFrame({'x':xData, 'y':yData})'''


st.code(code, language='python')


if __name__ == "__main__":
    main()
