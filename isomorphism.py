from itertools import permutations, product
import numpy as np


class Isomorphism:
    def __init__(self, cardinal_set):
        self.__cardinal = cardinal_set

        # computing all bijective functions as permutations
        self.__bijective_functions = list(permutations(range(cardinal_set)))

        # we calculate this beforehand, it will be used in _______. We are actually computing all the ways
        # we can write x*y using elements from the set (for computing f(xy) = f(x) * f(y))
        self.__cartesian_product = list(product(range(self.__cardinal), repeat=2))

        self.__associative_keys = set()

    def __compute_key(self, nparray):
        # the key will actually be the conversion of the number represented in nparray from base <self.__cardinal> into
        # base 10
        sum = 0
        for i in range(len(nparray)):
            sum += nparray[i] * ((self.__cardinal) ** i)
        return sum

    def __compute_operation_array(self, bij_function, operation_array):
        # we use this for generating all the way to choose x and y for at axiom f(x) * f(y) = f(xy)
        cartesian_product = self.__cartesian_product

        def get_old_at_IJ(i: int, j: int):
            return operation_array[i * self.__cardinal + j]

        new_operation_array = np.full(self.__cardinal * self.__cardinal, fill_value=-1, dtype=np.int8)

        def write_new_at_IJ(i: int, j: int, xy: int):
            new_operation_array[i * self.__cardinal + j] = xy

        for grouping in cartesian_product:
            x = grouping[0]
            y = grouping[1]
            xy = get_old_at_IJ(x, y)

            f_xy = bij_function[xy]
            f_x = bij_function[x]
            f_y = bij_function[y]

            write_new_at_IJ(f_x, f_y, f_xy)

        return new_operation_array

    def compute_isomorphisms(self, operation_array):
        key = self.__compute_key(operation_array)

        # if the given operation was already computed do nothing, otherwise compute all isomorphisms to that operation
        if key in self.__associative_keys:
            return None
        else:
            for bij_function in self.__bijective_functions:
                new_operation = self.__compute_operation_array(bij_function, operation_array)
                new_key = self.__compute_key(new_operation)

                if not key in self.__associative_keys:
                    self.__associative_keys.add(new_key)
                    yield new_operation
