import pandas as pd

data = pd.read_csv("Zip_Zhvi_AllHomes.csv")
states = data['State'].tolist()
prices = data['2017-10'].tolist()

