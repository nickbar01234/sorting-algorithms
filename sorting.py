#!/usr/bin/env python
import numpy as np

__all__ = ["insertionSort", "mergeSortRecursion", "quickSort", "MinHeap"] 

np.random.seed(42)

def insertionSort(array: int):

    # While the current value is greater than the value at the previous index. Assign
    # the value at the previous index to the current index. After exiting while 
    # loop, assign the value at index with current value.
    for i in range(1, len(array)):
        current = array[i]
        while i >= 1 and current < array[i - 1]:
            array[i] = array[i - 1]
            i -= 1
        array[i] = current

def mergeSortRecursion(array: list, left: int, right: int):

    # Subdivide the array while left and right have not crossed. 
    # Sort the subarrays. 
    if left < right:
        mid = (left + right) // 2
        mergeSortRecursion(array, left, mid)
        mergeSortRecursion(array, mid + 1, right)
        mergeSortMerge(array, left, mid, right)

def mergeSortMerge(array, left, mid, right):

    # Tracks the start of the left subarray.
    i = left
    # Tracks the start of the right subarray.
    j = mid + 1
    # Auxiliary to copy the elements in sorted order.
    aux = []
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            aux.append(array[i])
            i += 1
        else:
            aux.append(array[j])
            j += 1

    # Copy the left over elements in the left subarray.
    aux.extend(array[i:mid + 1])
    # Copy the left over elements in the right subarray
    aux.extend(array[j:right + 1])
    # Copy the elements in the auxilary array to the original array.
    array[left:right + 1] = aux

def quickSort(array: list, left: int, right: int, method: str = "vanilla"):
    assert method in ["vanilla", "randomized"]
    
    # Partition the array around the pivot when left has not crossed right.
    # Recurse on the two subarrays around the partition.
    if left < right:
        partition = quickSortPartition(array, left, right, method)
        quickSort(array, left, partition - 1, method)
        quickSort(array, partition + 1, right, method)

def quickSortPartition(array: list, left: int, right: int, method: str):
    
    # If method is randomized, pick a random index in range [left, right].
    # swap array[right] and array[random]. 
    if method == "randomized":
        random = np.random.randint(left, right + 1, 1)[0]
        array[random], array[right] = array[right], array[random]

    pivot = array[right]
    # i keep tracks of the index before the next element that is larger than 
    # the pivot
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i] 
    
    # Swap the pivot with the next element larger than the pivot.
    array[i + 1], array[right] = pivot, array[i + 1]

    return i + 1

class MinHeap:
    '''
    Min heap data structure ensures that at any node, it's value is the smallest
    in the subtree. 
    '''

    def __init__(self, numbers: list):
        
        # Store the data from index 1 to simplify the calculation when
        # heapifying.
        self.array = [None, *numbers.copy()]

        # Index indicates the range of values in the array to consider when
        # applying heap sort.
        self.index = len(self.array) - 1

        self.__buildHeap()

    def __str__(self):
        return str(self.array)

    def heapSort(self):

        # Pop the first element from the Heap and push into a new array.
        # Swap the first element of the Heap with the last element of the Heap.
        # Decrement the size of the Heap and reheapify.
        sorted_array = []
        while self.array[self.index] != None:
            sorted_array.append(self.array[1])
            self.array[1] = self.array[self.index]
            self.index -= 1
            self.__heapify(1)

        return sorted_array

    def __buildHeap(self):

        # Build heap bottom-up 
        for i in reversed(range(1, self.index // 2 + 1)):
            self.__heapify(i)

    def __heapify(self, i: int):

        # Base case 1 - Current index is out of range.
        if i > self.index:
            return
        
        left = i * 2
        right = i * 2 + 1

        # Base case 2 - No children.
        current = self.array[i]
        left_child = self.array[left] if left <= self.index else np.Inf
        right_child = self.array[right] if right <= self.index else np.Inf

        # Recursive case 1 - Left smaller than current.
        if left_child <= right_child and left_child < current:
            self.array[left], self.array[i] = current, left_child
            self.__heapify(left)
        # Recursive case 2 - Right smaller than current.
        elif right_child < current:
            self.array[right], self.array[i] = current, right_child
            self.__heapify(right)
