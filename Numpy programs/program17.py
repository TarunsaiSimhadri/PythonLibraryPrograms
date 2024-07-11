"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to change datatype.

"""


def change_datatype(num_list):

    """

    description:
        This function is used to change datatype.
    
    parameters:
        None

    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    arr_float = arr.astype(np.float64)
    print(arr_float)
    print(arr_float.dtype)


def main():

    num_list = [[2, 4, 6], [6, 8, 10]]
    change_datatype(num_list)


if __name__ == "__main__":
    main()