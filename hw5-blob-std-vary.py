
# Included in py
from random import randint
import math
import operator
import sys

#External installs
import numpy as np

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Local
sys.path.insert(0, './supportFiles')
from KmPlotter import KmPlotter
from fuzzyk import FuzzyKMeans
import pysupport as utils

# ------------------------------------------------------------------------------------------------------------------

# np.random.seed(0)


# ------------------------------------------------------------------------------------------------------------------


def generateValues(start=-5, stop=10, step=0.1):
	vals = []
	current = start
	while (current <= stop):
		vals.append(current)
		current += step
	return vals



def trainTestOnPoints(allData, allDataLabels, subsetSize, kclusters):
  # Create starting data to train and cross validate on
  subset = allData[0:subsetSize]
  subsetLabels = allDataLabels[0:subsetSize]

  # Post train testing
  pointsToTestInLargeEval = 500
  largeEvalSet = allData[subsetSize:(subsetSize + pointsToTestInLargeEval)]
  largeEvalSetLabels = allDataLabels[subsetSize:(subsetSize + pointsToTestInLargeEval)]


  # Up to but not including the end range. currently 4,5 beacuse mismatch on cluster count
  for clusterFitSize in range(kclusters, kclusters + 1):
    splitTrainTest2080(subset, subsetLabels, clusterFitSize, largeEvalSet, largeEvalSetLabels)



def splitTrainTest2080(subset, subsetLabels, kclusters,  largeEvalSet, largeEvalSetLabels):
  # train in different cuts
  for i in range (0, 5):
    # Randomize cuts using the random_state
    X_train, X_test, y_train, y_test = train_test_split(subset, subsetLabels, test_size=0.2, random_state=i)
    
    # Hard k means
    km = KMeans(n_clusters=kclusters)
    km.fit(X_train)

    percentCorrect = determinePredictionCorrectness(kclusters, km, X_test, y_test)
    percentCorrectOfLargeEval = determinePredictionCorrectness(kclusters, km, largeEvalSet, largeEvalSetLabels)
    # evalutate train (fit)
    trainAdjustedRandResult = metrics.adjusted_rand_score(y_train, km.labels_)  
    trainCalinskiResult = metrics.calinski_harabaz_score(X_train, km.labels_)
    testPredict = km.predict(X_test)
    testAdjustedRandResult = metrics.adjusted_rand_score(y_test, testPredict)  
    testCalinskiResult = metrics.calinski_harabaz_score(X_train, km.labels_)


    # Record: point count, test accuracy, after evaluation results (500)
    lineToWrite = "hard, " + str(kclusters) + ", " + str(len(subset)) + ", " + str(len(largeEvalSet))
    lineToWrite += ", " + str(percentCorrect) + ", " + str(percentCorrectOfLargeEval)
    lineToWrite += ", " + str(trainAdjustedRandResult) + ", " + str(trainCalinskiResult)
    lineToWrite += ", " + str(testAdjustedRandResult) + ", " + str(testCalinskiResult)

    utils.fileLog(lineToWrite)

    # Fuzzy kmeans
    fkm = FuzzyKMeans(k=kclusters, m=2)
    fkm.fit(X_train)

    percentCorrect = determinePredictionCorrectness(kclusters, fkm, X_test, y_test)
    percentCorrectOfLargeEval = determinePredictionCorrectness(kclusters, fkm, largeEvalSet, largeEvalSetLabels)
    # evalutate train (fit)
    trainAdjustedRandResult = metrics.adjusted_rand_score(y_train, fkm.labels_)  
    trainCalinskiResult = metrics.calinski_harabaz_score(X_train, fkm.labels_)
    testPredict = fkm.predict(X_test)
    testAdjustedRandResult = metrics.adjusted_rand_score(y_test, testPredict)  
    testCalinskiResult = metrics.calinski_harabaz_score(X_train, fkm.labels_)


    # Record: point count, test accuracy, after evaluation results (500)
    lineToWrite = "soft, " + str(kclusters) + ", " + str(len(subset)) + ", " + str(len(largeEvalSet))
    lineToWrite += ", " + str(percentCorrect) + ", " + str(percentCorrectOfLargeEval)
    lineToWrite += ", " + str(trainAdjustedRandResult) + ", " + str(trainCalinskiResult)
    lineToWrite += ", " + str(testAdjustedRandResult) + ", " + str(testCalinskiResult)

    utils.fileLog(lineToWrite)




def determinePredictionCorrectness(centroids, classifier, dataToTest, dataLabels):
  label_array = []
  prediction_array = []
  prediction_array2 = []
  matches = []
  X = dataToTest
  y = dataLabels
  prediction = classifier.predict(X)

  # create entry for each centroid
  for i in range(0, centroids):
    label_array.append([])
    prediction_array.append([])
    prediction_array2.append([])
    matches.append([])

  # Transfer the correct data labels, then get the predicted data label
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

  return (num_corr / num_labels)




# ------------------------------------------------------------------------------------------------------------------

# 4 clusters each 1 away from center at equal distances from each other
centers2 = [[0, 1], [1, 0]]
centers3 = [[1, 0], [0.866, -0.5], [-0.866, -0.5]]
centers4 = [[1, 0], [1, 0], [0, -1], [-1, 0]]
centers5 = [[1, 0], [0.309, 0.951], [-0.809, 0.588], [-0.809, -0.588], [.309, -0.951]]
centers6 = [[1, 0], [0.5, 0.866], [-.5, 0.866], [-1, 0], [-0.5, -.866],[0.5, -0.866]]
centers = centers2

# adding blanks for index 0 and 1
allCenters = [[], [], centers2, centers3, centers4, centers5, centers6]
totalNumberOfPointsToGenerate = 1500
standardDeviationOfPoints = 0.25

# numberOfPointsRange = generateValues(25, 50, 25)
numberOfPointsRange = generateValues(25, 500, 25)

# All data which to split apart later
dataSets = [[],[]] # add blanks for index 0 and 1
labelSets = [[],[]]
for i in range(2, len(allCenters)):
  data, labels = make_blobs(n_samples=totalNumberOfPointsToGenerate, centers=centers, cluster_std=standardDeviationOfPoints)
  dataSets.append(data)
  labelSets.append(labels)

lineToWrite = "Kmeans Type, K Clusters (Data clusters is 4), Points Used 20/80, Points Used Post 20/80"
lineToWrite += ", 20/80 Test Correct, Post 20/80 Correct"
lineToWrite += ", 20/80 Train Adjusted Rand Score, 20/80 Train Calinski Score, 20/80 Test Adjusted Rand Score, 20/80 Test Calinski Score"
utils.fileLog(lineToWrite)

for i in range(2, len(allCenters)):
  data = dataSets[i]
  labels = labelSets[i]
  n_clusters = i
  # Evaluate for different numbers of training sets to use 20/80 split on
  for count in numberOfPointsRange:
    trainTestOnPoints(data, labels, count, n_clusters)


# ------------------------------------------------------------------------------------------------------------------











