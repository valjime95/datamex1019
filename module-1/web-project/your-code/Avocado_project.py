# Avocado prices.
from bs4 import BeautifulSoup
import pandas as pd
import os
import re 
import json
import requests
from pandas.io.json import json_normalize

# Cargamos la base de datos y le damos formato de fecha a la columna fecha
avo = pd.read_csv('/Users/valeriajimeno/Documents/datamex1019/module-1/web-project/your-code/avocado_sin_key.csv')
avo = pd.DataFrame(avo)
avo['date']= pd.to_datetime(avo['date'], format = '%d/%m/%Y').dt.date
'''
 INTRODUCCIÓN A LA BASE.
 La base de datos es de la venta de aguacate (orgánico y convencional) en supermercados de estados unidos,
 las observaciones se refieren a semanas del 27-12-2015 al 26-03-2018
 Las semanas se repiten ya que de cada region, se registraron las mismas semanas.
 De las catorce variables, una es de tipo entero (year), tres de tipo categórico (Date, type, region) 
 y las demás son flotante.
'''

# Pequeño análisis de la constitución de la base
len(avo) # 17911 observaciones
len(avo.columns) # 14 columnas
avo.isnull().sum() # sin datos faltantes

print(avo.head())
print(avo.columns)
'''
Objetivo.
Lo que se quiere realizar es mostrar el precio promedio en pesos mexicanos y además ver la latitud y la longitud de
las regiones de venta.
Para el precio promedio en pesos, se va a extraer la información de la API de Banxico y para encontrar las coordenadas se realizara web scrapping de una página web
'''

''' ALCANCÉ MI NÚMERO DE CONSULTAS, POR LO QUE VOY A MANDAR LLAMAR MI CSV
# Se hace la request a la página de Banxico y el resultado se pide en forma de json.
with open('.gitignore') as f:
    acceso = f.read()
prueba = acceso.strip()

response = requests.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF63528/datos/2015-01-04/2018-03-26', headers = {'Bmx-Token':prueba})
result = response.json()

# Como result arrojó diccionarios de diccionarios de una sóla key, entonces buscamos llegar a la lista de diccionarios donde estuvieran las fechas y la cantidad, para poder normalizar el json y convertirlo en un dataframe.
tc_date = result['bmx']['series'][0]['datos']
df_tc = json_normalize(tc_date)
df_tc['fecha']= pd.to_datetime(df_tc['fecha'], format = '%d/%m/%Y').dt.date
'''
df_tc = pd.read_csv('/Users/valeriajimeno/Documents/datamex1019/module-1/web-project/your-code/df_tc.csv')
df_tc = pd.DataFrame(df_tc)
df_tc['fecha']= pd.to_datetime(df_tc['fecha'], format = '%Y/%m/%d').dt.date
print(df_tc)


# Creamos una lista en donde vamos a introducir las coordenadas si las fechas de ambos data frames coinciden.

tc = []
i, j = 0,0

while i < len(avo) and j < len(df_tc):
    #print(avo['date'][i],i,df_tc['fecha'][j],j)
    if avo['date'][i] == df_tc['fecha'][j]:
        tc.append(float(df_tc['dato'][j]))
        i += 1
    elif avo['date'][i] < df_tc['fecha'][j]:
        tc.append('No esta {}'.format(avo['date'][i]))
        i += 1
    else:
        j += 1

avo['exchange_rate'] = tc
# vamos a crear una variable que sea 'Price_mx'.
avo['Price_mx']= avo['Price_us']*avo['exchange_rate']
print(avo.head())

# REGIONES

# Lo que vamos a hacer es separar los nombres de las regiones por las mayúsculas, además vamos a cambiar el nombre
# de Total U s a US
reg_sep = list(map((lambda i: re.findall('[A-Z][^A-Z]*', i)),avo['region']))
prue=[]
for i in reg_sep:
    if len(i)>1:
        prue.append(' '.join(i))
    else:
        prue.append(i[0])
avo['region']= prue

for i in range(len(avo['region'])):
    if avo['region'][i] == 'Total U S':
        avo['region'][i] = 'US'

# En la variable de regiones, vienen además de regiones, ciudades, por lo que para buscar la latitud y longitud vamos a quitar las regiones y dejaremos sólo las ciudades.

avo = avo.drop(avo[(avo.region == 'Northeast')|(avo.region == 'Midsouth')|(avo.region == 'South Central')|(avo.region == 'Southeast')|(avo.region == 'West')|(avo.region == 'US')|(avo.region == 'Plains')|(avo.region == 'California')|(avo.region == 'Great Lakes')|(avo.region == 'South Carolina')|(avo.region == 'Northern New England')|(avo.region =='West Tex New Mexico')].index)

# WebS Scrapping

# Ahora para saber la latitud y longitud, vamos a scrapear de la siguiente página la tabla con las latitudes de
# las 1000 ciudades más importantes de US, para poder hacer merge con la columna de regiones
# y así hacer una columna con la latitud y otra con longitud.

request = requests.get('https://www.latlong.net/category/cities-236-15.html').content
soup = BeautifulSoup(request, 'lxml')
tabla = soup.find_all('table')
tab_sucia = [tabla[i].text.split('\n\n') for i in range(len(tabla))][0]

# Limpiamos la tabla que se genero con el request y lo convertimos en un dataframe con dos columnas, country y lat-long
tab = [i.replace('USA','US').replace('UK','US').split(',') for i in tab_sucia]
tab_clean = [(i[0].strip(),i[-1].replace(' the US','').replace('US','').strip()) for i in tab]
lat_long = pd.DataFrame(tab_clean, columns=['country', 'lat-long',]).drop_duplicates(subset = ['country'], keep='first')
# Acomodamos según los valores de la variable country y reiniciamos el índice para que no haya problema cuando hagamos el while.
lat_long = lat_long.sort_values(by =['country']).reset_index(drop=True)

# limpiamos la variable de regiones para que no exista problema al momento de querer hacer el match con el df de coordenadas.

def ciudades(i):
    if i == 'Baltimore Washington':
        i = 'Baltimore'
    elif i == 'Buffalo Rochester':
        i = 'Buffalo'
    elif i == 'Cincinnati Dayton':
        i = 'Cincinnati'
    elif i == 'Dallas Ft Worth':
        i = 'Dallas'
    elif i == 'Harrisburg Scranton':
        i = 'Harrisburg'
    elif i == 'Hartford Springfield':
        i = 'Springfield'
    elif i == 'Miami Ft Lauderdale':
        i = 'Miami'
    elif i == 'New Orleans Mobile':
        i = 'New Orleans'
    elif i == 'Phoenix Tucson':
        i = 'Phoenix'
    elif i == 'Raleigh Greensboro':
        i = 'Raleigh'
    elif i == 'Richmond Norfolk':
        i = 'Richmond'
    elif i == 'St Louis':
        i = 'St. Louis'
    elif i == 'New York':
        i = 'New York City'
        i = i 
    return i
avo.region =avo.region.apply(ciudades)

avo = avo.sort_values(by = ['region']).reset_index(drop=True)

# realizamos un while para crear una lista en donde esten las coordenadas según el df avo y lo asignamos a una nueva columna

i,j =0,0
coordinates = []

while i < len(avo) and j < len(lat_long):
    if avo.region[i] == lat_long.country[j]:
        coordinates.append(lat_long['lat-long'][j])
        i += 1
    elif avo.region[i] > lat_long.country[j]:
        j += 1
    else:
        coordinates.append('No está {}'.format(avo.region[i]))
        i += 1

avo['coordinates']=coordinates
print(set(avo.coordinates))
print(avo.head())
print(len(avo))


