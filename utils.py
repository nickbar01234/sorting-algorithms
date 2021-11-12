#!/usr/bin/env python

__all__ = ["mergeSortRecursion", "quickSort"] 

def mergeSortMerge(array, left, mid, right):
    '''
    The invariant is that the subarrays array[left: mid + 1] and 
    array[mid + 1: right + 1] are sorted. Compare the value between
    each subarrays and copy it over to an auxilary array. Copy
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

def quickSort(array: list, left: int, right: int, method: str = "vanilla"):

    assert method in ["vanilla", "median", "randomized"]
    
    if left < right:
        partition = quickSortPartition(array, left, right, method)
        quickSort(array, left, partition - 1, method)
        quickSort(array, partition + 1, right, method)

def quickSortPartition(array: list, left: int, right: int, method: str):
    
    if method == "vanilla":
        pivot = array[left]

    i = left
    j = right + 1
    while i < j:
        while j > i:
            j -= 1
            if array[j] < pivot:
                array[i] = array[j]
                break
        while i < j:
            i += 1
            if array[i] > pivot:
                array[j] = array[i]
                break
    array[j] = pivot
    return j
        
