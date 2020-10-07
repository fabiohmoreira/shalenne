import pandas as pd
from pymongo import MongoClient

mongo_client = MongoClient('localhost', 27018)
mongo_db = mongo_client['ProjetoIN242']
mongo_collection = mongo_db['contadorpessoas']

query = mongo_collection.find({})

df = pd.DataFrame.from_records(query)

df_filtro = df[['Entrada', 'Dia/hora', 'Quantidade de pessoas']]  ##seleção de colunas

df_filtro.plot.bar(x='Dia/hora', y='Quantidade de pessoas')












