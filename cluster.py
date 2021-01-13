from typing import List, Any
import numpy as np


class Cluster:
    def __init__(self, standards: List[list]):
        self.standards: List[np.ndarray] = [np.array(each) for each in standards]
        self.images: List[np.ndarray] = []

    def get_distance(self, image: list) -> float:
        to_all_standards = [np.linalg.norm(np.array(image) - each) for each in self.standards]
        return min(to_all_standards)

    def add_image(self, image: list) -> None:
        self.images.append(np.array(image))

    def decisive_function(self, image: list) -> Any:
        standard = np.mean(self.standards, axis=0)
        return np.sum((np.sum(np.array(image).transpose() * standard) - 0.5 * np.sum(standard.transpose() * standard)))
