from abstract_factory.product_abc import ProductABC
from sorts import bubble_sort
import json


class ColumnWriterAndBubbleSorter(ProductABC):
    def __init__(self, read_from: str, write_to: str):
        self._read_from = read_from
        self._write_to = write_to
        self._sorted = 'Not sorted'
        self._array = []

    def read(self):
        with open(self._read_from, 'r') as f:
            line = f.readline()
            self._array = json.loads(line)

    def write(self):
        with open(self._write_to, 'w') as f:
            for item in self._array:
                f.write(f'{item}\n')
            f.write(self._sorted)

    def do_action(self):
        bubble_sort(self._array)
        self._sorted = '"Bubble sort" used'
