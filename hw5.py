import numpy as np
from random import randint

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt
import operator

from KmPlotter import KmPlotter

plotter = KmPlotter()

features = 4

X, y = make_blobs(n_samples=200, n_features=2, centers=features, cluster_std=1)
test = []
test_labels = []

data_len = len(X)

for i in range(1,int(data_len * 0.80)):
  randomNum = randint(0, len(X) - 1)
  test.append(X[randomNum])
  test_labels.append(y[randomNum])
  X = np.delete(X, randomNum, 0)
  y = np.delete(y, randomNum, 0)

test = np.array(test)
test_labels = np.array(test_labels)

kmeans = KMeans(n_clusters=features, random_state=0).fit(X)
prediction = kmeans.predict(test)
# def plot(self, machine, data, fileName, fileType="png", saveInsteadOfShow=True):
plotter.plot(kmeans, X, fileName="blobs")
test_len = len(test)

num_labels = 0
num_corr = 0
label_array = []
prediction_array = []
prediction_array2 = []
matches = []

for i in range(0, features):
  label_array.append([])
  prediction_array.append([])
  prediction_array2.append([])
  matches.append([])

for i in range(0, len(test_labels)):
  label_array[test_labels[i]].append(i)
for i in range(0, len(prediction)):
  prediction_array[prediction[i]].append(i)

for i in range(0, features):
  for j in range(0, features):
    matches[i].append(len(set(label_array[i]) & set(prediction_array[j])))

for i in range(0, features):
  index, value = max(enumerate(matches[i]), key=operator.itemgetter(1))
  prediction_array2[i] = prediction_array[index]

for i in range(0, features):
  num_labels = num_labels + len(prediction_array2[i])
  num_corr = num_corr + len(set(label_array[i]) & set(prediction_array2[i]))

print(num_corr / num_labels)

