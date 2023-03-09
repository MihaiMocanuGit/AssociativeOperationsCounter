from generator import Generator
from isomorphism import Isomorphism
from itertools import product

class Validator:

    def __init__(self, cardinal_set: int):
        self.__cardinal = cardinal_set
        # used to generate all operations
        self.__generator = Generator(cardinal_set * cardinal_set, cardinal_set)

        # computing the number all existing operations. We will use this to count how many operations to be computed
        # will be left
        self.__no_operations = self.__compute_number_of_operations()
        self.__no_assoc_operations = 0

        # we will use this to generate all isomorphism from a generated semi-group
        self.__isomorphism = Isomorphism(cardinal_set)

        # we calculate this beforehand, it will be used in self.__is_associative. We are actually computing all the ways
        # we can write x*(y*z) using elements from the set
        self.__cartesian_product = list(product(range(self.__cardinal), repeat=3))
    def __compute_number_of_operations(self):
        return (self.__cardinal * self.__cardinal) ** self.__cardinal

    def __is_associative(self) -> bool:
        cartesian_product = self.__cartesian_product
        # (x * y) * z =?= x * (y * z)
        # We use associative_generator to go through all possible groups of <self.__cardinal> elements placed into 3 blocks
        # the first space representing x, the second y and the third z

        operation_map = self.__generator.get_array_ref()
        def getIJ(i:int, j:int):
            return operation_map[i*self.__cardinal + j]

        for grouping in cartesian_product:
            x = grouping[0]
            y = grouping[1]
            z = grouping[2]

            left_side = getIJ(getIJ(x, y), z)
            right_side = getIJ(x, getIJ(y, z))
            if left_side != right_side:
                return False

        return True




    def generate_next_valid(self):
        has_not_finished = self.__generator.generate_next()
        self.__no_operations -= 1

        while has_not_finished and not self.__is_associative():
            has_not_finished = self.__generator.generate_next()
            self.__no_operations -= 1

        return has_not_finished

    def start_generation(self):
        while self.generate_next_valid():
            self.__no_assoc_operations += 1
            yield self.__generator.get_array_ref(), self.__no_assoc_operations



