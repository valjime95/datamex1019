import pandas as pd
import numpy as np
import re
import nltk
from collections import Counter
import string

shark_data = pd.read_csv('sharks.csv' )
# Primero debemos ver como esta constituido nuestra data.
df = pd.DataFrame(shark_data)
df.columns = ['Case Number','Date','Year','Type','Country','Area','Location',
       'Activity','Name','Sex','Age','Injury','Fatal_(Y/N)','Time',
       'Species','Investigator/Source','pdf','href_formula','href',
       'CaseNumber_1','CaseNumber_2','original_order','Unnamed:_22',
       'Unnamed:_23']

# Funciones básicas para columnas de tipo object

tamaño = range(len(df))
            
no_info = lambda element: 'no information' if element=='' or element =='nan' or element=='.' else element
            
def lower(colum_name):
    df[colum_name] = df[colum_name].apply(lambda i: str(i).lower())
    
esp_1 = lambda x: re.sub('^\s+', "", x)
esp_2 = lambda x: re.sub('\s$', "", x)
esp_3 = lambda x: re.sub('\s{2}', "", x)
esp_4 = lambda x: re.sub('\s\s$', "", x)

def espacios(colum_name):
    df[colum_name] = df[colum_name].apply(esp_1)
    df[colum_name] = df[colum_name].apply(esp_2)
    df[colum_name] = df[colum_name].apply(esp_3)
    df[colum_name] = df[colum_name].apply(esp_4)

par = lambda x: re.sub('\(\w*', "", x)    

def parentesis(colum_name):
    df[colum_name] = df[colum_name].str.replace("?","")
    df[colum_name] = df[colum_name].str.replace(")","")
    df[colum_name] = df[colum_name].apply(par)


between = lambda element:'no information' if 'between' in element else element

months ={'jan':'01',
         'feb':'02',
         'mar':'03',
         'apr':'04',
         'may':'05',
         'jun':'06',
         'jul':'07',
         'aug':'08',
         'sep':'09',
         'oct':'10', 
         'nov':'11',
         'dec':'12'}
def format_date(element):
    element = element.replace('-','/')
    for key in months:
        element = element.replace(key,months[key])
    return element

night = ['22','23','00','01','02','03','04','05','06']
morning = ['07','08','09','10','11']
afternoon = ['12','13','14','15','16','17']
evening = ['18','19','20','21']
    
def time(lista,nombre):
    for i in lista:
    	df['Time'][df['Time'].str.startswith(i)]= nombre

n = ['night','pm','dusk','dark','midnight']
m = ['morning','am']
a = ['afternoon','sunset','day','sundown','mid afternoon', 'late afternoon','midday']

def time2(lista,nombre):
    for i in lista:
        df['Time'][df['Time'].str.contains(pat = i)] = nombre

final_clea_t= lambda x: x if x=='no information' or x=='afternoon' or x=='morning' or x=='evening' else 'no information'
df['Time']=df['Time'].apply(final_clea_t)


#import * 
lower('Date')
df.Date = df.Date.str.replace("reported","")
df.Date= df.Date.str.replace("before ","")
espacios('Date')
parentesis('Date')
df['Date'] = df['Date'].apply(between)

# .....DATE.....
path1 = '\d{2}\/\d{2}\/\d{2}|\d{2}\-[aA-zZ]{3}\-\d{4}|\d{2}\-[aA-zZ]{3}\-\d{2}'
y = [re.findall(path1,df.Date[i]) for i in tamaño ]
dates = list(map((lambda x: "no information" if x == []  else format_date(x[0])), y))
df.Date = dates

# ---Year----
years = list(map((lambda i: i if len(str(i))== 4 else 'No information'),df['Year']))
df['Year']= years

# ----Sex----
lower('Sex')
df['Sex'] = df['Sex'].apply(no_info)
espacios('Sex')
sexo =lambda x: x if x =='m' or x=='f'  or x == 'no information' else 'no information'
df.Sex = df.Sex.apply(sexo)

# ----Fatal----
lower('Fatal_(Y/N)')
df['Fatal_(Y/N)'] = df['Fatal_(Y/N)'].apply(no_info)
espacios('Fatal_(Y/N)')
fatal =lambda x: x if x =='n' or x=='y'  or x == 'no information' else 'no information'
df['Fatal_(Y/N)'] = df['Fatal_(Y/N)'].apply(fatal)

#------pdf------
lower('pdf')
df['pdf'] = df['pdf'].apply(no_info)
espacios('pdf')
PDF=lambda x: x if x.endswith('.pdf') else 'no information'
df['pdf']=df['pdf'].apply(PDF)
#set(df['pdf']

#----href----
lower('href')
df['href'] = df['href'].apply(no_info)
espacios('href')
http = lambda x: x if x.startswith('http://') else 'no information'
df['href'] = df['href'].apply(http)

#----href_formula----
lower('href_formula')
df['href_formula']=df['href_formula'].apply(no_info)
espacios('href_formula')
df['href_formula'] = df['href_formula'].apply(http)

#----Unnamed:_22----
lower('Unnamed:_22')
df['Unnamed:_22']=df['Unnamed:_22'].apply(no_info)

#----Unnamed:_23----
lower('Unnamed:_23')
df['Unnamed:_23']=df['Unnamed:_23'].apply(no_info)

#----CaseNumber_1----
lower('CaseNumber_1')
path3 = '\d{4}\.\d{2}\.\d{2}\.\w+|\d{4}\.\d{2}\.\d{2}'
case = [re.findall(path3,df['CaseNumber_1'][i]) for i in tamaño]
case_1 = list(map((lambda x: "no information" if x == []  else x[0]),case))
df['CaseNumber_1'] = case_1

#----CaseNumber_2----
lower('CaseNumber_2')
case_ = [re.findall(path3,df['CaseNumber_2'][i]) for i in tamaño]
case_2 = list(map((lambda x: "no information" if x == []  else x[0]),case_))
df['CaseNumber_2'] = case_2

#----Location----
lower('Location')
df['Location'] = df['Location'].str.replace("off ","")
df['Location']=df['Location'].apply(no_info)
espacios('Location')

#----Time----
lower('Time')
df['Time'] = df['Time'].str.replace('before ',"")
df['Time'] = df['Time'].str.replace('early ',"")
df['Time'] = df['Time'].str.replace('-',"")
df['Time'] = df['Time'].str.replace('.',"")
df['Time'] = df['Time'].str.replace('>',"")
df['Time'] = df['Time'].str.replace('<',"")
df['Time'] = df['Time'].apply(no_info)
espacios('Time')
df['Time'] = df['Time'].apply(between)
df['Time'].value_counts()

time(night,'night')
time(morning,'morning')
time(afternoon,'afternoon')
time(evening,'evening')

time(n,'night')
time(m,'morning')
time(a,'afternoon')
espacios('Time')

df['Time']=df['Time'].apply(final_clea_t)
df['Time'].value_counts()

#----type----
#   ESPECÍFICO
df['Type'][df['Type'].str.startswith('Boat')]='Boating'

#----Activity----
'''
lower('Activity')
df['Activity']=df['Activity'].apply(no_info)
espacios('Activity')
parentesis('Activity')

atv_ = clear_multiple_char(actv_s)

lista_limpia=comment_raiz(atv_)# Add numbers

dic_limpio = dict(counter(lista_limpia))
activities = list(filter((lambda key: key.endswith('ing')),dic_limpio))
'''
#----Country----
lower('Country')
df['Activity']=df['Country'].apply(no_info)
espacios('Country')
parentesis('Country')

for i  in range(len(df)):
    if 'ocean' in df['Country'][i] or 'sea' in df['Country'][i] or 'gulf' in df['Country'][i] or 'golf' in df['Country'][i] or 'diego garcia' in df['Country'][i] or '/' in df['Country'][i]:
        df['Country'][i] = 'no information'

# Area

lower('Area')
df['Area']=df['Area'].apply(no_info)
espacios('Area')
parentesis('Area')
coma = lambda x: re.sub('\,[a-z]|\,\s[a-z]*', "", x)
df['Area'] = df['Area'].apply(coma)