import streamlit as st
import pandas as pd
import numpy as np
import pyodbc

st.set_page_config(
    page_title='Home Page',
    page_icon='🏠',
    layout='wide'
)

st.title("Welcome to Vodafone Customer Churn Predictor")

multi = '''

## Introduction
This app helps to predict customer churn for Vodafone using advanced machine learning models. 

## Overview of Features
- **Data Exploration**: Explore the dataset used for analysis.
- **Historical Analysis**: View historical trends and patterns in customer churn.
- **Churn Prediction**: Predict the likelihood of customer churn based on input data.
- **Dashboard**: Visualize key metrics and insights.

## Navigation Guide
Use the sidebar to navigate to different pages such as Data, History, Predict, and Dashboard.

## User Instructions
To predict churn, go to the Predict page, enter the required customer details, and click 'Predict'.

## Benefits
- Identify customers at risk of churning.
- Make data-driven decisions to improve customer retention.
- Gain insights into factors influencing customer churn.

## About the Case Study
This app is based on a case study of Vodafone, using real-world data to understand and predict customer churn.

## Contact Information
For support or feedback, please contact us at [support@example.com](mailto:support@example.com).

'''

st.markdown(multi)