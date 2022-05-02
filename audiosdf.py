import pandas as pd
import os
import subprocess


df = pd.read_excel("/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/Tipificación_Cliente_CHEC_2017_12.xlsx")
df1 = pd.read_excel("/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/DVD1-Consolidado.xlsx")
df2 = pd.read_excel("/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/DVD2-Consolidado.xlsx")



cod = df.loc[:,["CallID","Piloto","CodFinalizacion","L_Municipio"]]
dvd1 = df1.loc[:,["SEGMENTO GRABACION ID","NOMBRE DE ARCHIVO","FUENTE","RUTA DEL ARCHIVO"]]
dvd2 = df2.loc[:,["SEGMENTO GRABACION ID","NOMBRE DE ARCHIVO","FUENTE","RUTA DEL ARCHIVO"]] 

dvd1["SEGMENTO GRABACION ID"] = dvd1["SEGMENTO GRABACION ID"].fillna(0)
dvd1["SEGMENTO GRABACION ID"] = dvd1["SEGMENTO GRABACION ID"].astype(int)
dvd2["SEGMENTO GRABACION ID"] = dvd2["SEGMENTO GRABACION ID"].fillna(0)
dvd2["SEGMENTO GRABACION ID"] = dvd2["SEGMENTO GRABACION ID"].astype(int)

cod["CallID"] = cod["CallID"].fillna(0)
cod["CallID"] = cod["CallID"].astype(int)

    
faltaEnergia = (cod[df["CodFinalizacion"].isin(["FALTA ENERGIA EN EL SECTOR"])])
mn = (cod[df["L_Municipio"].isin(["Dorada"])])
pl = (cod[df["Piloto"].isin(["CHEC_ATENCIONDANOS"])])
     

fe = pd.merge(left=faltaEnergia,right=dvd1,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
fe1 = pd.merge(left=faltaEnergia,right=dvd2,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
mu =  pd.merge(left=mn,right=dvd1,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
mu1 =  pd.merge(left=mn,right=dvd2,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
pt =  pd.merge(left=pl,right=dvd1,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")
pt1 =  pd.merge(left=pl,right=dvd2,how='inner', left_on="CallID", right_on="SEGMENTO GRABACION ID")


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

rt = os.walk('/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/audios/CHEC_ATENCIONDANOS/Todos los archivos')

rutas_destino = ['/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/FaltaEnergía', '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/Dorada', '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/PilotoChec']
            

def copy(a, b):
    for ruta, dir, archivos in rt:        
        for i in archivos:
            if i in a.tolist():                           
                subprocess.run(['cp', ruta + '/' + i, b])  
    return


copy(fec, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/FaltaEnergía')
copy(fe1c, '/mnt/c/Users/Acer/Desktop/Desktop/Pruebas/prueba_audios/FaltaEnergía')
  
  
  
         
          
    
   
