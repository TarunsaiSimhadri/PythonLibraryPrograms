"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array.

"""


def modify_array(num_list):

    """

    description:
        This function is used to create an array of (3, 4) shape, multiply every element value by 3 and display the new array.
    
    parameters:
        num_list(array) : num_list that is going to modify.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list).reshape(3, 4)
    arr = arr*3      
    print(arr)

def main():

    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    modify_array(num_list)


if __name__ == "__main__":
    main()