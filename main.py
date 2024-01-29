import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

humedadInterna=0
respuesta=""

#semaforo que calcula cuando hay que hecharle agua a la planta
def regar(humedadInterna):
    humedadInterna = float(humedadInterna)
    if  humedadInterna <= 950:
        return "malo.jpg" #"Aca necesito agua"

    #elif humedadInterna >= 300 and humedadInterna <=950:
     #   return "normal.jpg" #"Me empiezo a quedar sin agua" 
    
    else:
        return "bueno.jpg" #"no necesito agua"

#crea el servidor web
app = Flask(__name__)

@app.route('/') #creamos la ruta principal
def home():
    return 'home'

@app.route('/send_data', methods=['POST']) #creamos la ruta donde se capturan los datos
def capturarDatos():
    #values #se capturan los datos y se imprimen 
    val = request.data
    print(val)
    #val2 = request.values
    #print(val2)
     
    #guardo los datos en variables seperandolos con ; y =
    temperatura = str(val).split(";")[1].split('=')[1]
    print("temoperatura= ", temperatura)
    humedadInterna = str(val).split(";")[2].split('=')[1]
    print("humedadInterna= ",humedadInterna)
    luz = str(val).split(";")[3].split('=')[1]
    print(luz)
    humedadExterna = str(val).split(";")[4].split('=')[1]
    print(humedadExterna)

    
    respuesta = regar(humedadInterna)
    return respuesta retorna el valor que se calcula en la funicon regar que es cuando se riega
    
#esta es la ruta para las imagenes iteractivas de la app movil
@app.route('/send_data_movil', methods=['POST']) #creamos la ruta donde se capturan los datos
def capturarDatos_movil():
    val2 = request.data #recibe un post de datos
    print(val2)
    
    respuesta = regar(humedadInterna) 
    print(respuesta)
    return respuesta Regresa el return de la funcion segar que son string que idifican las imagenes iteractivas
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80) #inicamos la pagina
