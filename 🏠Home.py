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