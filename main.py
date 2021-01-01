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
    N = validate('int', 'N: ', 'Please give an integer!')
    combinations = getCombinations(range(1, N + 1))
    continueInput = True
    bidderCount = 1
    bidders = {}
    while continueInput:
        print(f'Bidder {bidderCount}: ')
        bidders[f'bidder_{bidderCount}'] = {}
        for item in combinations:
            bidd = validate('float', f'{item}: ', 'Only numbers!')
            bidders[f'bidder_{bidderCount}'][f'{str(item)}'] = bidd

        while True:
            answer = input('Continue? y/n\n')
            if answer == 'y' or answer == 'n':
                break
            else:
                print("'y' for yes or 'n' for no.")

        if answer == 'n':
            continueInput = False
        else:
            bidderCount += 1

print(bidders)
