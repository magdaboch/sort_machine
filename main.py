from bubble_sort import BubbleSort
from quicksort import QuickSort
from sort_time_complexity import SortTimeComplexity


if __name__ == '__main__':
    array = [1, 5, 63, 72, 9, 34]
    bubble_sorts = BubbleSort()
    bubble_sorts.get_data(array)
    print(bubble_sorts.sort(array))
    quick_sort = QuickSort()
    # quick_sort.get_data()
    sort_machine = SortTimeComplexity()
    print(sort_machine.measure_time(bubble_sorts, array))


