import random
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
try:
  f = open('USA_Housing.csv')
except FileNotFoundError:
  print('El fichero no existe.')
else:
    lineas = f.readlines()
    f.close()
housing = pd.read_csv('USA_Housing.csv', sep = '\t')
housing.rename(columns = {"Avg. Area Income": "Salario medio anual de la zona", "Avg. Area House Age":"Media de edad de las casas", "Avg. Area Number of Rooms": "Media de habitaciones", "Avg. Area Number of Bedrooms":"Media de dormitorios", "Area Population": "Poblacion de la zona", "Price": "Precio", "Address": "Direccion"})
#Funcion para buscar a través de un minimo del salario
def buscar_zona_min_salario(housing, min):
    dt_mask = housing['Salario medio anual de la zona'] >= min
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
#Ejemplo
buscar_zona_min_salario(housing, 50000)
#Funcion para buscar zonas a partir de una edad maxima de las casas
def buscar_zona_max_edad(housing, max):
    dt_mask = housing['Media de edad de las casas'] <= max
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
#Ejemplo
buscar_zona_max_edad(housing, 6)
#Funcion para buscar zonas con un numero de dormitorios minimos
def buscar_zona_min_dormitorios(housing, min):
    dt_mask = housing['Media de habitaciones'] >= min
    filtered_dt = housing[dt_mask]
    print(filtered_dt)
#Ejemplo
buscar_zona_min_dormitorios(housing, 5)
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
#Ejemplo


