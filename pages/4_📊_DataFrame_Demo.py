import streamlit as st
import tensorflow as tf
import pandas as pd
import altair as alt
from urllib.error import URLError
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


st.set_page_config(page_title="DataFrame Demo", page_icon="📊")
st.title("Deep learning classification Cancer Data")

df_cancer = pd.read_csv("Datasets/Cancer_Data.csv")
st.write(df_cancer)

null_values = df_cancer.isnull().sum()

st.write(null_values)
df_cancer=df_cancer.drop(['Unnamed: 32' ,'id'], axis=1)


label_encoder= LabelEncoder()
df_cancer['diagnosis']=label_encoder.fit_transform(df_cancer['diagnosis'])

test = df_cancer['diagnosis'].value_counts()

st.write(test)


# Calculate the correlation matrix
correlation_matrix = df_cancer.corr()

# Extract the correlation of features with the target variable
correlation_cancer_target = correlation_matrix['diagnosis']

# Filter correlations greater than 0.5
corr_target_best = correlation_cancer_target[correlation_cancer_target > 0.5]

st.write(corr_target_best)

st.bar_chart(corr_target_best)