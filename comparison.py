#!/usr/bin/env python

'''
Implementations are written in sorting.py.

Note that arrays in Python are pass by reference.
'''


from sorting import *

import pathlib
import time
import matplotlib.pyplot as plt

__all__ = ["Comparison"] 

class Comparison:
    def __init__(self, output: str = ""):
        '''
        If output is provided, then a directory is created.
        The generated graphs are saved to this output.
        '''
        self.runtime = {} 
        self.output = None
        if output != "":
            self.output = pathlib.Path(output)
            self.output.mkdir(parents = True, exist_ok = True)

    def __call__(self, numbers: list, title: str, figtitle: str):
        '''
        Run tests on set of inputs and plot graphs. 

        Params
            * numbers - Numbers to be tested.
            * title - Title of the figure. 
            * figtitle - Filename of the exported graph. 
        '''

        # x coordinate
        x = []
        for number in numbers:
            x.append(len(number))

            insertion = self.insertionSort(numbers = number)
            merge = self.mergeSort(numbers = number)
            vanilla = self.quickSortVanilla(numbers = number)
            randomized = self.quickSortRandomized(numbers = number)
            heap = self.heapSort(numbers = number)
            tim = self.timSort(numbers = number)
        
        # Plot graph
        runtime = self.runtime
        self.__plot(runtime, x, title, figtitle)
        # Clear runtime after test.
        self.runtime = {}
        
        return runtime

    def __plot(self, runtime: dict,  x: list, title: str, figtitle: str = ""):
        '''
        Helper function to plot graphs.

        Param
            * runtime - Each key contains a list of runtime for n inputs. 
            * x - The x coordinate of the plot.
        '''

        colors = ['b', 'g', 'r', 'c', 'm', 'y']

        fig, ax = plt.subplots(figsize = (12, 7))
        for color, (algorithm, runtime) in enumerate(runtime.items()):
            ax.plot(x, runtime, label = algorithm, color = colors[color])

        ax.set(title = title, xlabel = "Elements (n)", ylabel = "Runtime (s)") 
        ax.legend(loc = "best")
        plt.tight_layout()
        plt.show()
        
        if self.output == None and figtitle != "":
            print(f"Expected to save graph but provided output directory of {self.output}")
        elif self.output != None and figtitle != "":
            output = str(self.output / figtitle)
            print(f"Saving output to {output}")
            fig.savefig(output) 

    def __timer(fnc):
        '''
        Decorator to record the runtime.
        '''
        def wrapper(self, *args, **kwargs):

            start = time.time()
            sorted_array = fnc(self, kwargs["numbers"])
            end =  time.time()
            
            assert sorted_array == sorted(kwargs["numbers"]), \
               f"{fnc.__name__} has incorrect output"

            if fnc.__name__ not in self.runtime:
                self.runtime[fnc.__name__] = []
            self.runtime[fnc.__name__].append(end - start)

            return sorted_array

        return wrapper

    @__timer
    def insertionSort(self, numbers: list):

        to_sort = numbers.copy()
        insertionSort(to_sort)
        
        return to_sort

    @__timer
    def mergeSort(self, numbers: list):

        to_sort = numbers.copy()
        mergeSortRecursion(to_sort, 0, len(to_sort) - 1)

        return to_sort

    @__timer
    def quickSortVanilla(self, numbers: list):
        
        to_sort = numbers.copy()
        quickSort(to_sort, 0, len(to_sort) - 1)
        return to_sort

    @__timer
    def quickSortRandomized(self, numbers: list):

        to_sort = numbers.copy()
        quickSort(to_sort, 0, len(to_sort) - 1, method = "randomized")
        
        return to_sort

    @__timer
    def heapSort(self, numbers: list):
        
        heap = MinHeap(numbers)
        return heap.heapSort()

    @__timer
    def timSort(self, numbers: list):
        '''
        Base comparison for the sorting algorithms implemented. Python uses
        Tim sort.
        '''

        to_sort = numbers.copy()
        return sorted(to_sort)

def generator(i):
    '''
    Helper function to create test set. 
    '''
    return list(np.random.randint(-100000, 100000, i))
            
if __name__ == "__main__":
    '''
    NOTE: Check function __timer inside Comparison to see assertion for output.
    If the function call returns, then the sorted output is correct. I 
    assumed that Python sorted function is implemented correctly. 
    '''

    import numpy as np 
    np.random.seed(42)

    sorted_case = list(range(800))
    reverse_sorted_case = list(reversed(range(800)))
    comparison = Comparison()

    print("Begin tests for insertion sort")
    _ = comparison.insertionSort(numbers = sorted_case)
    _ = comparison.insertionSort(numbers = reverse_sorted_case)
    for i in range(1000):
        random = generator(i)
        _ = comparison.insertionSort(numbers = random)
    print(f"Finish tests for insertion sort\n{'*' * 10}")

    print("Begin tests for merge sort")
    _ = comparison.mergeSort(numbers = sorted_case)
    _ = comparison.mergeSort(numbers = reverse_sorted_case)
    for i in range(1000):
        random = generator(i)
        _ = comparison.mergeSort(numbers = random)
    print(f"Finish tests for merge sort\n{'*' * 10}")

    print("Begin tests for traditional quick sort")
    _ = comparison.quickSortVanilla(numbers = sorted_case)
    _ = comparison.quickSortVanilla(numbers = reverse_sorted_case)
    for i in range(1000):
        random = generator(i)
        _ = comparison.quickSortVanilla(numbers = random)
    print(f"Finish tests for traditional quick sort\n{'*' * 10}")

    print("Begin tests for randomized quick sort")
    _ = comparison.quickSortRandomized(numbers = sorted_case)
    _ = comparison.quickSortRandomized(numbers = reverse_sorted_case)
    for i in range(1000):
        random = generator(i)
        _ = comparison.quickSortRandomized(numbers = random)
    print(f"Finish tests for randomized quick sort\n{'*' * 10}")

    print("Begin tests for building a min heap")
    print("Building a min heap on a sorted input")
    small_sorted_case = list(range(10))
    heap = MinHeap(small_sorted_case)
    print(f"Before: {small_sorted_case}")
    print(f"After: {heap}")
    
    print("Building a min heap on a reverse sorted input")
    small_reverse_sorted_case = list(reversed(range(10)))
    heap = MinHeap(small_reverse_sorted_case)
    print(f"Before: {small_reverse_sorted_case}")
    print(f"After: {heap}")

    print("Building a min heap with odd cardinality")
    odd_cardinality = generator(15)
    heap = MinHeap(odd_cardinality)
    print(f"Before: {odd_cardinality}")
    print(f"After: {heap}")
    print(f"Finish tests for building a min heap\n{'*' * 10}")

    print(f"Begin tests for heap sort")
    _ = comparison.heapSort(numbers = sorted_case)
    _ = comparison.heapSort(numbers = reverse_sorted_case)
    for i in range(1000):
        random = generator(i)
        _ = comparison.heapSort(numbers = random)
    print(f"Finish tests for heap sort\n{'*' * 10}")

    print("All tests have completed...exiting the program")
