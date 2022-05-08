# Tarea-USA-Housing

El link de este repositorio es: [Github](https://github.com/alexlomu/Tarea-USA-Housing)
https://github.com/alexlomu/Tarea-USA-Housing.
En esta entrega nos dan un dataset sobre viviendas en EE.UU. y nos piden hacer funciones y graficos sobre el dataset. Para ello he creado a parte de un archivo main.py donde se ejecutan todos las funciones desarrolladas dentro de la carpeta clases en el archivo funciones.py, donde ademas también he creado funciones para crear gráficos de todo tipo los cuales se guardaran en la carpeta Graficos.
El código de funciones.py es el siguiente:
```
import random
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

housing = pd.read_csv('USA_Housing.csv', sep = '\t')
#Funcion para buscar a través de un minimo del salario
def buscar_zona_min_salario(housing, min):
    dt_mask = housing['Salario medio anual de la zona'] >= min
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
#Funcion para buscar zonas a partir de una edad maxima de las casas
def buscar_zona_max_edad(housing, max):
    dt_mask = housing['Media de edad de las casas'] <= max
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
#Funcion para buscar zonas con un numero de dormitorios minimos
def buscar_zona_min_dormitorios(housing, min):
    dt_mask = housing['Media de habitaciones'] >= min
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
#Funcion para buscar una zona dependiendo de la población
def buscar_zona_poblacion(housing):
  ent = input("Deseas buscar una zona introduciendo un maximo o un minimo de poblacion?(Introduce max o min)")
  ent = ent.lower()
  if ent == "max":
    dt_mask = housing['Poblacion de la zona'] <= ent
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
  elif ent == "min":
    dt_mask = housing['Poblacion de la zona'] >= ent
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
  else:
    print("Algo ha ido mal :(")
#Funcion para buscar una zona a traves del precio medio
def buscar_zona_precio(housing):
  ent = input("Deseas buscar una zona introduciendo un maximo o un minimo de precio?(Introduce max o min)")
  ent = ent.lower()
  if ent == "max":
    dt_mask = housing['Precio'] <= ent
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
  elif ent == "min":
    dt_mask = housing['Precio'] >= ent
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
  else:
    print("Algo ha ido mal :(")
#Funcion para crear graficos excepto de dispersion
def grafico(dataset, tipo_grafico):
  fig, ax = plt.subplots()
  dataset.plot(kind=tipo_grafico, ax=ax)
  ax.set_title("Grafico", loc = "center", fontdict = {"fontsize":14, "fontweight":"bold", "color": "tab:blue"})
  ax.set_ylabel("")
  plt.savefig("graficos/grafico"+"-".join(tipo_grafico)+".png",bbox_inches="tight")
#Funcion para crear graficos de dispersion
def dispersion(eje_x, eje_y):
  fig, ax = plt.subplots()
  ax.scatter(housing[eje_x], housing[eje_y])
  ax.set_title("Grafico", loc = "center", fontdict = {"fontsize":14, "fontweight":"bold", "color": "tab:blue"})
  ax.set_ylabel("")
  plt.savefig("graficos/grafico"+"-".join("dispersion")+".png",bbox_inches="tight")
```

El código de main.py es el siguiente:
```
from clases import *
try:
  f = open('USA_Housing.csv')
except FileNotFoundError:
  print('El fichero no existe.')
else:
    lineas = f.readlines()
    f.close()
housing = pd.read_csv('USA_Housing.csv', sep = '\t')
housing.rename(columns = {"Avg. Area Income": "Salario medio anual de la zona", "Avg. Area House Age":"Media de edad de las casas", "Avg. Area Number of Rooms": "Media de habitaciones", "Avg. Area Number of Bedrooms":"Media de dormitorios", "Area Population": "Poblacion de la zona", "Price": "Precio", "Address": "Direccion"})

#Ejemplos funciones
buscar_zona_min_salario(housing, 50000)

buscar_zona_max_edad(housing, 6)

buscar_zona_min_dormitorios(housing, 5)

buscar_zona_poblacion(housing)

buscar_zona_precio(housing)

#Ejemplos graficas
grafico(housing["Media de edad de las casas"], "bar")

grafico(housing["Media de dormitorios"], "hist")

dispersion("Salario medio anual de la zona", "Precio")

dispersion("Media de edad de las casas", "Precio")

dispersion("Media de habitaciones", "Media de dormitorios")

dispersion("Poblacion de la zona", "Salario medio anual de la zona")
```
