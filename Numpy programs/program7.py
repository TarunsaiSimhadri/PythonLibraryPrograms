"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create a 8x8 matrix and fill it with a checkerboard pattern.

"""


def checkBoardPattern_matrix():

    """

    description:
        This function is used to create a 8x8 matrix and fill it with a checkerboard pattern.

    parameters:
        None

    return:
        none

    """

    import numpy as np

    matrix = np.zeros((8, 8), dtype=int)
    matrix[1::2, ::2] = 1
    matrix[::2, 1::2] = 1

    print(matrix)


def main():

    checkBoardPattern_matrix()


if __name__ == "__main__":
    main()