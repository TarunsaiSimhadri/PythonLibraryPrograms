"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to add a border (filled with 0's) around an existing array.

"""


def border_zero_matrix():

    """

    description:
        This function is used to add a border (filled with 0's) around an existing array.
            
    parameters:
        None

    return:
        none

    """

    import numpy as np

    arr = np.ones((3, 3), dtype = int)
    rows, cols = arr.shape
    matrix = np.zeros((rows + 2, cols + 2))
    matrix[1:4:, 1:4:] = 1
    print(matrix)


def main():

    border_zero_matrix()


if __name__ == "__main__":
    main()