% Open file
fileID = fopen('hard-soft-kmeans.csv');

% Read in file (comment out if already read)
dataRaw = textscan(fileID,'%s %f %f %f %f %f %f %f %f %f','Delimiter',',','HeaderLines',1);
% {1}  Kmeans Type
% {2}  K Clusters (Data clusters is 4)
% {3}  Points Used 20/80
% {4}  Points Used Post 20/80
% {5}  20/80 Test Correct
% {6}  Post 20/80 Correct
% {7}  20/80 Train Adjusted Rand Score
% {8}  20/80 Train Calinski Score
% {9}  20/80 Test Adjusted Rand Score
% {10} 20/80 Test Calinski Score

% Grab the size of the data
[row,~] = size(dataRaw{1});

% Index array for soft and hard k-means
hardIndex = zeros(row,1);
softIndex = zeros(row,1);
for i = 1:1:row
    if dataRaw{1}(i,1) == "hard"
        hardIndex(i,1) = 1;
    else
        softIndex(i,1) = 1;
    end
end

figure(1)
subplot(3,2,1);
y = dataRaw{6}.*hardIndex;
y(y == 0) = -1;
plot(dataRaw{2},y,'o');
title({"Hard 20/80 Test Accuracy","(dataCentroids = 4, \sigma = 0.25)"});
ylabel("20/80 test accuracy");
xlabel("hard k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,3);
y = dataRaw{9}.*hardIndex;
y(y == 0) = -1;
plot(dataRaw{2},y,'o');
title({"Hard Adjusted Rand Index (ARI) Score","(dataCentroids = 4, \sigma = 0.25)"});
ylabel("ADI score");
xlabel("hard k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,5);
y = dataRaw{10}.*hardIndex;
y(y == 0) = -1;
plot(dataRaw{2},y,'o');
title({"Hard Calinski-Harabaz Index (CHI) Score","(dataCentroids = 4, \sigma = 0.25)"});
ylabel("CHI score");
xlabel("hard k-means clusters");
xlim([1.5,5.5]);
ylim([0,max(y)*1.1]);
grid on;
subplot(3,2,2);
y = dataRaw{6}.*softIndex;
y(y == 0) = -1;
plot(dataRaw{2},y,'o');
title({"Soft 20/80 Test Accuracy","(dataCentroids = 4, \sigma = 0.25)"});
ylabel("20/80 test accuracy");
xlabel("soft k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,4);
y = dataRaw{9}.*softIndex;
y(y == 0) = -1;
plot(dataRaw{2},y,'o');
title({"Soft Adjusted Rand Index (ARI) Score","(dataCentroids = 4, \sigma = 0.25)"});
ylabel("ADI score");
xlabel("soft k-means clusters");
xlim([1.5,5.5]);
ylim([0,1.1]);
grid on;
subplot(3,2,6);
y = dataRaw{10}.*softIndex;
y(y == 0) = -1;
plot(dataRaw{2},y,'o');
title({"Soft Calinski-Harabaz Index (CHI) Score","(dataCentroids = 4, \sigma = 0.25)"});
ylabel("CHI score");
xlabel("soft k-means clusters");
xlim([1.5,5.5]);
ylim([0,max(y)*1.1]);
grid on;


