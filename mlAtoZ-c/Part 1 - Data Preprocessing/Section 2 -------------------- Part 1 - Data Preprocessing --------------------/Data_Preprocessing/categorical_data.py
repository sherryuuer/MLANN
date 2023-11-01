import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer


# Importing the dataset
dataset = pd.read_csv('mlAtoZ-c/Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Data_Preprocessing/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
print(X)
print(y)

# Taking care of missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Encoding categorical data
# Encoding the Independent Variable
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# onehotencoder = OneHotEncoder(categories=[0])

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
    remainder='passthrough'
)
X = ct.fit_transform(X)

# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
print(X)
print(y)
