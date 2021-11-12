#!/usr/bin/env python

from utils import *

import time
import matplotlib.pyplot as plt
import numpy as np 

__all__ = ["Comparison"] 

class Comparison:
    def __init__(self):
        self.runtime = {} 

    def __timer(fnc):
        '''
        Decorator to record the runtime.
        '''
        def wrapper(self, *args, **kwargs):

            start = time.time()
            sorted_array = fnc(self, kwargs["numbers"])
            end =  time.time()
            
            #assert sorted_array == sorted(kwargs["numbers"]), \
            #       f"{fnc.__name__} has incorrect output"

            if fnc.__name__ not in self.runtime:
                self.runtime[fnc.__name__] = []
            self.runtime[fnc.__name__].append(end - start)

            return sorted_array

        return wrapper

    @__timer
    def insertionSort(self, numbers: list):
        '''
        Loop through array starting at index 1. While the number at the 
        index is greater than the previous index, swap the number at the 
        previous index to the current index and decrement index. Finally,
        assign the original number to the new value of index.
        '''

        to_sort = numbers.copy()
        for i in range(1, len(to_sort)):
            current = numbers[i]
            while i >= 1 and current < to_sort[i - 1]:
                to_sort[i] = to_sort[i - 1]
                i -= 1
            to_sort[i] = current
        
        return to_sort

    @__timer
    def mergeSort(self, numbers: list):
        '''
        Subdivide the array and sort the subarrays. Merge the sorted subarrays.
        Note that arrays are passed by reference. Implementation of merge sort
        is done in utils.py.
        '''

        to_sort = numbers.copy()
        mergeSortRecursion(to_sort, 0, len(to_sort) - 1)

        return to_sort

    @__timer
    def quickSortVanilla(self, numbers: list):
        
        to_sort = numbers.copy()
        quickSort(to_sort, 0, len(to_sort) - 1)
        
        return to_sort
