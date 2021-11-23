import pandas as pd

data = pd.read_csv('data/result.csv')

DICT = data.to_dict()

print(DICT['Hora de saida'])