import numpy as np

class Generator:

    def __init__(self, length_of_group: int, cardinal_set: int):
        self.__length_group = length_of_group
        self.__cardinal = cardinal_set

        # we will be "counting" in base |A| = cardinal_of_set. So we set the index to the right-most digit
        self.__current_digit = self.__length_group - 1

        # I am actually storing the data of the given operation matrix (from the example) into a 1-D array
        # initially all the elements from AxA are mapped into just a0 (which is denoted by its index, 0)
        self.__array_projection = np.zeros(self.__length_group, dtype=np.int8)
        self.__array_projection[self.__current_digit] = -1



    def generate_next(self) -> bool:
        # if the addition would result in going over the base's max value , we need to advance towards the next more significant
        # digit and carry the one. Moreover, we have to reset all the less significant digits to their starting value
        # (that being 0)
        while self.__current_digit >= 0 and self.__array_projection[self.__current_digit] == self.__cardinal - 1:
            #TODO: change to python slicing
            for i in range(self.__current_digit, self.__length_group):
                self.__array_projection[i] = 0
            self.__current_digit -= 1

        # if our current_digit pointer is situatead outside the range of our number, than that means that we've gone
        # through all the possible numbers
        if self.__current_digit == -1:
            return False

        # we increase the value by one
        self.__array_projection[self.__current_digit] += 1

        #and we move the current_digit pointer back to the end (in the case we actually had to carry at least a one)
        self.__current_digit = self.__length_group - 1
        return True

    def get_array_ref(self):
        return self.__array_projection





