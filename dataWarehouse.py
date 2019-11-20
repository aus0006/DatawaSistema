# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:13:27 2019

@author: Álvaro Urdiales Santidrián
"""
import cherrypy
import os
import os.path
import pandas as pd
import func.functions as f
import sqlalchemy
from sqlalchemy.sql import text


class dataWarehouse:
   def index(self):
       output='''
       <html>
        <head>
         </head>
         <style>
         body {
                 margin-top: 15%;
                 margin-right: 25%;
                 margin-bottom: 25%;
                 margin-left: 25%;
                 
                     }
        #Cabecera {
                text-decoration: none;
                padding: 15px 70px 50px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #000000;
                 border-radius: 10px;
                 border: 2px solid #000000;
                 background-color:#D6D6D6;
                }
        #GBotones {
            margin-top: 50px;
            }
         .boton{
                 text-decoration: none;
                 padding: 10px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #ffffff;
                 border-radius: 10px;
                 border: 2px solid #000000;
        }   
        .boton:hover{
            opacity:0.8;
        }
        #b1{
            background-color: #8B3636;
        } 
        #b2{
            background-color: #764E1B;
        }
        #b3{
            background-color: #368B54;
        }
         </style>
         <body>
         <div id='Cabecera' align=center>
         <h1>DATA WAREHOUSE</h1>
             <div id='GBotones' align=center>
                 <a href="entradaDatos" class="boton" id="b1">Introducir datos</a>
                 <a href="actualizarDatos" class="boton" id="b2">Actualizar datos</a>
                 <a href="visualizarDatos" class="boton" id="b3">Visualizar datos</a>
            </div>
        </div>
       </body>
        </html>
       '''
       return output
   index.exposed = True
   
   def entradaDatos(self):
       output='''
       <html>
        <head>
         </head>
         <style>
         body {
                 margin-top: 15%;
                 margin-right: 25%;
                 margin-bottom: 25%;
                 margin-left: 25%;
                 
                     }
        #Cabecera {
                text-decoration: none;
                padding: 15px 70px 50px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #000000;
                 border-radius: 10px;
                 border: 2px solid #000000;
                 background-color:#D6D6D6;
                }
        #GBotones {
            margin-top: 50px;
            }
         .boton{
                 text-decoration: none;
                 padding: 10px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #ffffff;
                 border-radius: 10px;
                 border: 2px solid #000000;
        }   
        .boton:hover{
            opacity:0.8;
        }
        input[type=file],input[type=submit]{
                text-decoration: none;
                padding: 10px;
                font-family:"Arial Narrow", sans-serif;
                font-weight: 600;
                font-size: 20px;
                
                border-radius: 10px;
                border: 2px solid #000000;
        }   
        input[type=file],input[type=submit]:hover{
            opacity:0.8;
        }
        #b1{
            color: #ffffff;
            background-color: #8B3636;
        } 
        #a1{
            background-color: #EC9393;
        }
        #b4{
            background-color: #454260;
        }
         </style>
         <body>
         <div id='Cabecera' align=center>
         <h1>INTRODUCIR DATOS</h1>
             <div id='GBotones' align=center>
                 <form name="formulario" method="get" action="lecturaDatos">
                 <input type="file" name="name" accept=".xls,.xlsx" id="a1">
                 <input type="submit" id="b1" \>
                 </form>
            </div>
            <div>
                <p>*el archivo a seleccionar debe encontrarse en la misma ruta que el programa.</p>
            </div>
            <div id='GBotones' align=right>
                <a href="index" class="boton" id="b4">Volver</a>
            </div>
      </div>
      </body>
        </html>
       '''
       return output
   entradaDatos.exposed = True 
   
   def actualizarDatos(self):
       output='''
       <html>
        <head>
         </head>
         <style>
         body {
                 margin-top: 15%;
                 margin-right: 25%;
                 margin-bottom: 25%;
                 margin-left: 25%;
                 
                     }
        #Cabecera {
                text-decoration: none;
                padding: 15px 70px 50px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #000000;
                 border-radius: 10px;
                 border: 2px solid #000000;
                 background-color:#D6D6D6;
                }
        #GBotones {
            margin-top: 50px;
            }
         .boton{
                 text-decoration: none;
                 padding: 10px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #ffffff;
                 border-radius: 10px;
                 border: 2px solid #000000;
        }   
        .boton:hover{
            opacity:0.8;
        }
        input[type=file],input[type=submit]{
                text-decoration: none;
                padding: 10px;
                font-family:"Arial Narrow", sans-serif;
                font-weight: 600;
                font-size: 20px;
                
                border-radius: 10px;
                border: 2px solid #000000;
        }   
        input[type=file],input[type=submit]:hover{
            opacity:0.8;
        }
        #b1{
            color: #ffffff;
            background-color: #764E1B;
        } 
        #a1{
            background-color: #B99361;
        }
        #b4{
            background-color: #454260;
        }
         </style>
         <body>
         <div id='Cabecera' align=center>
         <h1>ACTUALIZAR DATOS</h1>
             <div id='GBotones' align=center>
                 <form name="formulario" method="get" action="actualizaDatos1">
                 <input type="file" name="name" accept=".xls,.xlsx" id="a1">
                 <input type="submit" id="b1" \>
                 </form>
            </div>
            <div>
                <p>*el archivo a seleccionar debe encontrarse en la misma ruta que el programa.</p>
            </div>
            <div id='GBotones' align=right>
                <a href="index" class="boton" id="b4">Volver</a>
            </div>
      </div>
      </body>
        </html>
       '''
       return output
   actualizarDatos.exposed = True
       
   
   def lecturaDatos(self,name=None):
       #salida
       output='''
               <html>
                <head>
                 </head>
                 <style>
                 body {
                         margin-top: 15%;
                         margin-right: 25%;
                         margin-bottom: 25%;
                         margin-left: 25%;
                         
                             }
                #Cabecera {
                        text-decoration: none;
                        padding: 15px 70px 50px;
                         font-family:"Arial Narrow", sans-serif;
                         font-weight: 600;
                         font-size: 20px;
                         color: #000000;
                         border-radius: 10px;
                         border: 2px solid #000000;
                         background-color:#D6D6D6;
                        }
                #GBotones {
                    margin-top: 50px;
                    }
                 .boton{
                         text-decoration: none;
                         padding: 10px;
                         font-family:"Arial Narrow", sans-serif;
                         font-weight: 600;
                         font-size: 20px;
                         color: #ffffff;
                         border-radius: 10px;
                         border: 2px solid #000000;
                }   
                .boton:hover{
                    opacity:0.8;
                }
                input[type=file],input[type=submit]{
                        text-decoration: none;
                        padding: 10px;
                        font-family:"Arial Narrow", sans-serif;
                        font-weight: 600;
                        font-size: 20px;
                        
                        border-radius: 10px;
                        border: 2px solid #000000;
                }   
                input[type=file],input[type=submit]:hover{
                    opacity:0.8;
                }
                #b1{
                    color: #ffffff;
                    background-color: #8B3636;
                } 
                #a1{
                    background-color: #EC9393;
                }
                #b4{
                    background-color: #454260;
                }
                 </style>
                 <body>
                 <div id='Cabecera' align=center>
                 <h1>INTRODUCIR DATOS</h1>
                    <div>
    '''
       #xml
       if name:
           if os.path.exists(name):
               #LEER DATOS DE EXCEL
               f.leerExcel(self,name)
               tabla=f.formateoDatos(self)
               #tablahtml=tabla.to_html()
               #GUARDAR DATOS EN BD
               conn=f.conexionDB(self)
               #CREAR DATAFRAMES POR TABLA PARA SUBIR
               dfgrado=tabla[['CG','Grado']]
               dfgrado=dfgrado.drop_duplicates(subset='CG')
               
               dfasignaturas=tabla[['CA','Asignatura', 'Curso', 'TpVp', 'HDocAsig','CG']]
               dfasignaturas= dfasignaturas.drop_duplicates(subset='CA')
               
               dfgrupo=tabla[['Grupo', 'Igrup', 'Macrogrupo', 'HDocTipgr', 'TipDoc','CA']]
               dfgrupo=dfgrupo.drop_duplicates(subset=['Grupo','CA'])
               
               dflistado=tabla[['Anno','Fecha', 'CG']]
               dflistado=dflistado.drop_duplicates(subset='Anno')
               
               dfprofesor=tabla[['Cprof','Profesor','Iprof','Actas','CDS','Docencia','Resp','OfertaConjunta']]
               dfprofesor=dfprofesor.drop_duplicates(subset='Cprof')
               
               dfhoras=tabla[['CG','Grupo','Cprof','CA','Anno','HProfGrup']]
               dfhoras=dfhoras.drop_duplicates(subset=['CG','Grupo','Cprof','CA','Anno'])
               
               try:
                   dfgrado.to_sql(con=conn, name='grados', if_exists='append',index=False)
               except:
                   output+='''
                       <p>ERROR: El grado no se ha introducido.</p>
                   '''               
               try:
                   dfasignaturas.to_sql(con=conn, name='asignaturas', if_exists='append',index=False)
               except:
                   output+='''
                       <p>ERROR: las asignaturas no se han introducido.</p>
                   '''               
               try:
                   dflistado.to_sql(con=conn, name='listados', if_exists='append',index=False)
               except:
                   output+='''
                       <p>ERROR: Los listados no se han introducido.</p>
                   '''               
               try:
                   dfgrupo.to_sql(con=conn, name='grupos', if_exists='append',index=False)
               except:
                   output+='''
                       <p>ERROR: Los grupos no se han introducido.</p>
                   '''               
               try:
                   dfprofesor.to_sql(con=conn, name='profesores', if_exists='append',index=False)
               except:
                   output+='''
                       <p>ERROR: Los profesores no se han introducido.</p>
                   '''                 
               try:
                   dfhoras.to_sql(con=conn, name='horasasignadas', if_exists='append',index=False)
               except:
                   output+='''
                       <p>ERROR: Las horas no se han introducido.</p>
                   '''               
               #BORRAR ARCHIVO TEMPORAL
               if os.path.isfile("tmp/out.csv"):
                   os.remove("tmp/out.csv")
               #salida
               output+='''
                        <p>Los datos se han leido correctamente.</p>
                    </div>
                    <div id='GBotones' align=right>
                        <!--
                        <form action="mostrarTablaIntroducida" method="get">
                        <input type="hidden" name="tablahtml"/>
                        <input type="submit" id="b1" value="Mostrar tabla" />
                        </form>
                        --->
                        <a href="index" class="boton" id="b4">Volver</a>
                    </div>
              </div>
              </body>
                </html>
               '''
               
               
           else:
                output+='''
                        <p>ERROR: El archivo no se encuentra en el mismo directorio.</p>
                    </div>
                    <div id='GBotones' align=right>
                        <a href="entradaDatos" class="boton" id="b1">Introducir datos</a>
                        <a href="index" class="boton" id="b4">Volver</a>
                    </div>
              </div>
              </body>
                </html>
               '''
       else:
           output+='''
                       <p>ERROR: No has introducido ningun archivo.</p>
                    </div>
                    <div id='GBotones' align=right>
                        <a href="entradaDatos" class="boton" id="b1">Introducir datos</a>
                        <a href="index" class="boton" id="b4">Volver</a>
                    </div>
              </div>
              </body>
                </html>
               '''
       return output
   lecturaDatos.exposed = True
   
   def actualizaDatos1(self,name=None):
       #salida
       output='''
               <html>
                <head>
                 </head>
                 <style>
                 body {
                         margin-top: 15%;
                         margin-right: 25%;
                         margin-bottom: 25%;
                         margin-left: 25%;
                         
                             }
                #Cabecera {
                        text-decoration: none;
                        padding: 15px 70px 50px;
                         font-family:"Arial Narrow", sans-serif;
                         font-weight: 600;
                         font-size: 20px;
                         color: #000000;
                         border-radius: 10px;
                         border: 2px solid #000000;
                         background-color:#D6D6D6;
                        }
                #GBotones {
                    margin-top: 50px;
                    }
                 .boton{
                         text-decoration: none;
                         padding: 10px;
                         font-family:"Arial Narrow", sans-serif;
                         font-weight: 600;
                         font-size: 20px;
                         color: #ffffff;
                         border-radius: 10px;
                         border: 2px solid #000000;
                }   
                .boton:hover{
                    opacity:0.8;
                }
                input[type=file],input[type=submit]{
                        text-decoration: none;
                        padding: 10px;
                        font-family:"Arial Narrow", sans-serif;
                        font-weight: 600;
                        font-size: 20px;
                        
                        border-radius: 10px;
                        border: 2px solid #000000;
                }   
                input[type=file],input[type=submit]:hover{
                    opacity:0.8;
                }
                #b1{
                    color: #ffffff;
                    background-color: #8B3636;
                } 
                #a1{
                    background-color: #EC9393;
                }
                #b4{
                    background-color: #454260;
                }
                 </style>
                 <body>
                 <div id='Cabecera' align=center>
                 <h1>ACTUALIZAR DATOS</h1>
                    <div>
    '''
       #xml
       if name:
           if os.path.exists(name):
               #LEER DATOS DE EXCEL
               fechaExcel=f.leerExcel(self,name)
               tabla=f.formateoDatos(self)
               conn=f.conexionDB(self)
               #comprobar que datos ya hay
               s = text(
                       "SELECT Fecha FROM horas WHERE CA = :ca AND Grupo = :gr AND Cprof = :cp AND Grado = :g AND Anno = :a")
               rs=conn.execute(s,ca=str(tabla['CA'][0]), gr=str(tabla['Grupo'][0]), cp=str(tabla['Cprof'][0]), g=str(tabla['Grado'][0]), a=str(tabla['Anno'][0])).fetchall()
               if rs:
                   datos=True
                   fechaBD=rs[0][0]
                   if fechaBD<fechaExcel:
                       output+='''
                           <p>Los datos nuevos son mas recientes.</p>
                           '''
                   elif fechaBD>fechaExcel:
                       output+='''
                           <p>Los datos de la base de datos son mas recientes.</p>
                           '''
                   else:
                       output+='''
                           <p>Los datos son de la misma fecha.</p>
                           '''
               else:
                   datos=False
                   output+='''
                           <p>No hay datos para actualizar.</p>
                           '''
               #comprobar fechas

               #salida
               output+='''
                        <p>¿Que desea hacer?</p>
                    </div>
                    <div id='GBotones' align=right>
                    '''
               if datos:
                   output+='''
                        <a href="actualizarDatos2" class="boton" id="b1">Actualizar datos BD</a>
                        '''
               output+='''
                        <a href="index" class="boton" id="b4">Volver</a>
                    </div>
              </div>
              </body>
                </html>
               '''
               
               
           else:
                output+='''
                        <p>ERROR: El archivo no se encuentra en el mismo directorio.</p>
                    </div>
                    <div id='GBotones' align=right>
                        <a href="actualizarDatos" class="boton" id="b1">Introducir datos</a>
                        <a href="index" class="boton" id="b4">Volver</a>
                    </div>
              </div>
              </body>
                </html>
               '''
       else:
           output+='''
                       <p>ERROR: No has introducido ningun archivo.</p>
                    </div>
                    <div id='GBotones' align=right>
                        <a href="actualizarDatos" class="boton" id="b1">Introducir datos</a>
                        <a href="index" class="boton" id="b4">Volver</a>
                    </div>
              </div>
              </body>
                </html>
               '''
       return output       
       
       
       return output
   actualizaDatos1.exposed = True

   def actualizarDatos2(self):
       #salida
       output='''
               <html>
                <head>
                 </head>
                 <style>
                 body {
                         margin-top: 15%;
                         margin-right: 25%;
                         margin-bottom: 25%;
                         margin-left: 25%;
                         
                             }
                #Cabecera {
                        text-decoration: none;
                        padding: 15px 70px 50px;
                         font-family:"Arial Narrow", sans-serif;
                         font-weight: 600;
                         font-size: 20px;
                         color: #000000;
                         border-radius: 10px;
                         border: 2px solid #000000;
                         background-color:#D6D6D6;
                        }
                #GBotones {
                    margin-top: 50px;
                    }
                 .boton{
                         text-decoration: none;
                         padding: 10px;
                         font-family:"Arial Narrow", sans-serif;
                         font-weight: 600;
                         font-size: 20px;
                         color: #ffffff;
                         border-radius: 10px;
                         border: 2px solid #000000;
                }   
                .boton:hover{
                    opacity:0.8;
                }
                input[type=file],input[type=submit]{
                        text-decoration: none;
                        padding: 10px;
                        font-family:"Arial Narrow", sans-serif;
                        font-weight: 600;
                        font-size: 20px;
                        
                        border-radius: 10px;
                        border: 2px solid #000000;
                }   
                input[type=file],input[type=submit]:hover{
                    opacity:0.8;
                }
                #b1{
                    color: #ffffff;
                    background-color: #8B3636;
                } 
                #a1{
                    background-color: #EC9393;
                }
                #b4{
                    background-color: #454260;
                }
                 </style>
                 <body>
                 <div id='Cabecera' align=center>
                 <h1>ACTUALIZAR DATOS</h1>
                    <div>
    '''
       #xml
       #LEER DATOS DE EXCEL
       tabla=f.formateoDatos(self)
       conn=f.conexionDB(self)
       #comprobar que datos ya hay
       s = text(
               "SELECT Fecha FROM horas WHERE CA = :ca AND Grupo = :gr AND Cprof = :cp AND Grado = :g AND Anno = :a")
       rs=conn.execute(s,ca=str(tabla['CA'][0]), gr=str(tabla['Grupo'][0]), cp=str(tabla['Cprof'][0]), g=str(tabla['Grado'][0]), a=str(tabla['Anno'][0])).fetchall()
       fechaBD=rs[0][0]
       #Borramos datos
       s = text(
               "DELETE FROM horas WHERE Fecha= :f")
       try:
           conn.execute(s,f=fechaBD).fetchall()
       except:
           sol=True
       
       #GUARDAR DATOS EN BD
       try:
           tabla.to_sql(con=conn, name='horas', if_exists='append',index=False)
       except:
           output+='''
               <p>ERROR: Los datos no se han introducido.</p>
           '''               
       #BORRAR ARCHIVO TEMPORAL
       if os.path.isfile("tmp/out.csv"):
           os.remove("tmp/out.csv")
       #salida
       output+='''
                <p>Los datos se han introducido correctamente.</p>
            </div>
            <div id='GBotones' align=right>
                <!--
                <form action="mostrarTablaIntroducida" method="get">
                <input type="hidden" name="tablahtml"/>
                <input type="submit" id="b1" value="Mostrar tabla" />
                </form>
                --->
                <a href="index" class="boton" id="b4">Volver</a>
            </div>
      </div>
      </body>
        </html>
       '''
      
       return output
       
   actualizarDatos2.exposed = True    
   
   def mostrarTablaIntroducida(self,tablahtml):
       output='''
       <html>
        <head>
         </head>
         <style>
         body {
                 margin-top: 15%;
                 margin-right: 25%;
                 margin-bottom: 25%;
                 margin-left: 25%;
                 
                     }
        #Cabecera {
                text-decoration: none;
                padding: 15px 70px 50px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #000000;
                 border-radius: 10px;
                 border: 2px solid #000000;
                 background-color:#D6D6D6;
                }
        #GBotones {
            margin-top: 50px;
            }
         .boton{
                 text-decoration: none;
                 padding: 10px;
                 font-family:"Arial Narrow", sans-serif;
                 font-weight: 600;
                 font-size: 20px;
                 color: #ffffff;
                 border-radius: 10px;
                 border: 2px solid #000000;
        }   
        .boton:hover{
            opacity:0.8;
        }
        input[type=file],input[type=submit]{
                text-decoration: none;
                padding: 10px;
                font-family:"Arial Narrow", sans-serif;
                font-weight: 600;
                font-size: 20px;
                
                border-radius: 10px;
                border: 2px solid #000000;
        }   
        input[type=file],input[type=submit]:hover{
            opacity:0.8;
        }
        #b1{
            color: #ffffff;
            background-color: #8B3636;
        } 
        #a1{
            background-color: #EC9393;
        }
        #b4{
            background-color: #454260;
        }
         </style>
         <body>
         <div id='Cabecera' align=center>
         <h1>TABLA</h1>
         '''  + tablahtml + '''
              <div id='GBotones' align=right>
             <a href="entradaDatos" class="boton" id="b1">Introducir mas datos</a>
             <a href="index" class="boton" id="b4">Volver</a>
             </div>
         </div>
         </body>
         </html>
       ''' 
       return output
       
      
   mostrarTablaIntroducida.exposed = True


   def visualizarDatos(self):
       return "En proceso"
   visualizarDatos.exposed = True
       
   
conf_path = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(conf_path, "MyProj.conf")
cherrypy.config.update(conf_path)   
cherrypy.quickstart(dataWarehouse())
