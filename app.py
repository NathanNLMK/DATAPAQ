import streamlit as st 
from streamlit_option_menu import option_menu
from views.home import createPage as createHomePage
from views.login import createPage as createLoginPage
from views.datapaq import createPage as createDatapaqPage
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
v_menu=["Login","Home", "Datapaq"]

with st.sidebar:

    selected = option_menu(
        menu_title="DATAPAQ",  # required
        options=v_menu,  # required
        icons=None,  # optional
        menu_icon="thermometer-high",  # optional
        default_index=0,  # optional
    )

if selected=="Login":
    createLoginPage()

if selected=="Home":
    createHomePage()


if selected=="Datapaq":
    createDatapaqPage()





