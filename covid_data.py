''' Libs here -- please include all libs what you need below'''

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import warnings
#import pandas as pd
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
    url="https://ourworldindata.org/"
    #final_path=os.path.join(path,"Final_path")
    browser.get(url) 
    #search=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//div[@class="SiteSearchNavigation"]')))
    search=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//div[@class="SiteSearchNavigation"]/input')))
    #search.click()
    search.send_keys('coronavirus')
    graphs=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//a[@href="/coronavirus"]')))
    graphs.click()
    cookies=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//button[@class="button accept"]')))
    cookies.click()
    graphs2=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//a[@href="https://ourworldindata.org/coronavirus-data-explorer"]/div/div/p')))
    graphs2.click()
    world=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//div[@class="EntitySearchResults VerticalScrollContainer"]/div')))
    world_path='//div[@class="EntitySearchResults VerticalScrollContainer"]/div'
    #for i in range(1,len(world.find_elements(By.XPATH,'//label'))):
    clear=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//div[@class="ClearSelectionButton"]')))
    clear.click()
    for i in range (1,len(world.find_elements(By.XPATH,world_path + '/label'))+1):
        country=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,world_path + f'/label[{i}]')))
        #country.click()
        country_name=country.get_attribute("data-flip-id")
        #print(country_name)
        #print(country.get_attribute("class"))
        #select=country.get_attribute("class")
        if country_name=='Colombia':
            country.click()
        # elif 'EntityPickerOption selected focused' in select:
        #     country.click()    
        elif country_name=='Brazil':
            country.click()
        elif country_name=='United Kingdom':
            country.click()
        elif country_name=='United States':
            country.click()                           
        else:
            pass
    metric=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//input[@id="react-select-2-input"]')))
    metric.click()
    metric.send_keys('Confirmed deaths')
    metric.send_keys(Keys.RETURN)
    #interval=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//form[@class="ExplorerControlBar"]/div[2]/div[2]')))
    #interval.click()
    #interval.send_keys('Weekly')
    #interval.send_keys(Keys.RETURN)
    LinearLog=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//span[@class="clickable toggleSwitch"]')))
    LinearLog.click()
    Facet=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//div[@class="FacetStrategyDropdown"]')))
    Facet.click()
    Split_country=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//div[@class="FacetStrategyOption"]')))
    Split_country.click()
    Download=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//li[@class="tab clickable icon download-tab-button"]')))
    Download.click()
    PNG=WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.XPATH,f'//button[@data-track-note="chart_download_png"]')))
    PNG.click()

if __name__ == '__main__':
    downloadpath = os.path.join(path, "Confirmed_deaths")
    mozilla_bin = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = start_browser(downloadpath, mozilla_bin)
    selenium(browser,downloadpath)
pass