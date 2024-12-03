import streamlit as st 
from streamlit_option_menu import option_menu
from views import datapaq, home, login
import streamlit_authenticator as stauth

import pandas as pd
from datetime import datetime, timedelta
import numpy as np

import numpy.polynomial.polynomial as nppol
import matplotlib.pyplot as plt
from math import sqrt, pi, exp, log
import scipy.stats as stats
from scipy import optimize
from scipy.optimize import minimize

st.set_page_config(layout="centered")
v_menu=["Home", "Login", "Datapaq"]

with st.sidebar:

    st.header("MULTPAGE WITH OPTION MENU")

    selected = option_menu(
        menu_title=None,  # required
        options=v_menu,  # required
        icons=None,  # optional
        menu_icon="menu-down",  # optional
        default_index=0,  # optional
    )

if selected=="Home":
    home.createPage()

if selected=="Login":
    login.createPage()

if selected=="Datapaq":
    datapaq.createPage()





