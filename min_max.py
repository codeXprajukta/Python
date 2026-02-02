from sklearn.preprocessing import MinMaxScaler,Normalizer
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
scaler=MinMaxScaler()
data = datasets.load_iris()['data']
Normalizer().fit_transform(X=data)
scaler.fit(data)
data=scaler.transform(data)
plt.hist(data[:,0])
plt.show()
