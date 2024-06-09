import streamlit as st
import pandas as pd
import numpy as np
import pyodbc

st.set_page_config(
    page_title='Predict Page',
    page_icon='🤖',
    layout='wide'
)

st.title("Predict Customer Churn")