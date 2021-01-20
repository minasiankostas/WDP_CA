import numpy as np


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

    print(bids)