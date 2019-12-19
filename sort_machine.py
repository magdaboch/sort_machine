"""
File contains implementation of AbstractSrtMachine
"""
import sphinx
from abc import ABC, abstractmethod


class AbstractSortMachine(ABC):
    def __init__(self):
        """
        Abstract class, which define method of sorting
        """
        pass

    @abstractmethod
    def get_data(self, array):
        """

        :param array:
        :return:
        """
        self.array = array

    @abstractmethod
    def sort(self):
        pass

    # def set_sorted_list(self, algorytm: AbstractSortMachine, array):
    #     algorytm.get_data(array)
    #     self.sorted_list = algorytm.sort(array)
    #     print(self.sorted_list)


