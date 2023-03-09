from itertools import permutations

class Isomorphism:
    def __init__(self, cardinal_set):
        self.__cardinal = cardinal_set
        self.__bijective_functions = list(permutations(range(cardinal_set)))

        self.__associative_keys = set

    def __compute_key(self, nparray):
        # the key will actually be the conversion of the number represented in nparray from base <self.__cardinal> into
        # base 10
        sum = 0
        for i in range(len(nparray)):
            sum += nparray[i]*((self.__cardinal)**i)
        return sum

