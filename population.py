''' Libs here -- please include all libs what you need below'''

from selenium.webdriver.common.by import By
import glob
import warnings
import pandas as pd
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
    url="https://world-statistics.org/"
    #final_path=os.path.join(path,"Final_path")
    browser.get(url)
    pop1=f"/a[2]"
    pop2=f"/a[3]"
    def Pop(pop):
        Indicators=browser.find_element(By.XPATH,f'//a[@href="index.php#indicators"]')
        Indicators.click()
        Population=browser.find_element(By.XPATH,f'//a[@id="aTopic11"]')
        Population.click()
        TotalPopulation=browser.find_element(By.XPATH,f'//div[@id="subtopic117"]/a')
        TotalPopulation.click()
        path_UN='//div[@id="list117"]'
        UN_estimates=browser.find_element(By.XPATH, path_UN + pop )
        UN_estimates.click()
    Pop(pop1)    
    countries=len(browser.find_elements(By.XPATH,f'//select[@id="selcountry"]/option'))
    south_america_list=["ARG","BOL","BRA","CHL","COL","ECU","GUY","PRY","PER","SUR","TTO","URY","VEN"]
    for i in range(1,countries):
        country_1=browser.find_element(By.XPATH,f'//select[@id="selcountry"]/option[{i}]')
        country_value=country_1.get_attribute('value')
        #print(country_value)
        for country in  south_america_list:
            if country_value==country:
                country_1.click()
                #print(country_value)
    AllLines=browser.find_element(By.XPATH,f'//div[@id="myTable_length"]/label/select/option[3]')
    AllLines.click()
    CSV=browser.find_element(By.XPATH,f'//a[@class="dt-button buttons-csv buttons-html5"]')
    CSV.click()
    namearchive="Populations/World Statistics - International StatisticsChart context menuZoom inZoom outChart context menuChart context menuChart context menuChart context menuSt. Vincen.csv"
    try:
        os.rename(namearchive,"Populations/UN19502020.csv")
    except:
        pass    
    Pop(pop2)
    Tab=browser.find_element(By.XPATH,'//i[@class="fa fa-table"]')
    Tab.click()
    for i in range(1,countries):
        country_1=browser.find_element(By.XPATH,f'//select[@id="selcountry"]/option[{i}]')
        country_value=country_1.get_attribute('value')
        #print(country_value)
        for country in  south_america_list:
            if country_value==country:
                country_1.click()
                #print(country_value) 
                AllLines=browser.find_element(By.XPATH,f'//div[@id="myTable_length"]/label/select/option[3]')
                AllLines.click()
                NoChanges=browser.find_element(By.XPATH,'//div[@class="DTFC_LeftHeadWrapper"]/table/thead/tr/th[2]/select/option[9]')
                NoChanges.click()
                CSV=browser.find_element(By.XPATH,f'//a[@class="dt-button buttons-csv buttons-html5"]')
                CSV.click()
                try:
                    os.rename(namearchive,f"Populations/UNProyection_bycountry_{i}.csv")
                except:
                    pass
                delete=browser.find_element(By.XPATH,f'//ul[@id="listcountry"]/li')
                delete.click()
    pass

def Pandas(csv_archive):
    a=1
    listoflands=glob.glob(csv_archive) 
    Lands=[]
    for land in listoflands:
        DataFrameForLand=pd.read_csv(land)
        Lands.append(DataFrameForLand) 
    UN20202100=pd.concat(Lands,ignore_index=True)
    UN20202100=UN20202100.drop("VariantConstant-fertilityConstant-mortalityHigh variantInstant-replacementLow variantMedium variantMomentumNo changeZero-migration",axis=1)
    UN20202100.to_csv('Populations/UN20202100.csv',index=False)
    UN19502020=pd.read_csv("Populations/UN19502020.csv")
    Population_final=pd.merge(UN19502020,UN20202100,on=['Country','2020'])
    Population_final.to_csv('Populations/Final_table.csv',index=False)
    os
    #Population_19502100=pd.DataFrame()
    #Population_19502100['Country']=[]
    #Population_final['Country']
    #Population_final.columns.tolist()[1:]
    #Population_19502100['Year']=[]
    #Population_19502100['Population']=[]
    pass


if __name__ == '__main__':
    downloadpath = os.path.join(path, "Populations")
    mozilla_bin = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = start_browser(downloadpath, mozilla_bin)
    selenium(browser,downloadpath)
    csv_archive="Populations/UNProyection_bycountry_*.csv"
    Pandas(csv_archive)
pass