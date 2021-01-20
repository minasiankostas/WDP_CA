import numpy as np
import itertools


def getWDPCombinations(collection):
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for less in getWDPCombinations(collection[1:]):
        for k, subset in enumerate(less):
            yield less[:k] + [[first] + subset] + less[k + 1:]
        yield [[first]] + less


def getCombinations(items):
    result = [[]]
    for item in items:
        subsets = [subset + [item] for subset in result]
        result.extend(subsets)

    result.pop(0)
    return sorted(result, key=len)


def validate(inputType, inputMessage, errorMessage):
    if inputType == 'int':
        while True:
            try:
                return int(input(inputMessage))
            except ValueError as e:
                print(errorMessage)
    else:
        while True:
            try:
                return float(input(inputMessage))
            except ValueError as e:
                print(errorMessage)


def createArray(a, n):
    array = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            array[i][j] = a[i, j]

    return array


global heapList
heapList = []


def heapPermutation(a, size, n, I):
    global heapList
    if size == 1:
        heapList.append(createArray(I[a], n))
        return

    for i in range(size):
        heapPermutation(a, size - 1, n, I)
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]


# Based on Heap's algorithm -> https://en.wikipedia.org/wiki/Heap%27s_algorithm
def hpArrays(n):
    I = np.identity(n, dtype=int)
    a = np.arange(n)
    heapPermutation(a, n, n, I)
    return np.asarray(heapList)


# Custom permutation function for nxm array
def customPermutation(n, m):
    results = []
    a = np.zeros((n, m))
    for k in range(a.shape[0]):
        for h in range(a.shape[1]):
            a[k][h] = 1
            for i in range(a.shape[0] - 1, -1, -1):
                for j in range(a.shape[1] - 1, -1, -1):
                    if np.sum(a[i]) < 1 and np.sum(a[:, j]) < 1:
                        a[i][j] = 1
                        results.append(a.tolist())
                        a = np.zeros((n, m))
                        a[k][h] = 1

            a = np.zeros((n, m))

    results.sort()
    arrays = []
    for result in list(k for k, _ in itertools.groupby(results)):
        arrays.append(np.asarray(result))

    return np.asarray(arrays)
