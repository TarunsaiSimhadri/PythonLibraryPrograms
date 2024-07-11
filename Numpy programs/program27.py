"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to remove specific elements in a numpy array.

"""


def remove_element(num_list):

    """

    description:
        This function is used to remove specific elements in a numpy array.
    
    parameters:
        num_list(array) : num_list that is going to eliminate specific elements using numpy lib.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    to_eliminate = [0, 3, 4]
    modified_arr = np.delete(arr, to_eliminate)
    print(modified_arr)
    

def main():

    num_list = [10, 20, 30, 20, 40, 50]
    remove_element(num_list)


if __name__ == "__main__":
    main()