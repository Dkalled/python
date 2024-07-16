import pandas as pd
from Projeto_1.settings import Config
from dicionario import mapa




for item in mapa:
    if item.lista == 'sellers':
        df_sellers = pd.DataFrame
        df_sellers = pd.read_csv(item.arquivos)
    if item.lista == 'order_items':
        df_itens = pd.DataFrame
        df_itens = pd.read_csv(item.arquivos)
    else:
        df = pd.DataFrame
        df = pd.read_csv(item.arquivos)
        print(df.info())

df_result = pd.DataFrame.merge(df_sellers, df_itens, how='inner', on='seller_id')
df_result.to_json('resultado.json')

df_json = pd.DataFrame
df_json = pd.read_json('resultado.json')
print(df_json)
