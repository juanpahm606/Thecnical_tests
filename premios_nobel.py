''' Libs here -- please include all libs what you need below'''

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
import warnings
import pandas as pd
''' TARS Library '''

import os
import sys
__file__ = os.path.abspath(__file__)
path = os.path.dirname(__file__)
mainpath = os.path.split(path)
sys.path.append(mainpath[0])
warnings.filterwarnings("ignore")

from Dependencias.WebDriverLocal import start_browser    

def selenium(browser,downloadpath):
    #------------------------------------
    # VARIABLES DE CONFIGURACION
    #----------------------------------------------------------------------------------------------------------------------------
    url="https://es.wikipedia.org/wiki/Anexo:Ganadores_del_Premio_Nobel"
    final_path=os.path.join(path,"Final_path")

    # ----------------------------------------------------------------------------------------------------------------------------
    browser.get(url) #Entra a Wikipedia al Anexo de ganadores del Nobel
    df={'Año':[],'Física':[],'Química':[],'Medicina':[],'Literatura':[],'Paz':[],'Economía':[]} #Diccionario donde guardamos los valores
    for i in range(1,121): #Una tabla con columans para el año y cada categoría de los Nobel
        Age= WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[1]')))
        A_text=Age.text #Convierte el valor encontrado en texto, las variables tienen el nombre de cada categoría del premio Nobel
        df['Año'].append(A_text)
        Physics=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[2]')))
        P_text=Physics.text
        df['Física'].append(P_text)
        Chemistry=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[3]')))
        C_text=Chemistry.text
        df['Química'].append(C_text)
        Medicine=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[4]')))
        M_text=Medicine.text
        df['Medicina'].append(M_text)
        Literature=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[5]')))
        L_text=Literature.text
        df['Literatura'].append(L_text)
        Peace=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[6]')))
        P_text=Peace.text
        df['Paz'].append(P_text)
        Economy=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table/tbody/tr[{i}]/td[7]')))
        E_text=Economy.text
        df['Economía'].append(E_text)
    df2=pd.DataFrame.from_dict(df)#Guarda los datos en un Dataframe  
    df2.to_csv(final_path + "\\premios_nobel.csv",sep=';',index=False) #Pasamos los valores del DataFrame  a un CSV
pass






if __name__ == '__main__':
    downloadpath = os.path.join(path, "Download_path")
    mozilla_bin = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = start_browser(downloadpath, mozilla_bin)
    selenium(browser,downloadpath)