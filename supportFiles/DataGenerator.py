

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

import numpy as np
import numpy.random as nprandom

from sklearn import mixture

import math


# ------------------------------------------------------------------------------------------------------------------

class DataObject:

    def __init__(self, centroids, standardDeviation, numberOfPoints, radius=1):
        # Create tracking values for center locations
        self.centroidLocations = []
        self.centroidPoints = []
        self.points = [] # A modified point object
        
        # These are the same
        self.standardDeviation = standardDeviation
        self.sigma = standardDeviation

        # safety checks
        # Python convention is _ marks private or things that shouldn't be modified
        self._hasMadeCentroids = False
        self._hasMadePoints = False

        # Place Centroids
        self._makeCentroids(centroids, radius)

        # Make Points
        self._makePoints(numberOfPoints)

    # Python convention is _ marks private or things that shouldn't be modified
    def _makeCentroids(self, centroidCount, radius):
        if (self._hasMadeCentroids):
            print("Warning: _makeCentroids accessed after already generated, they were NOT made")
            return
        self._hasMadeCentroids = True

        # Special case for each
        if (centroidCount == 1):
            self.centroidLocations.append([0,0])
        elif (centroidCount == 2):
            self.centroidLocations.append([-1 * (radius / 2),0])
            self.centroidLocations.append([1 * (radius / 2),0])
        elif (centroidCount == 3):
            # 1st point is directly north of origin
            self.centroidLocations.append([0, radius])
            # equilateral triangle, next is left lower point
            # def legCalculator(hypotenuse, degree, leg="a"):
            self.centroidLocations.append([
                legCalculator(hypotenuse=radius, degree=-30, leg='o'),
                -1 * legCalculator(hypotenuse=radius, degree=-30, leg='a')]) # -1 because negative y value, the -30 degree account for -x
            # right leg
            self.centroidLocations.append([
                legCalculator(hypotenuse=radius, degree=30, leg='o'),
                -1 * legCalculator(hypotenuse=radius, degree=30, leg='a')])
        elif (centroidCount == 4):
            # Going clockwise
            self.centroidLocations.append([0, radius])
            self.centroidLocations.append([radius, 0])
            self.centroidLocations.append([0, -1 * radius])
            self.centroidLocations.append([-1 * radius, 0])
        elif (centroidCount == 5):
            # Going clockwise, 360 / 5 = 72 deg changes
            self.centroidLocations.append([0, radius])
            # Next two height wise are at 18 deg
            self.centroidLocations.append([ legCalculator(hypotenuse=radius, degree=18, leg='a'), legCalculator(hypotenuse=radius, degree=18, leg='o')])
            self.centroidLocations.append([ -1 * legCalculator(hypotenuse=radius, degree=18, leg='a'), legCalculator(hypotenuse=radius, degree=18, leg='o')])
            # Next two height wise are at 18 deg
            self.centroidLocations.append([ legCalculator(hypotenuse=radius, degree=-54, leg='a'), legCalculator(hypotenuse=radius, degree=-54, leg='o')])
            self.centroidLocations.append([ -1 * legCalculator(hypotenuse=radius, degree=-54, leg='a'), legCalculator(hypotenuse=radius, degree=-54, leg='o')])
        # add caontainer for centroid points
        for i in range(0, len(self.centroidLocations)):
            self.centroidPoints.append([])
    

    # Python convention is _ marks private or things that shouldn't be modified
    def _makePoints(self, numberOfPoints):
        if (self._hasMadePoints):
            print("Warning: _makePoints accessed after points already generated, additional points were NOT made")
            return
        
        self._hasMadePoints = True
        centroids = self.centroidLocations

        if (len(centroids)) < 1:
            print("Warning: _makePoints centroids: ", len(centroids))
            print("         Unable to make points")
            return

        sigma = self.sigma
        centroidIndex = 0
        pointsPerCentroid = math.floor(numberOfPoints / len(centroids))
        pointsRemainderForLast = numberOfPoints % len(centroids)

        for centroidIndex in range(0, len(centroids)):
            for pointCount in range(0, pointsPerCentroid):
                point = [
                    nprandom.normal(0, sigma) + centroids[centroidIndex][0], # x value
                    nprandom.normal(0, sigma) + centroids[centroidIndex][1] # y value
                ]
                self.points.append(point)
                self.centroidPoints[centroidIndex].append(point)
        # Go to last centroid
        centroidIndex = len(centroids) - 1
        # Add remainders to it
        for pointCount in range(0, pointsRemainderForLast):
            point = [
                nprandom.normal(0, sigma) + centroids[centroidIndex][0], # x value
                nprandom.normal(0, sigma) + centroids[centroidIndex][1] # y value
            ]
            self.points.append(point)
            self.centroidPoints[centroidIndex].append(point)

    def getPoints(self, numberOfPoints, offset=0):
        if (numberOfPoints + offset) > len(self.points):
            print("Warning: getPoints queried for  ", numberOfPoints, " points")
            print("         more than available: ", len(self.points))
            return
        points = []
        labels = []
        centroidIndex = 0
        centroidRound = math.floor(offset / len(self.centroidLocations))
        for i in range(0, numberOfPoints):
            points.append(self.centroidPoints[centroidIndex][centroidRound])
            labels.append(centroidIndex)

            # alternate evenly between centroids
            centroidIndex += 1
            if centroidIndex >= len(self.centroidLocations):
                centroidIndex = 0
                centroidRound += 1
        return points, labels


def legCalculator(hypotenuse, degree, leg="a"):
    if (leg == "a"):
        return math.cos(math.radians(degree)) * hypotenuse
    else:
        return math.sin(math.radians(degree)) * hypotenuse