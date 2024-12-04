import streamlit as st 
import pandas as pd
import numpy as np

def calculPMT(Vbande,EpBande,TemperatureEtuve2):
    h1 =38.2902405939276
    h2 =47.61410470400322
    h3 = 27.15486032472619
    t= 9.30/(Vbande/60)
    Epbande2 = EpBande /1000
    PMT = TemperatureEtuve2 + ((TemperatureEtuve2 + ((TemperatureEtuve2 + (35-TemperatureEtuve2)*np.exp((-2*h1)*t/(Epbande2*7850*449)))-TemperatureEtuve2)*np.exp((-2*h2)*t/(Epbande2*7850*449)))-TemperatureEtuve2)*np.exp((-2*h3)*t/(Epbande2*7850*449))
    return PMT

def createPage():
    st.empty()
    st.write("# Test de la formule PMT")

    if st.session_state['authentication_status']:
        col1,col2,col3 = st.columns(3)
        with col1:
            Vbande = st.number_input("Entree la valeur voulu de vitesse : ",key="VitesseBande", value= None,placeholder="Type a number....")
        with col2:
            EpBande = st.number_input("Epaisseur de bande voulu: ",key="EpaisseurBande", value= None,placeholder="Type a number....")
        with col3:
            TemperatureEtuve2 = st.number_input("Temperature Etuve voulu : ",key="Temperature Etuve2", value= None,placeholder="Type a number....")
        if Vbande is not None and EpBande is not None and TemperatureEtuve2 is not None:
            PMT = calculPMT(Vbande,EpBande,TemperatureEtuve2)
            st.write("Voici la valeur de PMT pour les parametres renseigné:",PMT)
        else:
            st.warning("Vous devez renseigner des valeurs")
    elif st.session_state['authentication_status'] is None:
        st.warning("Il faut d'abord vous login")
    return True