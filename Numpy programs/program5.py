"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to add a border (filled with 1's) around an existing array.

"""


def border_zero_matrix():

    """

    description:
        This function is used to add a border (filled with 1's) around an existing array.
            
    parameters:
        None

    return:
        none

    """

    import numpy as np

    matrix = np.ones((5, 5), dtype = int)
    matrix[1:4:, 1:4:] = 0
    print(matrix)


def main():

    border_zero_matrix()


if __name__ == "__main__":
    main()