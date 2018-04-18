

import matplotlib.pyplot as plt

import numpy as np

from sklearn.cluster import KMeans

from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles
from sklearn.datasets import make_moons

from KmPlotter import KmPlotter

plotter = KmPlotter()


def generateValues(start=-5, stop=10, step=0.1):
	vals = []
	current = start
	while (current <= stop):
		vals.append(current)
		current += step
	return vals


#                           start, stop, step
clusterRange = generateValues(2, 10, 1)

for i in range(0, len(clusterRange)):
    print("Run ", i+1, " / ", len(clusterRange))
    X, y = make_blobs(n_samples=20, n_features=2, shuffle=True, noise=None, random_state=None)
    machine = KMeans(n_clusters=clusterRange[i], random_state=0).fit(X)

    # def plot(self, machine, data, fileName, fileType="png", saveInsteadOfShow=True):
    plotter.plot(machine, X, fileName="blobTest-clusters" + str(clusterRange[i]))



print("Done")