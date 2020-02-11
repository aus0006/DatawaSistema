# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 14:56:50 2020

@author: urdy9
"""

def enlace(url, id, label):
  return '<a href="' + url + '" class="boton" id="' + id + '">' + label + '</a>'

def errorBorrado(self, tabla):
    return  '''
               <p>ERROR: Los datos de 
               ''' +tabla+ '''
               no se han borrado.</p>
               ''' 

def errorIntro(self, tabla):
    return  '''
               <p>ERROR: Los datos de 
               ''' +tabla+ ''' 
               no se han introducido.</p>
               ''' 
def errorAct(self, tabla):
    return  '''
               <p>ERROR: Los nuevos datos de 
               ''' +tabla+ ''' 
               no se han introducido.</p>
               ''' 

def css(self):
    return'''
    <html>
        <head>
         </head>
         <style>
         body {
                 display:block;
                 margin-top: 15%;
                 margin-right: auto;
                 margin-bottom: 15%;
                 margin-left: auto;
                 
                 
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
                 vertical-align: middle;
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
                color: #ffffff;
                border-radius: 10px;
                border: 2px solid #000000;
        }   
        input[type=file],input[type=submit]:hover{
            opacity:0.8;
        }
        input[type=text],input[type=submit]{
                text-decoration: none;
                padding: 10px;
                font-family:"Arial Narrow", sans-serif;
                font-weight: 600;
                font-size: 20px;
                        
                border-radius: 10px;
                border: 2px solid #000000;
            }   
        input[type=text],input[type=submit]:hover{
                opacity:0.8;
            }
        td {
                font-size: 15px;
                line-height: 20px;
                padding: 0 20px;
                text-align: justify;
                vertical-align: top;
                width: 50%;
        }

        td.first {
                border-right: 2px solid #000000;
        }
        table {
            width: auto;
           
        }
        th, td {
            width: auto;
            text-align: left;
            border-spacing: 0;
            
        }
        
        #b0{
            background-color: #625C78;
        }
        #b1{
            background-color: #8B3636;
        } 
        #b2{
            background-color: #764E1B;
        }
        #b21{
            background-color: #76421B;
        }
        #b3{
            background-color: #368B54;
        }
        #b4{
            background-color: #454260;
        }
        #b5{
            color: #ffffff;
            background-color: #71A449;
        }
        #b6{
            background-color: #49A457;
        }
        #b7{
            background-color: #49A479;
        }
        #b8{
            background-color: #49A49A;
        }
        #a1{
            background-color: #EC9393;
        }
        #a2{
            background-color: #B99361;
        }
        #a3{
            background-color: #FFFFFF;
        }
         </style> 
         
              
                
    '''