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
        df['Time'][df['Time'].str.contains(pat = i)]=nombre

final_clea_t= lambda x: x if x=='no information' or x=='afternoon' or x=='morning' or x=='evening' else 'no information'
df['Time']=df['Time'].apply(final_clea_t)

'''
##### nueva funcion para strings 
actv = df.Activity.values.tolist()
actv_s = [nltk.tokenize.wordpunct_tokenize(text) for text in actv]
stopwords = nltk.corpus.stopwords.words('english')

from itertools import groupby

def clear_multiple_char(comment):        
    ti = []
    for words in comment:
        t = [''.join(["".join(i) for i, _ in groupby(word)]) if len(word)>10 else word for word in words]
        ti.append(t)
    return ti

punctuation = string.punctuation # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
punctuation += '0123456789'

def comment_raiz(comment):
    text = []
    for lista in comment:
        valids = [word for word in lista if word not in stopwords and word not in punctuation and len(word)>2]
        valids_true = [''.join([char for char in word if char not in punctuation]) for word in valids if 
                       len(''.join([char for char in word if char not in punctuation]))>0]
        text.append(valids_true)
    return text

# lis_type = [nltk.pos_tag(lista_limpia[i])for i in range(len(lista_limpia))]

from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
punctuation = string.punctuation # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
punctuation += '0123456789'

def comment_raiz(comment):
    text = []
    for lista in comment:
        valids = [stemmer.stem(word) for word in lista if word not in stopwords and word not in punctuation and len(word)>2]
        valids_true = [''.join([char for char in word if char not in punctuation]) for word in valids if 
                       len(''.join([char for char in word if char not in punctuation]))>0]
        text.append(valids_true)
    return text

atv_fin=comment_raiz(atv_)# Add numbers

atv_fin


from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize, sent_tokenize 

w_vb = list(map((lambda lista: nltk.pos_tag(lista[i][0]) for i in range(len(pruebita))),listilla))
lista = []

for i in range(len(pruebita)):
    tagged = nltk.pos_tag(lista[i][0])
    lista.append(tagged)

def counter(comment_clear):
    cnt = Counter()
    for words in comment_clear:
        for word in words:
            cnt[word] += 1
    return cnt
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize, sent_tokenize
'''