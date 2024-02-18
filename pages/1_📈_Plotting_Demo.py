import streamlit as st
import random
import time

def main():
    random.seed(time.time())
    N = st.slider('Number of particles?', 0, 1000, 25)
    intentos = st.slider('Number of tries?', 0, 130, 25)

    tmax = 10 * N
    Particulas = [[0] * intentos for _ in range(tmax)]
    Suma = [0] * tmax
    parti = [0] * tmax

    for v in range(1, intentos + 1):
        nl = N
        for i in range(1, tmax + 1):
            probabilidad = nl / N
            aleatorio = random.random()
            if aleatorio <= probabilidad:
                nl -= 1
            else:
                nl += 1
            parti[i - 1] = nl
            Particulas[i - 1][v - 1] = nl

    probability_data = []

    for i in range(tmax):
        Suma[i] = sum(Particulas[i][:intentos])
        Pro = Suma[i] / intentos
        probability_data.append(Pro)
        # st.write(f"{Pro}   {Particulas[i][0]}  {Particulas[i][1]}  {Particulas[i][2]}  {Particulas[i][3]}  {Particulas[i][4]}")
 
    st.line_chart(probability_data)

if __name__ == "__main__":
    main()
