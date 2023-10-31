# Data Preprocessing

# Importing the libraries
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
# Imputer can not be use any more
# from sklearn.preprocessing import Imputer 
from sklearn.impute import SimpleImputer


# Importing the dataset
dataset = pd.read_csv('mlAtoZ-c/Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Data_Preprocessing/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Taking care of missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)
print(y)
