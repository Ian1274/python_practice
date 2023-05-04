import matplotlib.pyplot as plt
import random
import torch
from d2l import torch as d2l
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
print(df)

k = df.pop("b")
print(k)

df.insert(df.shape[1], 'label', k)
print(df)