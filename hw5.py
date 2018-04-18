import numpy as np
from random import randint

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn import metrics

import matplotlib.pyplot as plt
import operator

# Custom plotter
from KmPlotter import KmPlotter

plotter = KmPlotter()

centroids = 4

X, y = make_blobs(n_features=2, centers=centroids, cluster_std=3)

kmeans = KMeans(n_clusters=centroids, random_state=0).fit(X)


prediction = kmeans.predict(X)
data_length = len(X)

label_array = []
prediction_array = []
prediction_array2 = []
matches = []

for i in range(0, centroids):
  label_array.append([])
  prediction_array.append([])
  prediction_array2.append([])
  matches.append([])

for i in range(0, len(y)):
  label_array[y[i]].append(i)
for i in range(0, len(prediction)):
  prediction_array[prediction[i]].append(i)

for i in range(0, centroids):
  for j in range(0, centroids):
    matches[i].append(len(set(label_array[i]) & set(prediction_array[j])))

for i in range(0, centroids):
  index, value = max(enumerate(matches[i]), key=operator.itemgetter(1))
  prediction_array2[i] = prediction_array[index]

num_labels = 0
num_corr = 0
for i in range(0, centroids):
  num_labels = num_labels + len(prediction_array2[i])
  num_corr = num_corr + len(set(label_array[i]) & set(prediction_array2[i]))

print(num_corr / num_labels)

calinskiResult = metrics.calinski_harabaz_score(X, kmeans.labels_)

# def plot(self, machine, data, fileName, fileType="png", saveInsteadOfShow=True):
plotter.plot(kmeans, X, fileName="blobs-correct" + str(num_corr / num_labels) + "-calinski" + str(calinskiResult))

