from audioop import mul
from operator import index
from xmlrpc.client import MultiCall
import pandas as pd
import numpy as np
import os
import shutil
import subprocess
df = pd.read_excel("/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/Tipificación_Cliente_CHEC_2017_12.xlsx")
df1 = pd.read_excel("/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/DVD1-Consolidado.xlsx")
df2 = pd.read_excel("/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/DVD2-Consolidado.xlsx")


# cod = df["CodFinalizacion"].unique()
# print(cod, len(cod))

# for i in cod:
#     a = df[df["CodFinalizacion"].str.contains(i)]
#     print(a, len(a))

cod = df.loc[:,["CallID","Piloto","CodFinalizacion","L_Municipio"]]
dvd1 = df1.loc[:,["SEGMENTO GRABACION ID","NOMBRE DE ARCHIVO","FUENTE","RUTA DEL ARCHIVO"]]
dvd2 = df2.loc[:,["SEGMENTO GRABACION ID","NOMBRE DE ARCHIVO","FUENTE","RUTA DEL ARCHIVO"]] 

dvd1["SEGMENTO GRABACION ID"] = dvd1["SEGMENTO GRABACION ID"].fillna(0)
dvd1["SEGMENTO GRABACION ID"] = dvd1["SEGMENTO GRABACION ID"].astype(int)
dvd2["SEGMENTO GRABACION ID"] = dvd2["SEGMENTO GRABACION ID"].fillna(0)
dvd2["SEGMENTO GRABACION ID"] = dvd2["SEGMENTO GRABACION ID"].astype(int)

cod["CallID"] = cod["CallID"].fillna(0)
cod["CallID"] = cod["CallID"].astype(int)

# for i in cod:
#     a = df[df["CodFinalizacion"].str.contains(i)]
#     if i == "FALTA ENERGIA EN EL SECTOR":
#         print(a)
# print(dvd2)
    
faltaEnergia = (cod[df["CodFinalizacion"].isin(["FALTA ENERGIA EN EL SECTOR"])])
mn = (cod[df["L_Municipio"].isin(["Dorada"])])
pl = (cod[df["Piloto"].isin(["CHEC_ATENCIONDANOS"])])
# dvd_1 = (dvd1[df1["FUENTE"].isin(["AVAYA"])])


# dvd_1["SEGMENTO GRABACION ID"] = dvd_1["SEGMENTO GRABACION ID"].fillna(0)
# dvd_1["SEGMENTO GRABACION ID"] = dvd_1["SEGMENTO GRABACION ID"].astype(int)


# fe = faltaEnergia.to_excel("falta Energia.xlsx")
# fe1 = mn.to_excel("Municipio.xlsx")
# fe2 = pl.to_excel("Piloto.xlsx")
# dv1 = dvd_1.to_excel("dvd_1.xlsx")
# print(dvd_1.head)

# print(faltaEnergia.dtypes)
# print(dvd_1.dtypes)


# for i in faltaEnergia.index:
#     a = faltaEnergia['CallID'][i]
#     # print(a)
    
# for j in dvd1.index:
#     b = dvd1['SEGMENTO GRABACION ID'][j]
#     print(b)
    
        
    
         
    
    
    # for j in dvd1.index:
        
            
# def merge(left, right, how, left_on, right_on):    
#     pd.merge(left=,right=,how=, left_on=, right_on=)
#     return
     

fe = pd.merge(left=faltaEnergia,right=dvd1,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
fe1 = pd.merge(left=faltaEnergia,right=dvd2,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
mu =  pd.merge(left=mn,right=dvd1,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
mu1 =  pd.merge(left=mn,right=dvd2,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
pt =  pd.merge(left=pl,right=dvd1,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
pt1 =  pd.merge(left=pl,right=dvd2,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")

# rute = '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/CHEC_ATENCIONDANOS'

def tr(var):
    for column, contenido in var.items():
        if  column == 'NOMBRE DE ARCHIVO':
            a = contenido
    return a

fec = tr(fe)
fe1c = tr(fe1)
muc = tr(mu)
mu1c = tr(mu1)
ptc = tr(pt)
pt1c = tr(pt1)

lista = [fec, fe1c, muc, mu1c, ptc, pt1c]
# print(type(fec))
# os.mkdir('FaltaEnergía')

# dir = os.listdir('/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/CHEC_ATENCIONDANOS')
# print (dir)


rt = os.walk('/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/CHEC_ATENCIONDANOS/Todos los archivos')

rutas_destino = ['/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/FaltaEnergía', '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/Dorada', '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/PilotoChec']

for ruta, dir, archivos in rt:        
    for i in archivos:
        if i in fec.tolist():                           
            subprocess.run(['cp', ruta + '/' + i, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/FaltaEnergía'])  
            
            

for ruta, dir, archivos in rt:        
    for i in archivos:
        if i in fe1c.tolist():                           
            subprocess.run(['cp', ruta + '/' + i, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/FaltaEnergía'])  
              
            
for ruta, dir, archivos in rt:        
    for i in archivos:
        if i in muc.tolist():                           
            subprocess.run(['cp', ruta + '/' + i, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/Dorada'])  
            
for ruta, dir, archivos in rt:        
    for i in archivos:
        if i in mu1c.tolist():                           
            subprocess.run(['cp', ruta + '/' + i, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/Dorada'])      
            
for ruta, dir, archivos in rt:        
    for i in archivos:
        if i in ptc.tolist():                           
            subprocess.run(['cp', ruta + '/' + i, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/PilotoChec'])  
            
for ruta, dir, archivos in rt:        
    for i in archivos:
        if i in pt1c.tolist():                           
            subprocess.run(['cp', ruta + '/' + i, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/PilotoChec'])      
            



  
  
  
    # copy(fe1c, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/FaltaEnergía')
    # copy(muc,'/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/Dorada')
    # copy(mu1c,'/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/Dorada')
    # copy(ptc,'/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/PilotoChec')
    # copy(pt1c,'/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/PilotoChec')     
            # print(i)
    # dir_names = archivos
    # print(dir_names)
    
   
# dir = list(Path('/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/CHEC_ATENCIONDANOS').iterdir())
# print(dir)

# dv1 = fe1.to_excel("Fe1.xlsx")

# dv1 = mu.to_excel("mu.xlsx")
# dv1 = mu1.to_excel("mu1.xlsx")
# dv1 = pt.to_excel("pt.xlsx")
# dv1 = pt1.to_excel("pt1.xlsx")