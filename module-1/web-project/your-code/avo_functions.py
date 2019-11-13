
from bs4 import BeautifulSoup
import pandas as pd
import os
import re 
import json
import requests
from pandas.io.json import json_normalize

def df(file):
	avo = pd.read_csv(file)
	avo = pd.DataFrame(avo)
	avo['date']= pd.to_datetime(avo['date'], format = '%d/%m/%Y').dt.date
	return avo

def acceso_API(url):
	with open('.gitignore') as f:
    		acceso = f.read()
	prueba = acceso.strip()
	response = requests.get(url, headers = {'Bmx-Token':prueba})
	result = response.json()
	tc_date = acceso_API(url)['bmx']['series'][0]['datos']
	df_tc = json_normalize(tc_date)
	df_tc['fecha']= pd.to_datetime(df_tc['fecha'], format = '%d/%m/%Y').dt.date
	return df_tc

def df_sin_api(path,avo):
	df_tc = pd.read_csv(path)
	df_tc = pd.DataFrame(df_tc)
	df_tc['fecha']= pd.to_datetime(df_tc['fecha'], format = '%Y/%m/%d').dt.date
	tc = []
	i, j = 0,0
	while i < len(avo) and j < len(df_tc):
		if avo['date'][i] == df_tc['fecha'][j]:
			tc.append(float(df_tc['dato'][j]))
			i += 1
		elif avo['date'][i] < df_tc['fecha'][j]:
			tc.append('No esta {}'.format(avo['date'][i]))
			i += 1
		else:
			j += 1

	avo['exchange_rate'] = tc
	avo['Price_mx']= avo['Price_us']*avo['exchange_rate']
	print(avo)
	return avo 

def coordenadas(av):
	reg_sep = list(map((lambda i: re.findall('[A-Z][^A-Z]*', i)),av['region']))
	prue=[]
	for i in reg_sep:
		if len(i)>1:
			prue.append(' '.join(i))
		else:
			prue.append(i[0])
			av['region']= prue
	for i in range(len(av['region'])):
		if av['region'][i] == 'Total U S':
			av['region'][i] = 'US'

	av = av.drop(av[(av.region == 'Northeast')|(av.region == 'Midsouth')|(av.region == 'South Central')|(av.region == 'Southeast')|(av.region == 'West')|(av.region == 'US')|(av.region == 'Plains')|(av.region == 'California')|(av.region == 'Great Lakes')|(av.region == 'South Carolina')|(av.region == 'Northern New England')|(av.region =='West Tex New Mexico')].index)
	
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
		else:
			i = i 
		return i
	av.region =av.region.apply(ciudades)

	av = av.sort_values(by = ['region']).reset_index(drop=True)

	request = requests.get('https://www.latlong.net/category/cities-236-15.html').content
	soup = BeautifulSoup(request, 'lxml')
	tabla = soup.find_all('table')
	tab_sucia = [tabla[i].text.split('\n\n') for i in range(len(tabla))][0]
	tab = [i.replace('USA','US').replace('UK','US').split(',') for i in tab_sucia]
	tab_clean = [(i[0].strip(),i[-1].replace(' the US','').replace('US','').strip()) for i in tab]
	lat_long = pd.DataFrame(tab_clean, columns=['country', 'lat-long',]).drop_duplicates(subset = ['country'], keep='first')
	lat_long = lat_long.sort_values(by =['country']).reset_index(drop=True)

	i,j =0,0
	coordinates = []

	while i < len(av) and j < len(lat_long):
		if av.region[i] == lat_long.country[j]:
			coordinates.append(lat_long['lat-long'][j])
			i += 1
		elif av.region[i] > lat_long.country[j]:
			j += 1
		else:
			coordinates.append('No está {}'.format(av.region[i]))
			i += 1
	av['coordinates']=coordinates
	print (av)
	return av