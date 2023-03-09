from validator import Validator
import numpy as np
import time
start_time = time.time()

def transform_array_into_matrix(np_array, cardinal: int):
    return np.reshape(np_array, (cardinal, cardinal), order='C')

def main():
    n = int(input("What is the cardinal of the set?\n>>\t"))
    validator = Validator(n)

    start_time = time.time()
    for operation in validator.start_generation():
        operation_matrix = transform_array_into_matrix(operation[0], n)
        counter = operation[1]
        print(operation_matrix)
        print((n-1)*"\t" + str(counter))
    print("--- %s seconds ---" % (time.time() - start_time))



if __name__ == '__main__':
    main()
