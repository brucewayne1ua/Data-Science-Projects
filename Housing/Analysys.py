import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns 

data = pd.read_csv("housing.csv")
data.info()
data.dropna(inplace=True)
data.info()

from sklearn.model_selection import train_test_split
X = data.drop(['median_house_value'],axis=1)
y = data['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
train_data = X_train.join(y_train)

plt.figure(figsize=15)
sns.heatmap(train_data.corr(), annot=True, cmap="YlGnBlu")