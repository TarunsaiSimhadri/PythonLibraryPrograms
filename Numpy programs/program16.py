"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to change the data type of an array.

"""


def flatten_array(num_list):

    """

    description:
        This function is used to change the data type of an array.
    
    parameters:
        num_list(array) : num_list that is going to change data type using numpy lib.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    matrix = arr.reshape(2, 3)
    print(matrix)
    flattened = matrix.reshape(-1)
    print(flattened)
    

def main():

    num_list = [10, 20, 30, 20, 40, 50]
    flatten_array(num_list)


if __name__ == "__main__":
    main()