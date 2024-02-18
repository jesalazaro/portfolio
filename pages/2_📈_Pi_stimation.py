import streamlit as st
import numpy
from bokeh.plotting import figure


st.title("Estimating the value of pi")

def main():
    N = st.slider("Number of dots?", 50, 5000, 100)
    xData = []
    yData = []
    for i in range(N):
        x = numpy.random.uniform(-1, 1)
        y = numpy.random.uniform(-1, 1)
        if numpy.sqrt(x**2 + y**2) < 1:
            xData.append(x)
            yData.append(y)

    st.write('Value of pi: ') 
    st.write(4 * len(xData)/float(N))
    p = figure(title='Pi estimation', x_axis_label='x', y_axis_label='y')
    p.scatter(xData ,yData , color='navy')
    st.bokeh_chart(p, use_container_width=True)
    



if __name__ == "__main__":
    main()
