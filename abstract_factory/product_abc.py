from abc import ABC, abstractmethod


class ProductABC(ABC):
    @abstractmethod
    def read(self): pass

    @abstractmethod
    def write(self): pass

    @abstractmethod
    def do_action(self): pass
