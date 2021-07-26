import numpy
import sequence

print("cats")

def add_numbers(num_1: int, num_2: int):
    """
    Adds two numbers together.

    :param num_1:
    :param num_2:
    :return:
    """
    print(f'You added: {num_1} and {num_2} = {num_1 + num_2}')
    return num_1 + num_2

if __name__ == "__main__":
    print(add_numbers(1, 3))