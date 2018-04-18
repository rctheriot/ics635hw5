

import matplotlib.pyplot as plt
import numpy as np



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

