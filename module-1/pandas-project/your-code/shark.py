import * 
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