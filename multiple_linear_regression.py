import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split as tts
boston = datasets.load_boston()

x= boston.data
y= boston.target

x_train, x_test,y_train,y_test = tts(x,y, test_size=1, random_state=1)

regr= linear_model.LinearRegression()

regr.fit(x_train, y_train)
print('Coefficients: {}'.format(regr.coef_))
print('Variance Score: {}'.format(regr.score(x_test,y_test)))

plt.scatter(regr.predict(x_train),regr.predict(x_train)-y_train,color='green',label='Train Data')

plt.scatter(regr.predict(x_test), regr.predict(x_test)-y_test,color='blue', label='Test Data')
plt.hlines(y=0, xmin=0, xmax=0, linewidth=2)
plt.show()
