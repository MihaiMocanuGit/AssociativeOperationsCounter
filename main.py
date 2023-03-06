from generator import Generator


def main():
    generator = Generator(4)
    while generator.generate_next_valid():
        print(generator.transfrom_array_into_matrix())
        print()


if __name__ == '__main__':
    main()
