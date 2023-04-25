"""import torch
x = torch.arange(12,dtype=torch.float32).reshape(3,4)
y = torch.arange(12,dtype=torch.float32).reshape(3,4)
z = torch.cat((x,y),dim=0)
print(z)"""


import os
import pandas as pd
import torch

data = pd.read_csv("C:\PycharmProject\Dive-into-deeplearning\data\house_tiny.csv")
print(data)
inputs , output =data.iloc[:, 0:2], data.iloc[:,2]
inputs = inputs.fillna(inputs.mean())
print(inputs)
inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)
X, y = torch.tensor(inputs.values), torch.tensor(output.values)
print(X, y)