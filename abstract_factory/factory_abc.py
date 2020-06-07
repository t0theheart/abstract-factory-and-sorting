from abc import ABC, abstractmethod


class AbstractFactoryABC(ABC):
    @staticmethod
    @abstractmethod
    def create_bubble_sorter(): pass

    @staticmethod
    @abstractmethod
    def create_selection_sorter(): pass

    @staticmethod
    @abstractmethod
    def create_insertion_sorter(): pass
