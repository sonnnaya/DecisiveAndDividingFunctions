import matplotlib.pyplot as plt
import numpy as np

from cluster import Cluster
from main import classificated


def separator(x: float, cluster1: Cluster, cluster2: Cluster) -> float:
    s1 = np.mean(cluster1.standards, axis=0)
    s2 = np.mean(cluster2.standards, axis=0)

    return (0.5 * (np.dot(s1.T, s1) - np.dot(s2.T, s2)) + x * (s2[0] - s1[0])) / (s1[1] - s2[[1]])


image_clusters = [cluster.images for cluster in classificated]

x_es = [[image[0] for image in images] for images in image_clusters]
y_es = [[image[1] for image in images] for images in image_clusters]

x_separators = [x for x in np.arange(-10, 10, 1)]
y_separators = [[separator(x, classificated[i], classificated[j]) for x in np.arange(-10, 10, 1)]
                for i in range(len(classificated))
                for j in range(len(classificated))
                if j > i]

for i in range(len(x_es)):
    plt.scatter(x_es[i], y_es[i])

for y in y_separators:
    plt.plot(x_separators, y)

plt.axis([-10, 10, -10, 10])

# fig, axes = plt.subplots(nrows=2, ncols=3)
#
# axes[0, 0].set(title='The boundary between class 1 and class 2')
# axes[0, 1].set(title='The boundary between class 1 and class 3')
# axes[0, 2].set(title='The boundary between class 1 and class 4')
# axes[1, 0].set(title='The boundary between class 2 and class 3')
# axes[1, 1].set(title='The boundary between class 2 and class 4')
# axes[1, 2].set(title='The boundary between class 3 and class 4')
#
# for i, ax in enumerate(axes.flat):
#     for j in range(len(x_es)):
#         ax.scatter(x_es[j], y_es[j])
#
#     ax.plot(x_separators, y_separators[i])
#     ax.axis([-10, 10, -10, 10])

plt.show()
