from itertools import permutations

class Isomorphism:
    def __init__(self, cardinal_set):
        self.__cardinal = cardinal_set
        self.__bijective_functions = list(permutations(range(cardinal_set)))


