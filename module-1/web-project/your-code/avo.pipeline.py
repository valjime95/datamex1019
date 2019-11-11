from avo_functions import * 

file_path = '/Users/valeriajimeno/Documents/datamex1019/module-1/web-project/your-code/avocado_sin_key.csv'
url_banxico ='https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF63528/datos/2015-01-04/2018-03-26'
tipo_cambio = '/Users/valeriajimeno/Documents/datamex1019/module-1/web-project/your-code/df_tc.csv'

avocado = df(file_path)

df_pmx = df_sin_api(tipo_cambio,avocado)

coordenadas(df_pmx)