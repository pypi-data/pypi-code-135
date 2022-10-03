def bubbleSort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x+1
        for i in range(1,n-x):
            if arr[i-1]>arr[i]:
                swap(i-1, i)
                swapped = True
    return arr
def insertionSort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos>0 and arr[pos-1]>cursor:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = cursor
    return arr
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr
def countingSort(arr):
    maxEl = max(arr)
    countArrayLen = maxEl+1
    countArr = [0]*countArrayLen
    sizeArr = len(arr)
    for el in arr:
        countArr[el] += 1
    for i in range(1,countArrayLen):
        countArr[i] += countArr[i-1]
    outArr = [0]*sizeArr
    i = sizeArr-1
    while i>=0:
        currentEl = arr[i]
        countArr[currentEl] -= 1
        newValue = countArr[currentEl]
        outArr[newValue] = arr[i]
        i -= 1
    return outArr
def countingSortForRadix(arr, placeValue):
    countArray = [0]*10
    inputSize = len(arr)
    for i in range(inputSize):
        placeElement = (arr[i] // placeValue)%10
        countArray[placeElement] += 1
    for i in range(1,10):
        countArray[i] += countArray[i-1]
    outputArray = [0]*inputSize
    i = inputSize-1
    while i>=0:
        currentEl = arr[i]
        placeElement = (arr[i]//placeValue)%10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1
    return outputArray
def radixSort(arr):
    maxEl = max(arr)
    D = 1
    while maxEl>0:
        maxEl /= 10
        D += 1
    placeVal = 1
    outputArray = arr
    while D>0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10
        D -= 1
    return outputArray