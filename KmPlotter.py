

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from sklearn import mixture



class KmPlotter:

    def plot(self, machine, data, fileName, fileType="png", saveInsteadOfShow=True):
        # Find min and max of the data
        x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
        y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
        mesh_step_size = 0.2
        xx, yy = np.meshgrid(np.arange(x_min, x_max, mesh_step_size), np.arange(y_min, y_max, mesh_step_size))

        # Get labels for the mesh
        Z = machine.predict(np.c_[xx.ravel(), yy.ravel()])
        # Apply color
        Z = Z.reshape(xx.shape)
        plt.figure(1)
        plt.clf()
        plt.imshow(Z, interpolation='nearest',
                extent=(xx.min(), xx.max(), yy.min(), yy.max()),
                cmap=plt.cm.Paired,
                aspect='auto', origin='lower')

        plt.plot(data[:, 0], data[:, 1], 'k.', markersize=2)
        # Plot the centroids as a white X
        centroids = machine.cluster_centers_
        plt.scatter(centroids[:, 0], centroids[:, 1],
                    marker='x', s=169, linewidths=3,
                    color='w', zorder=10)
        plt.title(fileName)
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.xticks(())
        plt.yticks(())
        if (saveInsteadOfShow):
            plt.savefig('images/' + fileName + "." + fileType)
        else:
            plt.show()
        plt.clf()

        # Now create GaussianMixture
        # print("cluster centers: ", len(machine.cluster_centers_))
        clf = mixture.GaussianMixture(n_components=len(machine.cluster_centers_), covariance_type='full')
        # repack for GaussianMixture
        gma = []
        for i in range(0, len(machine.cluster_centers_)):
            gma.append([])
        t_dataPredictions = machine.predict(data)
        for i in range(0, len(data)):
            gma[t_dataPredictions[i]].append(data[i])
        X_train = np.vstack(gma)

        # print()
        # print()
        # print((t_dataPredictions))
        # print()
        # print()
        # print((X_train))
        # print()
        # print()
        # print(vars(X_train))
        # print()
        # print()


        clf.fit(X_train)
        # display predicted scores by the model as a contour plot
        x = np.linspace(x_min - 4, x_max + 4) # 1 was applied above
        y = np.linspace(y_min - 4, y_max + 4)
        X, Y = np.meshgrid(x, y)
        XX = np.array([X.ravel(), Y.ravel()]).T
        Z = -clf.score_samples(XX)
        Z = Z.reshape(X.shape)

        CS = plt.contour(X, Y, Z, norm=LogNorm(vmin=1.0, vmax=15.0),
                        levels=np.logspace(0, 1, 20))
        CB = plt.colorbar(CS, shrink=0.8, extend='both')
        plt.scatter(X_train[:, 0], X_train[:, 1], .8)

        plt.title('gmm-' + fileName)
        plt.axis('tight')
        if (saveInsteadOfShow):
            plt.savefig('images/gmm-' + fileName + "." + fileType)
        else:
            plt.show()

