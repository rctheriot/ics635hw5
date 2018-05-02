import numpy as np
from sklearn_extensions.fuzzy_kmeans import KMedians, FuzzyKMeans, KMeans
from sklearn.datasets.samples_generator import make_blobs

np.random.seed(0)
centroids = 5
batch_size = 45
X, labels_true = make_blobs(n_features=100, centers=2, cluster_std=5.25)

kmeans = KMeans(k=3)
kmeans.fit(X)

fuzzy_kmeans = FuzzyKMeans(k=10, m=2)
fuzzy_kmeans.fit(X)

print('KMEANS')
print(kmeans.cluster_centers_)

print('FUZZY_KMEANS')
print(fuzzy_kmeans.labels_)
print(labels_true)