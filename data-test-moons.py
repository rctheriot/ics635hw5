

import matplotlib.pyplot as plt

import numpy as np

from sklearn.cluster import KMeans

from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles
from sklearn.datasets import make_moons

from KmPlotter import KmPlotter

plotter = KmPlotter()


X, y = make_moons(n_samples=20, shuffle=True, noise=None, random_state=None)
machine = KMeans(n_clusters=2, random_state=0).fit(X)

# def plot(self, machine, data, fileName, fileType="png", saveInsteadOfShow=True):
plotter.plot(machine, X, fileName="moonTest")

print("Done")