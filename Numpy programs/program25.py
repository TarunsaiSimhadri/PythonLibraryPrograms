"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to suppresses the use of scientific notation for small numbers in numpy array.

"""


def supress_elements(num_list):

    """

    description:
        This function is used to suppresses the use of scientific notation for small numbers in numpy array.
    
    parameters:
        num_list(array) : num_list that is going to supreess and precision to 3 using numpy lib.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    np.set_printoptions(suppress = True, precision = 3)
    print(arr)

def main():

    num_list = [1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01]
    supress_elements(num_list)


if __name__ == "__main__":
    main()