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
def grafico(housing, tipo_grafico):
  fig, ax = plt.subplots()
  housing.plot(kind=tipo_grafico, ax=ax)
  ax.set_title("Grafico", loc = "center", fontdict = {"fontsize":14, "fontweight":"bold", "color": "tab:blue"})
  ax.set_ylabel("")
  plt.savefig("graficos/grafico"+"-".join(tipo_grafico)+".png",bbox_inches="tight")
