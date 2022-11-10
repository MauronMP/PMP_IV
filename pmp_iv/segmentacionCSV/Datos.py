#!/usr/bin/env python
# coding: utf-8

# # Obtención de los datos.

# In[3]:


import pandas as pd
import numpy as np

class Datos():
    
    def __init__(self):
        self.df = pd.read_csv('/home/mauron/Dropbox/UGR/IV/data/incendiosForestales.csv')
        
    def getDF(self):
        return self.df
    
    def filtrar_mes_dia(self,args_list):
        df = self.df
        constraints = []
        for a in args_list:
            col = a[0]
            symbol = a[1]
            value = a[2]
            constraint = "(df.{}{}{})".format(col, symbol, value)
            constraints.append(constraint)
            
        filter_str = "&".join(constraints)

        return df[eval(filter_str)]
    
    def filtrarViento(self,args_list):
        df = self.filtrar_mes_dia(args_list)
        df = df[['X','Y','month','day','wind']]
        filtrado = df.sort_values('wind', ascending=False).drop_duplicates(['X', 'Y']).sort_index()
        return filtrado
    
    def diagramaDispersion(self):
        df = self.df
        df['Log-area']=np.log10(df['area']+1)
        for i in df[['FFMC', 'DMC', 'DC']].describe():
            muestra = df.plot.scatter(i,'Log-area',grid=True)
            muestra.figure.savefig('/home/mauron/Dropbox/UGR/IV/output/diagramaDispersion/'+i+'.png',dpi=200)
        return len(df[['FFMC', 'DMC', 'DC','ISI']].columns)

