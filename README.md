# Sorting Algorithms Comparison

## Introduction

I implemented *insertion sort*, *merge sort*, two variants of 
*quick sort*, and *heap sort*. I then compared the runtime of different sorting
algorithms.

I also included Python's default sorting implementation - Tim sort - for
comparison. 

## TL;DR 

A few interesting observations. 

1) *Tim-sort* outperformed all my implementations, so you would probably be better off using Python's default sort function. 
2) We say that *traditional quick sort* has worst-case runtime of O(n^2), but on average, it performs very well. 
3) For input size smaller than 50, *insertion sort* is not that bad.
4) *Heap sort* has a small gap with *merge sort* and *quick sort* for large size inputs, but you would be better off using the heap for other purposes than sorting. 

## Algorithm Overview

**Insertion sort**: 
* Best-case - O(n)
* Worst-case - O(n^2)
* Average-case - O(n^2)
* Additional space complexity - O(1)
* Input sensitive: &#x2713;
* In-place: &#x2713;
* Stable: &#x2713;

**Merge sort**:
* Best-case - O(nlog(n))
* Worst-case - O(nlog(n))
* Average case - O(nlog(n))
* Additional space - O(n)
* Input sensitive: &#x2717;
* In-place: &#x2717;
* Stable: &#x2713;

**Quick sort**:
* Best-case - O(nlog(n))
* Worst-case - O(n^2)
* Expected case - O(nlog(n))
* Additional space - O(1)
* Input sensitive: &#x2717;
* In-place: &#x2713;
* Stable: &#x2717;

**Heap sort**:
* Best-case - O(nlog(n))
* Worst-case - O(nlog(n))
* Average-case - O(nlog(n))
* Additional space - O(1)
* Input sensitive: &#x2717;
* In-place: &#x2713;
* Stable: &#x2717;

## Setup 

Create a virtual environment: `python3 -m venv env`

Activate virtual environment: `source env/bin/activate`

Install pre-requisites: `pip install -r requirements.txt`

Tests can be ran in `sorting.ipynb`

## Analysis

### Sorted Input 

![image](https://user-images.githubusercontent.com/74647679/142796139-f1e26ef6-c925-48da-b57b-daf693a6a602.png)

As expected, the time taken for *traditional quick sort* grew with the input size. Because my implementation used the rightmost element as the pivot, no inversions were corrected for a sorted array. The time complexity for this case is O(n^2). In fact, in my tests, input size of around 3000 would throw `RecursionError: maximum recursion depth exceeded while calling a Python object`. 

The gap between other sorting algorithms are neligble for a sorted array. Note that although *heap sort* had no overhead work for building a min-heap in a sorted array, heapifying operation took O(log(n)) time which explained why it took the longest out of the remaining sorting algorithms. I was suprised to see the runtime between *merge sort* and *insertion sort* to be so close, since the former is **input insensitive** and the latter is **input sensitive**. My guess is that the input size was not big enough to see a difference.  

### Reverse Sorted Input

![image](https://user-images.githubusercontent.com/74647679/142798824-9f3a41bf-1040-461d-bfe5-2dfd5156b683.png)

In this test, the time complexity of *traditional quick sort* and *insertion sort* was O(n^2). I had expected the gap in runtime for these algorithms to be smaller, but the graph suggested that the gap would increase as the input size grows. 

For a reverse sorted input, *heap sort* had an overhead work to build a min-heap. The runtime differences between *merge sort*, *randomized quick sort*, and *tim sort* were negligble. 

### Heap Sort Comparison 

![image](https://user-images.githubusercontent.com/74647679/142799231-e30769d4-2421-48f3-a634-057cf5d0fa99.png)

In this test, I compared the runtime for *heap sort* on sorted inputs and reverse sorted inputs. As expected, the gap grew wider with larger input size. 

### Random Input

![image](https://user-images.githubusercontent.com/74647679/142799335-f7b94883-e52b-45a8-94bd-bd3fb8d3bf9d.png)

In this test, I used `numpy` to generate random inputs of size 0 to 2000. *Insertion sort* has an average time complexity of O(n^2), so its runtime for random sets of input were reasonable. It would be interesting to implement *shell sort* in the future to see against radom input sets; *shell sort* is a modified version of insertion sort which is expected to improve its runtime. 

Although we say that *traditional quick sort* has the worst-case time complexity of O(n^2), on average, it performs very well - O(nlog(n)). 

### Small Input

I have been told that for a small set of inputs, *heap sort* should not be used and *insertion sort* would work fine. For this test, I check the runtime of the different sorting algorithms on small sets of input from 0 to 500 elements. 

*Insertion sort* has neglible runtime compared to *merge sort* and *quick sort* for input size smaller than 50. I would say that it is a good choice if the given set is smaller than 50 and is not reverse sorted. From 0 to around 250 elements, *heap sort* took the longest out of all the algorithms I implemented. *Insertion sort* intersected with *heap sort* at around 250 elements. Therefore, for input size greater than 250, *insertion sort* would be a bad choice. 

*Randomized quick sort* is expected to improve the runtime for *quick sort*, but the test showed that *traditional quick sort* outperformed *randomized quick sort*. Of course, this is a pre-mature conclusion because the random indices in the randomized version were generated from a distribution in `np.seed`. In fact, *traditional quick sort* outperformed *merge sort* in this test. So for small input size, *traditional quick sort* is a good choice. 

![image](https://user-images.githubusercontent.com/74647679/142801216-79eafb14-fcf6-463c-97c0-95ccdf36a009.png)

![image](https://user-images.githubusercontent.com/74647679/142801218-1add281a-c846-4b3a-97ee-96a5353f60fa.png)

![image](https://user-images.githubusercontent.com/74647679/142801226-54305660-a2a5-4601-80ff-694ec2545003.png)

![image](https://user-images.githubusercontent.com/74647679/142801229-48c092b9-e073-49a3-a0e5-6e8bffe69505.png)

![image](https://user-images.githubusercontent.com/74647679/142801234-80f5e629-f317-4c8c-b0ff-09d43c59c0ea.png)

## Takeaways 

1) This was realized after the fact, but for a given set of input, the same function call can have different runtime. This can be seen in the random peaks throughout the graphs. For future reference, it would be more accurate to take the average over several trials of the same imput size. 
2) I originally computed the randomized index for *randomized quick sort* within the recursive function call, but this ended up increasing its runtime. I ended up precomputing the randomized index before calling *randomized quick sort*. This improved the runtime dramatically. 
