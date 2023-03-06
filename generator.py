import numpy
import numpy as np

class Generator:

    def __init__(self, cardinal_of_set: int):
        self.__cardinal = cardinal_of_set

        # we will be "counting" in base |A| = cardinal_of_set. So we set the index to the right-most digit (we consider
        # that the counting will start from 1 and end at |AxA| instead of the usual 0, |AxA| - 1;
        self.__current_digit = self.__cardinal * self.__cardinal - 1

        # I am actually storing the data of the given operation matrix (from the example) into a 1-D array
        # initially all the elements from AxA are mapped into just a1 (which is denoted by its index, 1)
        self.__array_projection = np.full((self.__cardinal * self.__cardinal), 1, dtype=np.int8)
        self.__array_projection[self.__current_digit] = 0



    def __generate_next(self) -> bool:
        # if the addition would result in going over the base, we need to advance towards the next more significant
        # digit and carry the one. Moreover, we have to reset all the less significant digits to their starting value
        # (that being 1)
        while self.__current_digit >= 0 and self.__array_projection[self.__current_digit] == self.__cardinal:
            #TODO: change to python slicing
            for i in range(self.__current_digit,  self.__cardinal * self.__cardinal):
                self.__array_projection[i] = 1
            self.__current_digit -= 1

        # if our current_digit pointer is situatead outside the range of our number, than that means that we've gone
        # through all the possible numbers
        if self.__current_digit == -1:
            return False

        self.__array_projection[self.__current_digit] += 1
        self.__current_digit = self.__cardinal * self.__cardinal - 1
        return True


    def __is_associative(self)-> bool:
        return True

    def transfrom_array_into_matrix(self):
        return numpy.reshape(self.__array_projection, (self.__cardinal, self.__cardinal), order='C')


    def generate_next_valid(self):
        #TODO: implement end case for when we've passed after the last number
        has_finished = self.__generate_next()

        while not self.__is_associative():
             has_finished = self.__generate_next()

        return has_finished


