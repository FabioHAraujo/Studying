import pandas as pd
notas = pd.read_csv("Movies/ml-latest/ratings.csv")
print(notas.head(15))
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
print(notas.head(15))
print(notas["nota"].unique())
print(notas['nota'].value_counts())

