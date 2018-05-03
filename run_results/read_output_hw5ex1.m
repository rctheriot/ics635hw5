% Open file
fileID = fopen('output-hw5ex1.csv');

% Read in file (comment out if already read)
dataRaw = textscan(fileID,'%f %f %f %f %f %f %f %f %f %f %s %f %f %s','Delimiter',',','HeaderLines',1);
% {1} dataGeneratedCentroids
% {2} kmeansClusters
% {3} standardDeviation
% {4} pointsTrain
% {5} pointsTest
% {6} pointsTotal
% {7} trainAdjustedRand
% {8} trainCalinski
% {9} testAdjustedRand
% {10} testAdjustedRandRank
% {11} testAdjustedRandRankMatchesDataCentroidCount
% {12} testCalinski
% {13} testCalinskiRank
% {14} testCalinskiRankMatchesDataCentroidCount

% Grab the size of the data
[row,~] = size(dataRaw{1});

sigDesired = 0.5;

% Identify which entries have sigma = 0.25
sigIndex = zeros(row,1);
for i = 1:1:row
    if dataRaw{3}(i,1) == sigDesired
        sigIndex(i,1) = 1;
    end
end

% Identify which entries 2, 3, and 4 centroids
dataCen2 = zeros(row,1);
dataCen3 = zeros(row,1);
dataCen4 = zeros(row,1);
for i = 1:1:row
    if dataRaw{1}(i,1) == 2
        dataCen2(i,1) = 1;
    end
    if dataRaw{1}(i,1) == 3
        dataCen3(i,1) = 1;
    end
    if dataRaw{1}(i,1) == 4
        dataCen4(i,1) = 1;
    end
end


kMeansClusters = dataRaw{2}.*sigIndex;
testAdjustedRand = dataRaw{9}.*sigIndex;
testCalinski = dataRaw{12}.*sigIndex;

figure(1)
subplot(3,2,1)
plot(kMeansClusters.*dataCen2,testAdjustedRand,".")
title("Adjusted Rand Index (dataCentroids = 2, \sigma = 0.5)");
xlim([1,11]);
ylabel("test accuracy");
xlabel("kMeans Clusters");
grid on;
subplot(3,2,2)
plot(kMeansClusters.*dataCen2,testCalinski,".")
title("Calinski (dataCentroids = 2, \sigma = 0.5)");
xlim([1,11]);
ylabel("Calinski Score");
xlabel("kMeans Clusters");
grid on;
subplot(3,2,3)
plot(kMeansClusters.*dataCen3,testAdjustedRand,".")
title("Adjusted Rand Index (dataCentroids = 3, \sigma = 0.5)");
xlim([1,11]);
ylabel("test accuracy");
xlabel("kMeans Clusters");
grid on;
subplot(3,2,4)
plot(kMeansClusters.*dataCen3,testCalinski,".")
title("Calinski (dataCentroids = 3, \sigma = 0.5)");
xlim([1,11]);
ylabel("Calinski Score");
xlabel("kMeans Clusters");
grid on;
subplot(3,2,5)
plot(kMeansClusters.*dataCen4,testAdjustedRand,".")
title("Adjusted Rand Index (dataCentroids = 4, \sigma = 0.5)");
xlim([1,11]);
ylabel("test accuracy");
xlabel("kMeans Clusters");
grid on;
subplot(3,2,6)
plot(kMeansClusters.*dataCen4,testCalinski,".")
title("Calinski (dataCentroids = 4, \sigma = 0.5)");
xlim([1,11]);
ylabel("Calinski Score");
xlabel("kMeans Clusters");
grid on;

