#!/usr/bin/env python
import numpy as np

__all__ = ["mergeSortRecursion", "quickSort", "MinHeap"] 

np.random.seed(42)

def mergeSortRecursion(array: list, left: int, right: int):
    '''
    Recursively subdivide the array, sort subarrays, and merge sorted
    subarrays.
    '''

    if left < right:
        mid = (left + right) // 2
        mergeSortRecursion(array, left, mid)
        mergeSortRecursion(array, mid + 1, right)
        mergeSortMerge(array, left, mid, right)

def mergeSortMerge(array, left, mid, right):
    '''
    The invariant is that the subarrays array[left: mid + 1] and 
    array[mid + 1: right + 1] are sorted. Compare the value between
    each subarrays and copy it over to an auxilary array. Finally, copy
    the auxilary array over to the original input.
    '''

    i = left
    j = mid + 1
    aux = []
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            aux.append(array[i])
            i += 1
        else:
            aux.append(array[j])
            j += 1

    aux.extend(array[i:mid + 1])
    aux.extend(array[j:right + 1])
    array[left:right + 1] = aux

def quickSort(array: list, left: int, right: int, method: str = "vanilla"):
    '''
    Partition the array around an element in the array. Recursively sort the subarrays.
    '''

    assert method in ["vanilla", "randomized"]
    
    if left < right:
        partition = quickSortPartition(array, left, right, method)
        quickSort(array, left, partition - 1, method)
        quickSort(array, partition + 1, right, method)

def quickSortPartition(array: list, left: int, right: int, method: str):
    '''
    Keep track of the index of next element larger than the pivot. 
    Loop through the array from left to right, if 
    '''
    
    if method == "randomized":
        random = np.random.randint(left, right + 1, 1)[0]
        array[random], array[right] = array[right], array[random]

    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i] 
    
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

    def heapSort(self):
        '''
        Pop the first element from the array and push into a new array. 
        Swap the first element with the element at the index we're considering.
        Finally, reheapify. The loop breaks when index equals to 0. 
        '''

        sorted_array = []
        while self.array[self.index] != None:
            sorted_array.append(self.array[1])
            self.array[1] = self.array[self.index]
            self.index -= 1
            self.__heapify(1)

        return sorted_array

    def __buildHeap(self):
        '''
        Build heap bottom up. 
        '''

        for i in reversed(range(1, self.index // 2 + 1)):
            self.__heapify(i)

    def __heapify(self, i: int):
        '''
        Recursively restore the heap invariant. Swap the value at the current
        index with the smallest of its two children. Recurse on the index
        with the smaller value.
        '''

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
