from abstract_factory import AbstractFactoryABC, LineWriterFactory, ColumnWriterFactory
from enum import Enum


class Sorting(Enum):
    bubble = 'bubble'
    selection = 'selection'
    insertion = 'insertion'


class Writer(Enum):
    line = 'line'
    column = 'column'


def get_factory(factory_type: str):
    if factory_type == Writer.line.value:
        return LineWriterFactory()
    elif factory_type == Writer.column.value:
        return ColumnWriterFactory()


def get_product(factory: AbstractFactoryABC, product_type: str):
    if product_type == Sorting.bubble.value:
        return factory.create_bubble_sorter()
    elif product_type == Sorting.selection.value:
        return factory.create_selection_sorter()
    elif product_type == Sorting.insertion.value:
        return factory.create_insertion_sorter()


def get_program(factory_type: str, product_type: str):
    factory = get_factory(factory_type)
    if factory:
        return get_product(factory, product_type)
