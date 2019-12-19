from sort_machine import AbstractSortMachine


class BubbleSort(AbstractSortMachine):
    def __init__(self):
        super(BubbleSort, self).__init__()

    def get_data(self, array):
        super().get_data(array)

    def sort(self, array):
        n = len(array)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

