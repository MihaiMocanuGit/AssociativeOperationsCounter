from generator import Generator
from isomorphism import Isomorphism
import numpy as np

class Validator:

    def __init__(self, cardinal_set: int):
        self.__cardinal = cardinal_set
        self.__generator = Generator(cardinal_set * cardinal_set, cardinal_set)

        self.__no_operations = self.__compute_number_of_operations()
        self.__no_assoc_operations = 0

        self.__isomorphism = Isomorphism(cardinal_set)
    def __compute_number_of_operations(self):
        return (self.__cardinal * self.__cardinal) ** self.__cardinal

    def __is_associative(self) -> bool:
        associative_generator = Generator(3, self.__cardinal)
        # (x * y) * z =?= x * (y * z)
        # We use associative_generator to go through all possible groups of <self.__cardinal> elements placed into 3 blocks
        # the first space representing x, the second y and the third z

        operation_map = self.__generator.get_array_ref()
        def getIJ(i:int, j:int):
            return operation_map[i*self.__cardinal + j]

        has_not_finished = associative_generator.generate_next()

        while has_not_finished:
            x = associative_generator.get_array_ref()[0]
            y = associative_generator.get_array_ref()[1]
            z = associative_generator.get_array_ref()[2]

            left_side = getIJ(getIJ(x, y), z)
            right_side = getIJ(x, getIJ(y, z))
            if left_side != right_side:
                return False

            has_not_finished = associative_generator.generate_next()
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



