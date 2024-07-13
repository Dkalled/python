import pandas as pd

df_sellers = pd.DataFrame
df_sellers = pd.read_csv('../olist_sellers_dataset.csv')
print(df_sellers.info())

df_itens = pd.DataFrame
df_itens = pd.read_csv('../olist_order_items_dataset.csv')
print(df_itens.info())

df_result = pd.DataFrame.merge(df_sellers, df_itens, how='inner', on='seller_id')
df_result.to_json('resultado.json')

df_json = pd.DataFrame
df_json = pd.read_json('resultado.json')
print(df_json)