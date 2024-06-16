import pandas as pd
import numpy as np

df = pd.read_csv(r'E:\Python\Python\Data\Raw_Data.csv')

duplicate_rows = df[df.duplicated()]
print(duplicate_rows)

print(df.isnull().any())

df.fillna(0, inplace=True)

df = df.sort_values(by='Created At')

df.to_csv('Clean_data.csv', index=False)









