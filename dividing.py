from typing import Callable
from cluster import Cluster


class DividingFunction:
    def __init__(self, cluster1: Cluster, cluster2: Cluster):
        self.cluster1 = cluster1
        self.cluster2 = cluster2
        self.function: Callable[[list], float] = DividingFunction.get_function(cluster1, cluster2)

    def __call__(self, image: list) -> float:
        return self.function(image)

    @staticmethod
    def get_function(cluster1: Cluster, cluster2: Cluster) -> Callable[[list], float]:
        def dividing(image: list) -> float:
            return cluster1.decisive_function(image) - cluster2.decisive_function(image)

        return dividing
