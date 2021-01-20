import numpy as np
import operator
from functions import *

if __name__ == '__main__':
    N = validate('int', 'Number of items: ', 'Please give an integer!')
    combinations = getCombinations(range(1, N + 1))
    bidders = validate('int', 'Number of bidders: ', 'Please give an integer!')
    bids = np.zeros((len(combinations), bidders))
    for bIndex, column in enumerate(bids.T):
        print(f'Bidder {bIndex + 1}')
        for i in range(len(column)):
            bid = validate('float', f'Combination {combinations[i]}: ', 'Only numbers!')
            column[i] = bid

    WDPCombinationsMax = []
    subset = list(range(1, N + 1))
    for WDPCombination in getWDPCombinations(subset):
        combinationList = []
        for value in WDPCombination:
            for cIndex, cValue in enumerate(combinations):
                if value == cValue:
                    combinationList.append(bids[cIndex])

        combinationArray = np.asarray(combinationList)
        if combinationArray.shape[0] == combinationArray.shape[1]:
            permutations = hpArrays(combinationArray.shape[0])
            perms = {}
            for pIndex, permutation in enumerate(permutations):
                permutationSum = 0
                perms[pIndex] = {'details': []}
                for i in range(permutation.shape[0]):
                    for j in range(permutation.shape[1]):
                        if permutation[i][j] == 1:
                            perms[pIndex]['details'].append({
                                'bidder': j + 1,
                                'combination': WDPCombination[i]
                            })
                            permutationSum += combinationArray[i][j]

                    perms[pIndex]['sum'] = permutationSum

            # Find max
            maxSum = -1
            maxIndex = 0
            for index, value in enumerate(perms):
                if perms[value]['sum'] > maxSum:
                    maxSum = perms[value]['sum']
                    maxIndex = index

            WDPCombinationsMax.append(perms[maxIndex])
        elif len(combinationArray) != 1:
            permutations = customPermutation(combinationArray.shape[0], combinationArray.shape[1])
            perms = {}
            for pIndex, permutation in enumerate(permutations):
                permutationSum = 0
                perms[pIndex] = {'details': []}
                for i in range(permutation.shape[0]):
                    for j in range(permutation.shape[1]):
                        if permutation[i][j] == 1:
                            perms[pIndex]['details'].append({
                                'bidder': j + 1,
                                'combination': WDPCombination[i]
                            })
                            permutationSum += combinationArray[i][j]

                perms[pIndex]['sum'] = permutationSum

            # Find max
            maxSum = -1
            maxIndex = 0
            for index, value in enumerate(perms):
                if perms[value]['sum'] > maxSum:
                    maxSum = perms[value]['sum']
                    maxIndex = index

            WDPCombinationsMax.append(perms[maxIndex])
        else:
            perms = {'details': [{
                'bidder': combinationArray.argmax() + 1,
                'combination': WDPCombination
            }], 'sum': max(combinationArray[0])}

            WDPCombinationsMax.append(perms)

    # Find final max
    maxSum = -1
    maxIndex = 0
    for index, combination in enumerate(WDPCombinationsMax):
        if combination['sum'] > maxSum:
            maxSum = combination['sum']
            maxIndex = index

    finalMax = WDPCombinationsMax[maxIndex]
    print(f"Winner: bidder {finalMax['details'][0]['bidder']} with combination {finalMax['details'][0]['combination']} and profit {finalMax['sum']}.")
