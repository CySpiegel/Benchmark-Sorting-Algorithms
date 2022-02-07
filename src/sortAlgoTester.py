# Matthew Stroble
# Program: This program attempts verify sorting algorithm time complexities on a given range of array sizes
# Methodology: Program will generate either a random array, or an array in descending order that will be timed
# across every sorting algorithm to be tested. Every sorting algorithm will tested on the exact same generated array
# for every array size that is tested. Program start from defined array start size and works up to the array max size
# that is defined in the settings.
import random
import sys
import copy
from timeit import default_timer as timer
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

from quickSort import *
from insertionSort import *
from heapSort import *
from bubbleSort import *
from mergeSort import *
from selectionSort import *


# Generate Random array of integers by giving it a size
def randArrayGenerator(size):
    randList = []
    for i in range(size):
        randList.append(random.randint(1, sys.maxsize))
    return randList

# put array in decending order (worst case)
def decendingArray(size):
    decList = []
    num = size
    for i in range(size):
        decList.append(num)
        num -= 1
    return decList

# calculate average time
def whatsMyAvrage(A):
    tally = 0
    for value in A:
        tally += value
    return tally/len(A)


# maximum elament
def maxElement(A):
    maxElement = 0
    for i in A:
        if i < maxElement:
            maxElement = i
    return maxElement


if __name__ == "__main__":

    # Settings - Adjust if needed
    # sets the size of the starting array to be tested
    arrayStart = 0

    # last array size to be tested
    arrayMax = 100000

    # Repeats tests on array size, higher number will produce better statistical average for every array size tested
    repeateTest = 100

    # How much to grow the array for the next set of array size to be tested
    stepSize = 10000

    # Y-axis time scale for output graph, if array size being tested < 1000 use 0.01 if arrayMax > 5000 use 1
    # TODO allows system to auto set time scale based on arrayMax.
    timeScaleFactor = 1

    # Sorting Algorithms to test True, pass False
    testBubbleSort = False
    testInsertionSort = False
    testSelectionSort = False
    testMergeSort = True
    testHeapSort = True
    testQuickSort = True
    testMaxElement = True
    testQuickSort3way = False
    testTimSort = True

    # TODO implement a switch case for array generator, worst case, random case, simisorted, mostly sorted
    # Array Generator Mode 0 = random array from [0, sys,maxsize], 1 = descending array, default to mode 0
    generatorMode = 0

    # TODO Settings - DEBUG options for each sorting algorithm to verify random input to sorted output.
    quickSortDebug = False
    insertionSortDebug = False
    # end of settings

    # NO EDITING BELOW THIS LINE UNLESS YOU ARE ADDING AN ALGORITHM TO THE TEST
    # Storing average computed time per array step
    runRange = []
    quicksortAvg = []
    insertionsortAvg = []
    maxelementAvg = []
    heapsortAvg = []
    bubblesortAvg = []
    mergesortAvg = []
    selectionSortAvg = []
    quickSort3wayAvg = []
    timsortAvg = []

    arrayUsed = ""


    if generatorMode == 2:
        print("Array Generator set to mode 2\nGenerating array in descending order")
    else:
        print("Array Generator in mode 1\nGenerating random arrays")

    # Program main loop, driver for testing
    for i in range(arrayStart, arrayMax + 1, stepSize):
        runRange.append(i)

        # inital clear for each run
        # Quicksort init
        quicksortTime = []
        quicksortArraySizeTime = []

        # insertionsort
        insertionsortTime = []
        insertionsortArraySizeTime = []

        # maxelament
        maxelamentTime = []
        maxelamentArraySizeTime = []

        # heapSort
        heapsortTime = []
        heapsortArraySizeTime = []

        # bubbleSort
        bubblesortTime = []
        bubblesortArraySizeTime = []

        # Merge Sort
        mergesortTime = []
        mergesortArraySizeTime = []

        # Selection Sort
        selectionsortTime = []
        selectionsortArraySizeTime = []

        # Quick Sort 3 way
        quicksort3wayTime = []
        quicksort3wayArraySizeTime = []

        # Tim Sort
        timsortTime = []
        timesortArraySizeTime = []

        print("Testing Array Size", i)
        for j in range(repeateTest):
            if generatorMode == 0:
                # generate a random array
                masterArray = randArrayGenerator(i)
                arrayUsed = "Random Element [0,sys.maxsize]"
            elif generatorMode == 1:
                masterArray = decendingArray(i)
                arrayUsed = "Elements in descending order, worst case"
            else:
                masterArray = randArrayGenerator(i)
                arrayUsed = "Generator out of range defaulting to Random Element [0,sys.maxsize]"

            # QuickSort
            if testQuickSort:
                test = [x for x in masterArray]
                if quickSortDebug:
                    print("Quick Sort \n Unsorted", test)
                n = len(test) - 1
                start = timer()
                quickSort(test, 0, n)
                end = timer()
                if quickSortDebug:
                    print("Quick Sort \n Sorted", test)
                quicksortArraySizeTime.append(end - start)

            # Insertion Sort
            if testInsertionSort:
                test = [x for x in masterArray]
                if insertionSortDebug:
                    print("Insertion Sort \n UnsortedArray", test)
                start = timer()
                insertionSort(test)
                end = timer()
                if insertionSortDebug:
                    print("Sorted Array", test)
                insertionsortArraySizeTime.append(end - start)

            # Max Element
            if testMaxElement:
                test = [x for x in masterArray]
                start = timer()
                maxElement(test)
                end = timer()
                maxelamentArraySizeTime.append(end - start)

            # Heap Sort
            if testHeapSort:
                test = [x for x in masterArray]
                start = timer()
                heapSort2(test)
                end = timer()
                heapsortArraySizeTime.append(end - start)

            # Merge Sort
            if testMergeSort:
                test = [x for x in masterArray]
                start = timer()
                mergeSort(test, 0, len(test) - 1)
                end = timer()
                mergesortArraySizeTime.append(end - start)

            # Bubble Sort
            if testBubbleSort:
                test = [x for x in masterArray]
                start = timer()
                bubbleSort(test)
                end = timer()
                bubblesortArraySizeTime.append(end - start)

            # Selection Sort
            if testSelectionSort:
                test = [x for x in masterArray]
                start = timer()
                selectionSort(test)
                end = timer()
                selectionsortArraySizeTime.append(end - start)

            if testTimSort:
                test = [x for x in masterArray]
                start = timer()
                sorted(test)
                end = timer()
                timesortArraySizeTime.append(end - start)


        # Computing average time for current test for given sorting algorithms
        if testQuickSort:
            quicksortAvg.append(whatsMyAvrage(quicksortArraySizeTime))
        if testInsertionSort:
            insertionsortAvg.append(whatsMyAvrage(insertionsortArraySizeTime))
        if testMaxElement:
            maxelementAvg.append(whatsMyAvrage(maxelamentArraySizeTime))
        if testHeapSort:
            heapsortAvg.append(whatsMyAvrage(heapsortArraySizeTime))
        if testBubbleSort:
            bubblesortAvg.append(whatsMyAvrage(bubblesortArraySizeTime))
        if testMergeSort:
            mergesortAvg.append(whatsMyAvrage(mergesortArraySizeTime))
        if testSelectionSort:
            selectionSortAvg.append(whatsMyAvrage(selectionsortArraySizeTime))
        if testTimSort:
            timsortAvg.append(whatsMyAvrage(timesortArraySizeTime))


    # outside of loops
    if testBubbleSort:
        plt.plot(runRange, bubblesortAvg, 'c-', label='Bubble Sort')
    if testSelectionSort:
        plt.plot(runRange, selectionSortAvg, 'c--', label='Selection Sort')
    if testMergeSort:
        plt.plot(runRange, mergesortAvg, 'm-', label='Merge Sort')
    if testHeapSort:
        plt.plot(runRange, heapsortAvg, 'g-', label='Heap Sort')
    if testQuickSort:
        plt.plot(runRange, quicksortAvg, 'r-', label='Quicksort')
    if testInsertionSort:
        plt.plot(runRange, insertionsortAvg, 'y-', label='Insertion Sort')
    if testMaxElement:
        plt.plot(runRange, maxelementAvg, 'b-', label='Max Element')
    if testTimSort:
        plt.plot(runRange, timsortAvg, 'm--', label='Tim Sort')

    plt.axis([arrayStart, arrayMax, 0, timeScaleFactor])
    plt.xlabel(arrayUsed)
    plt.ylabel("Time from default_timer (walltime)")
    plt.title("Matthew Stroble")
    plt.legend(loc='upper left', shadow=False, fontsize='small')
    plt.show()



