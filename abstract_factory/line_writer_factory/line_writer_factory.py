from abstract_factory.factory_abc import AbstractFactoryABC
from abstract_factory.line_writer_factory.products import (LineWriterAndBubbleSorter, LineWriterAndSelectionSorter,
                                                           LineWriterAndInsertionSorter)


class LineWriterFactory(AbstractFactoryABC):
    @staticmethod
    def create_bubble_sorter():
        return LineWriterAndBubbleSorter

    @staticmethod
    def create_selection_sorter():
        return LineWriterAndSelectionSorter

    @staticmethod
    def create_insertion_sorter():
        return LineWriterAndInsertionSorter
