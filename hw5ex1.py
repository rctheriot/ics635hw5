import sys
import os
import math

import numpy as np
from random import randint

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn import metrics

import matplotlib.pyplot as plt
import operator

from pandas import DataFrame

# Custom plotter
sys.path.insert(0, './supportFiles')
from KmPlotter import KmPlotter
import DataGenerator
import pysupport as utils

# ------------------------------------------------------------------------------------------------------------------

plotter = KmPlotter()


def runTestSet(params, fileName):

  # estimatedRuns = ((params.centroidRange.end - params.centroidRange.start) / params.centroidRange.increment *
  #   (params.standardDeviationRange.end - params.standardDeviationRange.start) / params.standardDeviationRange.increment *
  #   (params.pointRange.end - params.pointRange.start) / params.pointRange.increment) + 3
  
  currentRun = 1

  # if file doesn't exist add header
  if os.path.isfile(fileName) == False:
    fileHeader = [
      "dataGeneratedCentroids",
      "kmeansClusters",
      "standardDeviation",
      "pointsTrain",
      "pointsTest", 
      "pointsTotal",
      "trainAdjustedRand",
      "trainCalinski",
      "testAdjustedRand",
      "testAdjustedRandRank",
      "testAdjustedRandRankMatchesDataCentroidCount",
      "testCalinski",
      "testCalinskiRank",
      "testCalinskiRankMatchesDataCentroidCount",
    ]
    utils.addLineToFile(fileName, ', '.join(str(x) for x in fileHeader))
  
  linesToWriteToFile = []

  for centroidCount in range (params.centroidRange.start, params.centroidRange.end + 1, params.centroidRange.increment):
    stdDeviationValueRange = np.arange(params.standardDeviationRange.start, params.standardDeviationRange.end + params.standardDeviationRange.increment, params.standardDeviationRange.increment)
    for stdIndex in range (0, len(stdDeviationValueRange)):
      totalNumberOfPoints = params.pointRange.end + (centroidCount * 2) # buffer
      # Generate data  __init__(self, centroids, standardDeviation, numberOfPoints, radius=1):
      dataset = DataGenerator.DataObject(centroidCount, stdDeviationValueRange[stdIndex], totalNumberOfPoints)
      # for numberOfPoints variation
      for pointSubset in range (params.pointRange.start, params.pointRange.end + 1, params.pointRange.increment):
        # get points def getPoints(self, numberOfPoints, offset=0):
        trainCount = math.floor(pointSubset * 0.2)
        testCount = math.floor(pointSubset * 0.8)
        trainPoints, trainLabels = dataset.getPoints(trainCount)
        testPoints, testLabels = dataset.getPoints(testCount, offset=trainCount)
        clusterLimit = min(len(trainPoints), 11) # take the smaller, can't fit more clusters than samples
        clusterRankingAjustedRand = []
        clusterRakningCalinski = []
        clustersEvalutedInKmeans = 0
        for clusterCount in range(2, clusterLimit):
          clustersEvalutedInKmeans += 1
          # make kmeans
          kmeans = KMeans(n_clusters=clusterCount, random_state=0).fit(trainPoints)
          # evalutate train (fit)
          trainAdjustedRandResult = metrics.adjusted_rand_score(trainLabels, kmeans.labels_)  
          trainCalinskiResult = metrics.calinski_harabaz_score(trainPoints, kmeans.labels_)
          # evaluate test
          testPredictedLables = kmeans.predict(testPoints)
          testAdjustedRandResult = metrics.adjusted_rand_score(trainLabels, kmeans.labels_)  
          testCalinskiResult = metrics.calinski_harabaz_score(trainPoints, kmeans.labels_)
          clusterRankingAjustedRand.append(testAdjustedRandResult)
          clusterRakningCalinski.append(testCalinskiResult)
          #record
          valuesForFile = [
            centroidCount, clusterCount, stdDeviationValueRange[stdIndex],
            trainCount, testCount, (trainCount + testCount),
            trainAdjustedRandResult, trainCalinskiResult,
            testAdjustedRandResult, "testAdjustedRank", False, # index 8, 9, 10
            testCalinskiResult, "testCalinskiRank", False, # index 11, 12, 13
          ]
          linesToWriteToFile.append(valuesForFile)
          # utils.addLineToFile(fileName, ', '.join(str(x) for x in valuesForFile))
          # TODO image record
          #update
          currentRun += 1
          if currentRun % 10 == 0:
            print("Completed run ", currentRun)#, " / ", estimatedRuns)
          # end clusterCount
        # evaluate clusters
        # sorting is low to high, then reverse using slice with iterator in negative direction
        sortedClusterResultAdjustedRand = sorted(clusterRankingAjustedRand)[::-1]
        sortedClusterResultCalinski = sorted(clusterRakningCalinski)[::-1]
        for c in range(0, clustersEvalutedInKmeans):
          found_ar = False
          found_c = False
          for s in range(0, clustersEvalutedInKmeans):
            if (found_ar == False and clusterRankingAjustedRand[c] == sortedClusterResultAdjustedRand[s]):
              linesToWriteToFile[len(linesToWriteToFile) - clustersEvalutedInKmeans + c][9] = s + 1 # hard code to match index
              if ((c + 2) == centroidCount) and (s+1 == 1):
                linesToWriteToFile[len(linesToWriteToFile) - clustersEvalutedInKmeans + c][10] = True
              found_ar = True
            if (found_c == False and clusterRakningCalinski[c] == sortedClusterResultCalinski[s]):
              linesToWriteToFile[len(linesToWriteToFile) - clustersEvalutedInKmeans + c][12] = s + 1 # hard code to match index
              if ((c + 2) == centroidCount) and (s+1 == 1):
                linesToWriteToFile[len(linesToWriteToFile) - clustersEvalutedInKmeans + c][13] = True
              found_c = True
          
        # end trainCount
      # end stdDev
    #end centroidCount
  
  for i in range(0, len(linesToWriteToFile)):
    utils.addLineToFile(fileName, ', '.join(str(x) for x in linesToWriteToFile[i]))

  print("Finished")

# ------------------------------------------------------------------------------------------------------------------

# Setup parameters
params = utils.blank()
params.centroidRange = utils.blank()
params.centroidRange.start = 2
params.centroidRange.end = 4
params.centroidRange.increment = 1

params.standardDeviationRange = utils.blank()
params.standardDeviationRange.start = 0
params.standardDeviationRange.end = 3
params.standardDeviationRange.increment = 0.25

params.pointRange = utils.blank()
params.pointRange.start = 25
params.pointRange.end = 500
params.pointRange.increment = 25


# Local quick test values, comment these out to do the above in full
# params.centroidRange.end = 3
# params.standardDeviationRange.end = 1
# params.pointRange.end = 50

runTestSet(params, "localtest.csv")




