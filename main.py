from validator import Validator
import time


def main():
    n = int(input("What is the cardinal of the set?\n>>\t"))
    validator = Validator(n)
    counter = 0
    start_time = time.time()
    while validator.generate_next_valid():
        print(validator.transform_array_into_matrix())
        counter += 1
        print((n-1)*"\t", counter)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
