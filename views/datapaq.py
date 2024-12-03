import streamlit as st 

import pandas as pd
from datetime import datetime, timedelta
import numpy as np

import numpy.polynomial.polynomial as nppol
import matplotlib.pyplot as plt
from math import sqrt, pi, exp, log
import scipy.stats as stats
from scipy import optimize
from scipy.optimize import minimize

 #%%DATA
df_essais1= pd.read_excel('data/Data_essais1.xlsx')
df_essais2= pd.read_excel('data/Data_essais2.xlsx')
df_essais3= pd.read_excel('data/Data_essais3.xlsx')
df_essais4= pd.read_excel('data/Data_essais4.xlsx')
df_essais5= pd.read_excel('data/Data_essais5.xlsx')
df_histo =  pd.read_hdf('data/PourTestDatapaq.h5', 'table2')
df_histo.columns= ["DateTime","Vitesse","PMTligne","PMTligne2","TempE2Z1"
                    ,"TempE2Z2","TempE2Z3","SoutirageE2"]
df_histo['MoyenneTempE2'] = (df_histo['TempE2Z1']+df_histo['TempE2Z2']+df_histo['TempE2Z3'])/3
df_histo['DateTime'] = pd.to_datetime(df_histo['DateTime'])
##Essais1
df_essais1.columns= ["Temps","Longueur","TempAir1CM","TempContact2CM"
                    ,"TempAir3Centre","TempContact4Centre","TempAir5CO","TempContact6CO"]
Tbandevoulu1 = df_essais1['TempContact4Centre'].max()
Tbande0_1 = df_essais1['TempContact4Centre'].min()
Vbande1 = 50
#TbandeVoulu par zone
filtered_dfz1 = df_essais1[df_essais1['Longueur'] == 9.25]
Tbandez1voulu = float(filtered_dfz1['TempContact4Centre'])
filtered_dfz2 = df_essais1[df_essais1['Longueur'] == 18.5]
Tbandez2voulu = float(filtered_dfz2['TempContact4Centre'])
##Essais2
df_essais2.columns= ["Temps","Longueur","TempAir1CM","TempContact2CM"
                    ,"TempAir3Centre","TempContact4Centre","TempAir5CO","TempContact6CO"]
Tbandevoulu2 = df_essais2['TempContact4Centre'].max()
Tbande0_2 = df_essais2['TempContact4Centre'].min()
Vbande2 = 50
filtered_dfe2z1 = df_essais2[df_essais2['Longueur'] == 9.25]
Tbandee2z1voulu = float(filtered_dfe2z1['TempContact4Centre'])
filtered_dfe2z2 = df_essais2[df_essais2['Longueur'] == 18.5]
Tbandee2z2voulu = float(filtered_dfe2z2['TempContact4Centre'])
##Essais3
df_essais3.columns= ["Temps","Longueur","TempAir1CM","TempContact2CM"
                    ,"TempAir3Centre","TempContact4Centre","TempAir5CO","TempContact6CO"]
Tbandevoulu3 = df_essais3['TempContact4Centre'].max()
Tbande0_3 = df_essais3['TempContact4Centre'].min()
Vbande3 = 80
filtered_dfe3z1 = df_essais3[df_essais3['Longueur'] == 9.2]
Tbandee3z1voulu = float(filtered_dfe3z1['TempContact4Centre'])
filtered_dfe3z2 = df_essais3[df_essais3['Longueur'] == 18.4]
Tbandee3z2voulu = float(filtered_dfe3z2['TempContact4Centre'])
#Essais4
df_essais4.columns= ["Temps","Longueur","TempAir1CM","TempContact2CM"
                    ,"TempAir3Centre","TempContact4Centre","TempAir5CO","TempContact6CO"]
Tbandevoulu4 = df_essais4['TempContact4Centre'].max()
Tbande0_4 = df_essais4['TempContact4Centre'].min()
Vbande4 = 50
filtered_dfe4z1 = df_essais4[df_essais4['Longueur'] == 9.25]
Tbandee4z1voulu = float(filtered_dfe4z1['TempContact4Centre'])
filtered_dfe4z2 = df_essais4[df_essais4['Longueur'] == 18.5]
Tbandee4z2voulu = float(filtered_dfe4z2['TempContact4Centre'])
#Essais5
df_essais5.columns= ["Temps","Longueur","TempAir1CM","TempContact2CM"
                    ,"TempAir3Centre","TempContact4Centre","TempAir5CO","TempContact6CO"]
Tbandevoulu5 = df_essais5['TempContact4Centre'].max()
Tbande0_5 = df_essais5['TempContact4Centre'].min()
Vbande5 = 80
filtered_dfe5z1 = df_essais5[df_essais5['Longueur'] == 9.2]
Tbandee5z1voulu = float(filtered_dfe5z1['TempContact4Centre'])
filtered_dfe5z2 = df_essais5[df_essais5['Longueur'] == 18.4]
Tbandee5z2voulu = float(filtered_dfe5z2['TempContact4Centre'])
df_histo1 = df_histo[df_histo['DateTime'].between('2024-11-21 09:38:00','2024-11-21 09:40:30')]
# Calcul de la différence de temps en secondes
df_histo1['Temps_seconds'] = (df_histo1['DateTime'] - pd.Timestamp('2024-11-21 09:38:00')).dt.total_seconds()
# Calcul longueur en m
df_histo1['Longueur']= df_histo1['Temps_seconds']*(Vbande1/60)
SoutirageMoyen_1 = df_histo1['SoutirageE2'].mean()
TempEtuve2_1 = df_histo1['MoyenneTempE2'].mean()
df_histo2 = df_histo[df_histo['DateTime'].between('2024-11-21 09:50:30','2024-11-21 09:51:42')]
# Calcul de la différence de temps en secondes
df_histo2['Temps_seconds'] = (df_histo2['DateTime'] - pd.Timestamp('2024-11-21 09:50:30')).dt.total_seconds()
# Calcul longueur en m
df_histo2['Longueur']= df_histo2['Temps_seconds']*(Vbande2/60)
SoutirageMoyen_2 = df_histo2['SoutirageE2'].mean()
TempEtuve2_2 = df_histo2['MoyenneTempE2'].mean()
df_histo3 = df_histo[df_histo['DateTime'].between('2024-11-21 10:07:05','2024-11-21 10:08:00')]
# Calcul de la différence de temps en secondes
df_histo3['Temps_seconds'] = (df_histo3['DateTime'] - pd.Timestamp('2024-11-21 10:07:05.10000')).dt.total_seconds()
# Calcul longueur en m
df_histo3['Longueur']= df_histo3['Temps_seconds']*(Vbande3/60)
SoutirageMoyen_3 = df_histo3['SoutirageE2'].mean()
TempEtuve2_3 = df_histo3['MoyenneTempE2'].mean()
df_histo4 = df_histo[df_histo['DateTime'].between('2024-11-21 10:15:00','2024-11-21 10:16:09')]
# Calcul de la différence de temps en secondes
df_histo4['Temps_seconds'] = (df_histo4['DateTime'] - pd.Timestamp('2024-11-21 10:15:00')).dt.total_seconds()
# Calcul longueur en m
df_histo4['Longueur']= df_histo4['Temps_seconds']*(Vbande4/60)
SoutirageMoyen_4 = df_histo4['SoutirageE2'].mean()
TempEtuve2_4 = df_histo4['MoyenneTempE2'].mean()
df_histo5 = df_histo[df_histo['DateTime'].between('2024-11-21 10:27:00','2024-11-21 10:28:06')]
# Calcul de la différence de temps en secondes
df_histo5['Temps_seconds'] = (df_histo5['DateTime'] - pd.Timestamp('2024-11-21 10:27:00')).dt.total_seconds()
# Calcul longueur en m
df_histo5['Longueur']= df_histo5['Temps_seconds']*(Vbande5/60)
SoutirageMoyen_5 = df_histo5['SoutirageE2'].mean()
TempEtuve2_5 = df_histo5['MoyenneTempE2'].mean()
#%%Variable
# Constantes physiques
rhoBande = 7850  # kg/m^3
CpBande = 449    # J/K/kg
LZone = 9.30*3     # m
LParZone = 9.30
#%%
epBande1 = 0.66 / 1000  # Épaisseur de la bande (convertie en mètres)
temps1 = LZone/(Vbande1/60)
temps2 = LZone/(Vbande2/60)
temps3 = LZone/(Vbande3/60)
temps4 = LZone/(Vbande4/60)
temps5 = LZone/(Vbande5/60)

#%%CalculTempBande
def tempbande(Epbande2,Pbande2,Cpbande2,Tatm2,Tbande_t02,h,t):
    tbande = Tatm2 + (Tbande_t02-Tatm2)*np.exp((-2*h)*t/(Epbande2*Pbande2*Cpbande2))
    return tbande

#%%Fonction tempbande
def tempbande_ppp(VitesseBande,TempEtuve, Tbande0, Tbandez1_0, Tbandez2_0, hppV50z1, hppV50z2, hppV50z3,df_essaisn):
    df_final = pd.DataFrame()
    if VitesseBande ==50:
        for zone in range(1, 4):
            #print(zone)
            i = 0
            time = -0.3
            longueur = -0.25 + (zone - 1) * 9.25  # Ajouter un décalage pour chaque zone
            df_zone = pd.DataFrame(columns=['TempCalc', 'Longueur'])
            
            for i in range(38):
                time += 0.3
                longueur += 0.25
                if zone == 1:
                    result = tempbande(Epbande2=epBande1, Pbande2=7850, Cpbande2=449, Tatm2=TempEtuve, Tbande_t02=Tbande0, h=hppV50z1, t=time)
                elif zone == 2:
                    result = tempbande(Epbande2=epBande1, Pbande2=7850, Cpbande2=449, Tatm2=TempEtuve, Tbande_t02=df_final.loc[37,'TempCalc'], h=hppV50z2, t=time)
                elif zone == 3:
                    #print("jsuis zone3 v50")
                    result = tempbande(Epbande2=epBande1, Pbande2=7850, Cpbande2=449, Tatm2=TempEtuve, Tbande_t02=df_final.loc[75,'TempCalc'], h=hppV50z3, t=time)
                
                df_zone.loc[i + (zone-1)*38, 'TempCalc'] = result  # Mise à jour de l'indice pour continuer après la fin du dernier zone
                df_zone.loc[i + (zone-1)*38, 'Longueur'] = longueur
    
            df_final = pd.concat([df_final, df_zone], ignore_index=True)
            df_final=df_final.drop_duplicates(subset=['Longueur'])
            df_final_all =df_final.merge(df_essaisn,how='inner',on='Longueur')
            df_final_all['Erreur']=abs(df_final_all['TempCalc']-df_final_all['TempContact4Centre'])
            crit1= sum(df_final_all['Erreur']**2)
    elif VitesseBande==80 :
        for zone in range(1, 4):
            i = 0
            time = -0.3
            longueur = -0.40 + (zone - 1) * 9.2  # Ajouter un décalage pour chaque zone
            df_zone = pd.DataFrame(columns=['TempCalc', 'Longueur'])
            
            for i in range(24):
                time += 0.3
                longueur += 0.40
                if zone == 1:
                    result = tempbande(Epbande2=epBande1, Pbande2=7850, Cpbande2=449, Tatm2=TempEtuve, Tbande_t02=Tbande0, h=hppV50z1, t=time)
                elif zone == 2:
                    result = tempbande(Epbande2=epBande1, Pbande2=7850, Cpbande2=449, Tatm2=TempEtuve, Tbande_t02=df_final.loc[23,'TempCalc'], h=hppV50z2, t=time)
                elif zone == 3:
                    #print("jsuis zone3 v80")
                    result = tempbande(Epbande2=epBande1, Pbande2=7850, Cpbande2=449, Tatm2=TempEtuve, Tbande_t02=df_final.loc[47,'TempCalc'], h=hppV50z3, t=time)
                
                df_zone.loc[i + (zone-1)*23, 'TempCalc'] = result  # Mise à jour de l'indice pour continuer après la fin du dernier zone
                df_zone.loc[i + (zone-1)*23, 'Longueur'] = longueur
                df_zone.loc[i + (zone - 1) * 23, 'Longueur'] = round(df_zone.loc[i + (zone - 1) * 23, 'Longueur'],2)  # Arrondir à deux décimales

            df_final = pd.concat([df_final, df_zone], ignore_index=True)
            df_final=df_final.drop_duplicates(subset=['Longueur'])
            df_final_all =df_final.merge(df_essaisn,how='inner',on='Longueur')
            df_final_all['Erreur']=abs(df_final_all['TempCalc']-df_final_all['TempContact4Centre'])
            crit1= sum(df_final_all['Erreur']**2)
    return df_final,df_final_all,crit1



#%% Fonction objective globale pour l'optimisation
def objective_function_global(h_values,essais_config):
    hppV50z1, hppV50z2, hppV50z3 = h_values
    total_error = 0
    
    # Calculer l'erreur totale sur tous les essais pour ces valeurs de h
    for config in essais_config:
        df_final, df_final_all, crit1 = tempbande_ppp(config['Vbande'], config['TempEtuve'], config['Tbande0'], config['Tbandez1_0'], config['Tbandez2_0'], hppV50z1, hppV50z2, hppV50z3, config['df'])
        total_error += crit1
    
    return total_error



def run_calculbesth():
    # Dictionnaire regroupant les configurations par essai
    essais_config = [
        {'df': df_essais1, 'Vbande': Vbande1, 'TempEtuve': TempEtuve2_1, 'Tbande0': Tbande0_1, 'Tbandez1_0': Tbandez1voulu, 'Tbandez2_0': Tbandez2voulu},
        {'df': df_essais2, 'Vbande': Vbande2, 'TempEtuve': TempEtuve2_2, 'Tbande0': Tbande0_2, 'Tbandez1_0': Tbandee2z1voulu, 'Tbandez2_0': Tbandee2z2voulu},
        {'df': df_essais3, 'Vbande': Vbande3, 'TempEtuve': TempEtuve2_3, 'Tbande0': Tbande0_3, 'Tbandez1_0': Tbandee3z1voulu, 'Tbandez2_0': Tbandee3z2voulu},
        {'df': df_essais4, 'Vbande': Vbande4, 'TempEtuve': TempEtuve2_4, 'Tbande0': Tbande0_4, 'Tbandez1_0': Tbandee4z1voulu, 'Tbandez2_0': Tbandee4z2voulu},
        {'df': df_essais5, 'Vbande': Vbande5, 'TempEtuve': TempEtuve2_5, 'Tbande0': Tbande0_5, 'Tbandez1_0': Tbandee5z1voulu, 'Tbandez2_0': Tbandee5z2voulu}
    ]
    # Valeurs initiales pour h
    h_initial = [30, 30, 30]  # Valeurs arbitraires, à ajuster selon vos observations préliminaires
    
    # Optimisation des coefficients h pour toutes les zones et tous les essais
    result = minimize(objective_function_global, h_initial, args=essais_config,method='BFGS')

    optimized_h_values = result.x
    print("Optimized h values :", optimized_h_values)


    return optimized_h_values

optimized_h_values=run_calculbesth()



#%% GRAPH ET STATS POUR CHAQUE ESSAIS


def graph_calc_reel1DF(dfcalc,dfreel):
    fig, ax = plt.subplots()
    dfreel = dfreel[dfreel['Longueur']<28]
    ax.scatter(dfreel['Longueur'],dfreel['TempContact4Centre'],color = 'red', marker='o', alpha=.5,label='reel')
    ax.scatter(dfcalc['Longueur'],dfcalc['TempCalc'],color = 'blue', marker='o', alpha=.5,label='calc1')
    ax.set_xlabel(r'Longueur')
    ax.set_ylabel(r'TempContact')
    ax.legend()
    st.pyplot(fig)
    return fig



#%% Calcul erreur :
    
def stats_essais(dfcalc,dfreel):
    statsdf = pd.DataFrame(columns=['Longueur','Calc','Reel','Diff'])
    statsdf['Longueur']= dfcalc['Longueur']
    statsdf['Calc']= dfcalc['TempCalc']
    statsdf['Reel']= dfreel['TempContact4Centre']
    statsdf['Diff']= abs(statsdf['Calc']-statsdf['Reel'])
    statsdf['ErreurPourcent']= (statsdf['Diff']*100)/statsdf['Reel']
    statsdf[["Longueur","Calc","Reel","Diff","ErreurPourcent"]]=statsdf[["Longueur","Calc","Reel","Diff","ErreurPourcent"]].apply(pd.to_numeric)
    statsdf= statsdf[statsdf['Longueur']>2]  ##SUPRIMER CA SI ON VEUT TOUT 
    stat = statsdf.describe()
    return statsdf,stat




#%% Histogramme erreur

def HistogrammeErreur(dfstatsessaisx):
    #Histogramme Erreur
    # Création de la figure et des axes
    fig, ax = plt.subplots(figsize=(10, 6))
    # Utilisation des méthodes sur l'objet 'ax'
    ax.hist(dfstatsessaisx['Diff'], bins=10, alpha=0.5, label='Erreur1', color='Blue')
    ax.hist(dfstatsessaisx['ErreurPourcent'], bins=28, alpha=0.5, label='Erreur1Pourcent', color='Red')
    ax.legend()  # Ajout de légendes via 'ax'
    st.pyplot(fig)  # Affichage de la 

def ErreurEnFonctionLongueur(dfstatsessaisx):
    fig, ax = plt.subplots()
    ax.scatter(dfstatsessaisx['Longueur'],dfstatsessaisx['Diff'],color = 'blue', marker='o', alpha=.5,label='Erreur')
    ax.scatter(dfstatsessaisx['Longueur'],dfstatsessaisx['ErreurPourcent'],color = 'red', marker='o', alpha=.5,label='ErreurPourcent')
    ax.set_xlabel(r'Longueur')
    ax.set_ylabel(r'Erreur')
    ax.legend()
    st.pyplot(fig)
    


def Run_graph(essai_index,optimized_h_values):
    essais_config = {
        1: {'df': df_essais1, 'Vbande': Vbande1, 'TempEtuve': TempEtuve2_1, 'Tbande0': Tbande0_1, 'Tbandez1_0': Tbandez1voulu, 'Tbandez2_0': Tbandez2voulu},
        2: {'df': df_essais2, 'Vbande': Vbande2, 'TempEtuve': TempEtuve2_2, 'Tbande0': Tbande0_2, 'Tbandez1_0': Tbandee2z1voulu, 'Tbandez2_0': Tbandee2z2voulu},
        3: {'df': df_essais3, 'Vbande': Vbande3, 'TempEtuve': TempEtuve2_3, 'Tbande0': Tbande0_3, 'Tbandez1_0': Tbandee3z1voulu, 'Tbandez2_0': Tbandee3z2voulu},
        4: {'df': df_essais4, 'Vbande': Vbande4, 'TempEtuve': TempEtuve2_4, 'Tbande0': Tbande0_4, 'Tbandez1_0': Tbandee4z1voulu, 'Tbandez2_0': Tbandee4z2voulu},
        5: {'df': df_essais5, 'Vbande': Vbande5, 'TempEtuve': TempEtuve2_5, 'Tbande0': Tbande0_5, 'Tbandez1_0': Tbandee5z1voulu, 'Tbandez2_0': Tbandee5z2voulu}
    }
    config = essais_config[essai_index]
    df_tempbande, df_final_all, crit = tempbande_ppp(config['Vbande'], config['TempEtuve'], config['Tbande0'], config['Tbandez1_0'], config['Tbandez2_0'], optimized_h_values[0], optimized_h_values[1], optimized_h_values[2], config['df'])

    # Affichage des graphiques
    graph_calc_reel1DF(df_tempbande, config['df'])
    df_stats, stats = stats_essais(df_tempbande, config['df'])
    HistogrammeErreur(df_stats)
    ErreurEnFonctionLongueur(df_stats)

    return df_tempbande, df_final_all, crit, df_stats, stats, config

def createPage():
    if st.session_state['authentication_status'] is None:
        st.write("Il faut d'abord vous login pour voir les resultats")
    else:
        st.write("H calculé pour la zone 1 = ", optimized_h_values[0])
        st.write("H calculé pour la zone 2 = ", optimized_h_values[1])
        st.write("H calculé pour la zone 3 = ", optimized_h_values[2])
        essais = st.selectbox("Choix de l'essais a visualiser",(1,2,3,4,5))
        print(essais)
        dftempband1,dfall1,crittt1,dfstats1,statssss1, confiiig1=Run_graph(essais,optimized_h_values)
    return True