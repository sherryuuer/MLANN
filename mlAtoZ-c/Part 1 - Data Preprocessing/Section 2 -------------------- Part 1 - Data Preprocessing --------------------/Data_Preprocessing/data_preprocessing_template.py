import pandas as pd
from sklearn.model_selection import train_test_split


# Importing the dataset
dataset = pd.read_csv('mlAtoZ-c/Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Data_Preprocessing/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)
