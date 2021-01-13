from numpy import genfromtxt
from cluster import Cluster

images = genfromtxt('data_test.csv', delimiter=',')
clusters = [Cluster([[0.52, 5.7]]), Cluster([[-7.72, 1.06]]),
            Cluster([[5.3, -2.61]]), Cluster([[-1.81, -6.34]])]
