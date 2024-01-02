from datetime import datetime
import pandas as pd
archivo="Capacitación PIDGIN\datos.xlsx"
acontecimientos=pd.read_excel(archivo)
duracion=pd.DataFrame()
def present(date):
    if date=='Presente': 
        return datetime(2023,8,4,0,0)
    else:
        return date
acontecimientos=acontecimientos.applymap(present)
acontecimientos['Fecha de Fin']=acontecimientos['Fecha de Fin'].apply(pd.Timestamp)
duracion=acontecimientos.copy()
duracion['Número de días transcurridos']=acontecimientos['Fecha de Fin']-acontecimientos['Fecha de Inicio']
duracion.to_csv("Capacitación PIDGIN\\duracion_eventos.csv",sep=',',index=False)
