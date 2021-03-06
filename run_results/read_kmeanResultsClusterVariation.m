% Open file
fileID = fopen('kmeanResultsClusterVariation_NAremoved.csv');

% Read in file (comment out if already read)
dataRaw = textscan(fileID,'%s %f %f %f %f %f %f %f %f %f %f','Delimiter',',','HeaderLines',1);
% {1}  Kmeans Type
% {2}  data clusters
% {3}  k clusters
% {4}  Points Used 20/80
% {5}  Points Used Post 20/80
% {6}  20/80 Test Correct
% {7}  Post 20/80 Correct
% {8}  20/80 Train Adjusted Rand Score
% {9}  20/80 Train Calinski Score
% {10} 20/80 Test Adjusted Rand Score
% {11} 20/80 Test Calinski Score

% Grab the size of the data
[row,~] = size(dataRaw{1});

% Index array for soft and hard k-means
hardIndex = zeros(row,1);
softIndex = zeros(row,1);
kClutstersIndex = zeros(row,4);     % column 1: 2, column 2: 3, column 3:4, etc...
for i = 1:1:row
    
    % Check hard-soft
    if dataRaw{1}(i,1) == "hard"
        hardIndex(i,1) = 1;
    else
        softIndex(i,1) = 1;
    end
    
    % Check kMeans clusters
    if dataRaw{3}(i,1) == 2
        kClutstersIndex(i,1) = 1;
    elseif dataRaw{3}(i,1) == 3
        kClutstersIndex(i,2) = 1;
    elseif dataRaw{3}(i,1) == 4
        kClutstersIndex(i,3) = 1;
    else
        kClutstersIndex(i,4) = 1;
    end
end

figure(1)
subplot(3,2,1);
y1 = dataRaw{7}.*hardIndex.*kClutstersIndex(:,1);
y1(y1 == 0) = -1;
y2 = dataRaw{7}.*hardIndex.*kClutstersIndex(:,2);
y2(y2 == 0) = -1;
y3 = dataRaw{7}.*hardIndex.*kClutstersIndex(:,3);
y3(y3 == 0) = -1;
y4 = dataRaw{7}.*hardIndex.*kClutstersIndex(:,4);
y4(y4 == 0) = -1;
plot(dataRaw{3},y1,'o',...
    dataRaw{3},y2,'o',...
    dataRaw{3},y3,'o',...
    dataRaw{3},y4,'o');
title({"Hard 20/80 Test Accuracy","(dataCentroids = 2, \sigma = 0.25)"});
ylabel("20/80 test accuracy");
xlabel("no. of hard k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,3);
y1 = dataRaw{10}.*hardIndex.*kClutstersIndex(:,1);
y1(y1 == 0) = -1;
y2 = dataRaw{10}.*hardIndex.*kClutstersIndex(:,2);
y2(y2 == 0) = -1;
y3 = dataRaw{10}.*hardIndex.*kClutstersIndex(:,3);
y3(y3 == 0) = -1;
y4 = dataRaw{10}.*hardIndex.*kClutstersIndex(:,4);
y4(y4 == 0) = -1;
plot(dataRaw{3},y1,'o',...
    dataRaw{3},y2,'o',...
    dataRaw{3},y3,'o',...
    dataRaw{3},y4,'o');
title({"Hard Adjusted Rand Index (ARI) Score","(dataCentroids = 2, \sigma = 0.25)"});
ylabel("ADI score");
xlabel("no. of hard k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,5);
y1 = dataRaw{11}.*hardIndex;
y1 = dataRaw{11}.*hardIndex.*kClutstersIndex(:,1);
y1(y1 == 0) = -1;
y2 = dataRaw{11}.*hardIndex.*kClutstersIndex(:,2);
y2(y2 == 0) = -1;
y3 = dataRaw{11}.*hardIndex.*kClutstersIndex(:,3);
y3(y3 == 0) = -1;
y4 = dataRaw{11}.*hardIndex.*kClutstersIndex(:,4);
y4(y4 == 0) = -1;
plot(dataRaw{3},y1,'o',...
    dataRaw{3},y2,'o',...
    dataRaw{3},y3,'o',...
    dataRaw{3},y4,'o');
title({"Hard Calinski-Harabaz Index (CHI) Score","(dataCentroids = 2, \sigma = 0.25)"});
ylabel("CHI score");
xlabel("no. of hard k-means clusters");
xlim([1.5,5.5]);
ylim([0,max(y1)*1.1]);
grid on;
subplot(3,2,2);
y1 = dataRaw{7}.*softIndex.*kClutstersIndex(:,1);
y1(y1 == 0) = -1;
y2 = dataRaw{7}.*softIndex.*kClutstersIndex(:,2);
y2(y2 == 0) = -1;
y3 = dataRaw{7}.*softIndex.*kClutstersIndex(:,3);
y3(y3 == 0) = -1;
y4 = dataRaw{7}.*softIndex.*kClutstersIndex(:,4);
y4(y4 == 0) = -1;
plot(dataRaw{3},y1,'o',...
    dataRaw{3},y2,'o',...
    dataRaw{3},y3,'o',...
    dataRaw{3},y4,'o');
title({"Soft 20/80 Test Accuracy","(dataCentroids = 2, \sigma = 0.25)"});
ylabel("20/80 test accuracy");
xlabel("no. of soft k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,4);
y1 = dataRaw{10}.*softIndex.*kClutstersIndex(:,1);
y1(y1 == 0) = -1;
y2 = dataRaw{10}.*softIndex.*kClutstersIndex(:,2);
y2(y2 == 0) = -1;
y3 = dataRaw{10}.*softIndex.*kClutstersIndex(:,3);
y3(y3 == 0) = -1;
y4 = dataRaw{10}.*softIndex.*kClutstersIndex(:,4);
y4(y4 == 0) = -1;
plot(dataRaw{3},y1,'o',...
    dataRaw{3},y2,'o',...
    dataRaw{3},y3,'o',...
    dataRaw{3},y4,'o');
title({"Soft Adjusted Rand Index (ARI) Score","(dataCentroids = 2, \sigma = 0.25)"});
ylabel("ADI score");
xlabel("no. of soft k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,6);
y1 = dataRaw{11}.*softIndex;
y1 = dataRaw{11}.*softIndex.*kClutstersIndex(:,1);
y1(y1 == 0) = -1;
y2 = dataRaw{11}.*softIndex.*kClutstersIndex(:,2);
y2(y2 == 0) = -1;
y3 = dataRaw{11}.*softIndex.*kClutstersIndex(:,3);
y3(y3 == 0) = -1;
y4 = dataRaw{11}.*softIndex.*kClutstersIndex(:,4);
y4(y4 == 0) = -1;
plot(dataRaw{3},y1,'o',...
    dataRaw{3},y2,'o',...
    dataRaw{3},y3,'o',...
    dataRaw{3},y4,'o');
title({"Soft Calinski-Harabaz Index (CHI) Score","(dataCentroids = 2, \sigma = 0.25)"});
ylabel("CHI score");
xlabel("no. of soft k-means clusters");
xlim([1.5,5.5]);
ylim([0,max(y1)*1.1]);
grid on;




% figure(1)
% subplot(3,2,1);
% y1 = dataRaw{7}.*hardIndex*kClutstersIndex(:,1);
% y1(y1 == 0) = -1;
% y2 = dataRaw{7}.*hardIndex*kClutstersIndex(:,2);
% y2(y2 == 0) = -1;
% y2 = dataRaw{7}.*hardIndex*kClutstersIndex(:,3);
% y2(y2 == 0) = -1;
% y2 = dataRaw{7}.*hardIndex*kClutstersIndex(:,4);
% y2(y2 == 0) = -1;
% plot(dataRaw{2},y1,'o');
% title({"Hard 20/80 Test Accuracy","(dataCentroids = 4, \sigma = 0.25)"});
% ylabel("20/80 test accuracy");
% xlabel("hard k-means clusters");
% xlim([1.5,5.5]);
% ylim([0,1.1]);
% grid on;
% subplot(3,2,3);
% y1 = dataRaw{9}.*hardIndex;
% y1(y1 == 0) = -1;
% plot(dataRaw{2},y1,'o');
% title({"Hard Adjusted Rand Index (ARI) Score","(dataCentroids = 4, \sigma = 0.25)"});
% ylabel("ADI score");
% xlabel("hard k-means clusters");
% xlim([1.5,5.5]);
% ylim([0,1.1]);
% grid on;
% subplot(3,2,5);
% y1 = dataRaw{10}.*hardIndex;
% y1(y1 == 0) = -1;
% plot(dataRaw{2},y1,'o');
% title({"Hard Calinski-Harabaz Index (CHI) Score","(dataCentroids = 4, \sigma = 0.25)"});
% ylabel("CHI score");
% xlabel("hard k-means clusters");
% xlim([1.5,5.5]);
% ylim([0,max(y1)*1.1]);
% grid on;
% subplot(3,2,2);
% y1 = dataRaw{6}.*softIndex;
% y1(y1 == 0) = -1;
% plot(dataRaw{2},y1,'o');
% title({"Soft 20/80 Test Accuracy","(dataCentroids = 4, \sigma = 0.25)"});
% ylabel("20/80 test accuracy");
% xlabel("soft k-means clusters");
% xlim([1.5,5.5]);
% ylim([0,1.1]);
% grid on;
% subplot(3,2,4);
% y1 = dataRaw{9}.*softIndex;
% y1(y1 == 0) = -1;
% plot(dataRaw{2},y1,'o');
% title({"Soft Adjusted Rand Index (ARI) Score","(dataCentroids = 4, \sigma = 0.25)"});
% ylabel("ADI score");
% xlabel("soft k-means clusters");
% xlim([1.5,5.5]);
% ylim([0,1.1]);
% grid on;
% subplot(3,2,6);
% y1 = dataRaw{10}.*softIndex;
% y1(y1 == 0) = -1;
% plot(dataRaw{2},y1,'o');
% title({"Soft Calinski-Harabaz Index (CHI) Score","(dataCentroids = 4, \sigma = 0.25)"});
% ylabel("CHI score");
% xlabel("soft k-means clusters");
% xlim([1.5,5.5]);
% ylim([0,max(y1)*1.1]);
% grid on;


