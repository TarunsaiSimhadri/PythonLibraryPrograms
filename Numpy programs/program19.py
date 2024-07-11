"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to set a lower triangle in a matrix.

"""


def lower_tri():

    """

    description:
        This function is used to set a lower triangle in a matrix.
    
    parameters:
        None

    return:
        none

    """

    import numpy as np
    
    arr = np.zeros((4, 3))
    arr[1, :1] = 1
    arr[2, :2] = 1
    arr[3, ::] = 1
    print(arr)



def main():

    lower_tri()


if __name__ == "__main__":
    main()