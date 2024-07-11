"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to add an extra column to an numpy array.

"""


def add_column(num_list):

    """

    description:
        This function is used to add an extra column to an numpy array.
    
    parameters:
        num_list(array) : num_list that is going to an extra column to an numpy array using numpy lib.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    extra_column = np.array([[100],[200]])

    arr = np.hstack((arr, extra_column))
    print(arr)

def main():

    num_list = [[10, 20,], [40, 50]]
    add_column(num_list)


if __name__ == "__main__":
    main()