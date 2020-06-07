from abstract_factory.factory_abc import AbstractFactoryABC
from abstract_factory.column_writer_factory.products import (ColumnWriterAndBubbleSorter,
                                                             ColumnWriterAndSelectionSorter,
                                                             ColumnWriterAndInsertionSorter)


class ColumnWriterFactory(AbstractFactoryABC):
    @staticmethod
    def create_bubble_sorter():
        return ColumnWriterAndBubbleSorter

    @staticmethod
    def create_selection_sorter():
        return ColumnWriterAndSelectionSorter

    @staticmethod
    def create_insertion_sorter():
        return ColumnWriterAndInsertionSorter
