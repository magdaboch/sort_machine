import time
#import matplotlib.pyplot as plt
from sort_machine import AbstractSortMachine
from bubble_sort import BubbleSort
from quicksort import QuickSort

class SortTimeComplexity:

    def __init__(self, ):
        pass

    def get_algorytm(self):
        self.list_agloritm = [BubbleSort(), QuickSort()]

    def measure_time(self, algorytm: AbstractSortMachine, array):
        """
        Function which measure time for given algorytm
        :param algorytm: objects of class algorytm's
        :param array: list to sorting
        :return:
        """
        start = time.time()
        algorytm.get_data(array)
        algorytm.sort(array)
        end = time.time()
        return end - start

    def plot_graph(self):
        pass