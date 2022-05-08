import random
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
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




