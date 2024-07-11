"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to concatenate two 2d arrays.

"""


def concate_array(num_list):

    """

    description:
        This function is used to concatenate two 2d arrays.
    
    parameters:
        num_list(array) : num_list that is going to eliminate specific elements using numpy lib.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    
    concate_array = np.concatenate(arr, axis=1)
    print(concate_array)
    

def main():

    num_list = [[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
    concate_array(num_list)


if __name__ == "__main__":
    main()