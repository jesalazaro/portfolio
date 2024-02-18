import streamlit as st
import numpy
from bokeh.plotting import figure


st.title("Estimating the value of pi")

def main():
    N = 10_000
    xData = []
    yData = []
    for i in range(N):
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        if numpy.sqrt(x**2 + y**2) < 1:
            xData.append(x)
            yData.append(y)
    print(xData)
    p = figure(title='Pi estimation', x_axis_label='x', y_axis_label='y')
    p.scatter(xData ,yData , color='navy', alpha=0.5)
    st.bokeh_chart(p)

if __name__ == "__main__":
    main()
