# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:42:07 2019

@author: urdy9
"""

import os
import csv
import re
import pandas as pd
import numpy as np
import sqlalchemy

def leerExcel(self,name):
    #LEER DATOS DE EXCEL
    #creo directorio temporal
    try:
        os.stat("./tmp/")
    except:
        os.mkdir("./tmp/")
    #borro tmp
    if os.path.isfile("tmp/out.csv"):
        os.remove("tmp/out.csv")
    #creo csv para editar
    xmlToCsv=open("tmp/out.csv",'w',encoding='utf-8')
    csvWritter=csv.writer(xmlToCsv)
    #abro para lectura
    pr = open (name,'r')
    contenido = pr.read()
    #borro principio
    contenido = contenido[contenido.find('<Worksheet ss:Name="Carga docente por estudio">'):]
    #cojo datos iniciales
    datosIniciales=['Fecha de ejecución:</Data>','Curso académico:</Data>','Estudio:</Data>']
    paso=0
    while datosIniciales:
        contenido = contenido[contenido.find(datosIniciales.pop()):]
        contenido = contenido[contenido.find('<Data'):]
        contenido = contenido[contenido.find('>'):]
        ini=0
        fin=contenido.find('<')-1
        var=''
        var1=''
        var2=''
        for char in contenido:
            if ini > fin:
                break
            elif ini > 0:
                var+=char
            ini+=1
        if paso==0:
            codigo=False
            for c in var:
                if codigo:
                    var2+=c
                else:
                    if c=='-':
                        codigo=True
                    else:
                        var1+=c
            cg=var1
            grado=var2
            grado=grado[1:]
        elif paso ==1:
            curso=var
        else:
            fechaExe=var

        paso+=1
    paso=0
    
    #Creo cabecera y la escribo en el csv
    cabecera=['CA','Asignatura','Curso','TpVp','HDocAsig','HDocTipgr',
         'TipDoc','Grupo','Cprof','Profesor','HProfGrup','Igrup',
         'Iprof','Actas','CDS','Docencia','Resp','Macrogrupo','OfertaConjunta','CG','Grado','Anno','Fecha']
    csvWritter.writerow(cabecera)
    #preparo tabla
    contenido=contenido[contenido.find('C.A'):]
    contenido=contenido[contenido.find('<Row>'):]
    #creo variables lectura
    etiq_dict = {
            'data': re.compile(r'<Data ss:Type="......">(.*)</Data>'),
            'dataNull': re.compile(r'<Data ss:Type="String"/>'),
            }
    val_dict ={
            'value': re.compile(r'>.*</D'),
            }
    #leo datos
    linea=contenido[contenido.find('<Row'):contenido.find('</Row>')]
    while linea:
        linea_Valores=[]
        linea=contenido[contenido.find('<Row'):contenido.find('</Row>')]
        celda=linea[linea.find('<Cell'):linea.find('</Cell>')]
        while celda:
            celda=linea[linea.find('<Cell'):linea.find('</Cell>')]
            for key, etiq in etiq_dict.items():
                valor=''
                matchEt = etiq.search(celda)
                if matchEt:
                    if key=='data':
                        for keyV, val in val_dict.items():
                            matchVal=val.search(matchEt.group())
                            if matchVal:
                                for c in str(matchVal.group(0)):
                                    if c!=">" and c!="<":
                                        valor+=c
                                    elif c=='<':
                                        break
                    linea_Valores.append(valor)
            linea=linea[linea.find('</Cell>'):]
            linea=linea[linea.find('<Cell'):]
        if linea_Valores:
            linea_Valores.append(cg)
            linea_Valores.append(grado)
            linea_Valores.append(curso)
            linea_Valores.append(fechaExe)
        csvWritter.writerow(linea_Valores)
        contenido=contenido[contenido.find('</Row>'):]
        contenido=contenido[contenido.find('<Row>'):]
    #cierro
    xmlToCsv.close()
    return fechaExe

def formateoDatos(self):
    x=pd.read_csv('tmp/out.csv')
    x['Cprof'].fillna(0, inplace=True) 
    x['Profesor'].fillna('Sin asignar', inplace=True) 
    x['CA'] = x['CA'].astype(np.int)
    x['Asignatura'] = x['Asignatura'].astype(np.str) 
    x['Curso'] = x['Curso'].astype(np.int) 
    x['TpVp'] = x['TpVp'].astype(np.str) 
    x['HDocAsig'] = x['HDocAsig'].astype(np.float) 
    x['HDocTipgr'] = x['HDocTipgr'].astype(np.float) 
    x['TipDoc'] = x['TipDoc'].astype(np.int) 
    x['Grupo'] = x['Grupo'].astype(np.int) 
    x['Cprof'] = x['Cprof'].astype(np.int) 
    x['Profesor'] = x['Profesor'].astype(np.str) 
    x['HProfGrup'] = x['HProfGrup'].astype(np.float) 
    x['Igrup'] = x['Igrup'].astype(np.str) 
    x['Iprof'] = x['Iprof'].astype(np.str) 
    x['Actas'] = x['Actas'].astype(np.str) 
    x['CDS'] = x['CDS'].astype(np.str) 
    x['Docencia'] = x['Docencia'].astype(np.str) 
    x['Resp'] = x['Resp'].astype(np.str) 
    x['Macrogrupo'] = x['Macrogrupo'].astype(np.float) 
    x['OfertaConjunta'] = x['OfertaConjunta'].astype(np.float)
    x['CG'] = x['CG'].astype(np.int) 
    x['Grado'] = x['Grado'].astype(np.str) 
    x['Anno'] = x['Anno'].astype(np.str) 
    x['Fecha'] = x['Fecha'].astype(np.str)
    
    return x

def conexionDB(self):
    database_username = 'root'
    database_password = '1234'
    database_ip       = 'localhost'
    database_name     = 'datawarehouse'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                   format(database_username, database_password, 
                                                          database_ip, database_name))
    return database_connection

   

   