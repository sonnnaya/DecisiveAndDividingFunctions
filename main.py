from typing import List
from cluster import Cluster
from data import images, clusters
from dividing import DividingFunction


def get_clustered_decisive(image_list: List[list], clusters: List[Cluster]) -> List[Cluster]:
    classificated = clusters[:]

    for image in image_list:
        values = [cluster.decisive_function(image) for cluster in classificated]
        maximum = max(values)
        index = values.index(maximum)
        classificated[index].add_image(image)

    return classificated


def get_clustered_dividing(images: List[list], clusters: List[Cluster]) -> List[Cluster]:
    classificated = clusters[:]
    length = len(classificated)
    dividings = [DividingFunction(classificated[i], classificated[j])
                 for i in range(length)
                 for j in range(length)
                 if i != j]

    for image in images:
        dividing_values = list(map(lambda dividing: dividing(image), dividings))
        maximum = max(dividing_values)
        index = dividing_values.index(maximum)

        dividings[index].cluster1.add_image(image)

    return classificated


classificated = get_clustered_dividing(images, clusters)

if __name__ == '__main__':
    for i, each in enumerate(classificated):
        print(f"Class {str(i + 1)}:")
        for image in each.images:
            print(list(image), end=', ')
        print()
