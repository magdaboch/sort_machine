from sort_machine import AbstractSortMachine


class QuickSort(AbstractSortMachine):
    def __init__(self):
        super().__init__()

    def get_data(self):
        super().get_data()

    def sort(self, array):
        if len(array) <= 1:
            return array
        m = array[len(array) / 2]  # wyznaczenie elementu rozdzielajacego
        return sort([i for i in array if i <= m]) \ # posortowanie elementow mniejszych
        + sort([i for i in array if i > m])  # posortowanie elementow wiekszych

