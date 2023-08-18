import pandas as pd

# Carregar os arquivos CSV em dois DataFrames
df1 = pd.read_csv('prd.csv')
df2 = pd.read_csv('hml.csv')

only_in_df1 = df1.merge(df2, how='left', indicator=True).loc[lambda x: x['_merge'] == 'left_only']
only_in_df2 = df2.merge(df1, how='left', indicator=True).loc[lambda x: x['_merge'] == 'left_only']

# Salvar as linhas exclusivas em arquivos separados
only_in_df1.to_csv('exclusivas_em_arquivo1.csv', index=False)
only_in_df2.to_csv('exclusivas_em_arquivo2.csv', index=False)

print("Linhas exclusivas foram salvas em 'exclusivas_em_arquivo1.csv' e 'exclusivas_em_arquivo2.csv'")