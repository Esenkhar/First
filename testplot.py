import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

boston_dataset = load_boston()
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target
# print(boston['LSTAT'].describe(include='all').round(2))
# boston.hist(column='LSTAT', bins=20)
# boston.plot(kind='scatter', x='RM', y='MEDV', figsize=(8, 6))
X = boston[['RM']]
Y = boston['MEDV']
model = LinearRegression()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)
model.fit(X_train, Y_train)
y_test_predicted = model.predict(X_test)
# residuals = Y_test - y_test_predicted
plt.scatter(X_test, Y_test, label='testing data');
plt.plot(X_test, y_test_predicted, label='prediction', linewidth=3)
# plt.scatter(X_test, residuals ** 2, label='residuals')
# plt.hlines(y=0, xmin=X_test.min(), xmax=X_test.max(), linestyle='--')
plt.xlabel('RM, LSTAT')
plt.ylabel('MEDV')
plt.legend(loc='upper left')

plt.show()
