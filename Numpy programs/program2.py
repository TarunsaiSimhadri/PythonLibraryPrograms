"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create a 3x3 matrix with values ranging from 2 to 10.

"""


def convert_array(num_list):

    """

    description:
        This function is used to create a 3x3 matrix with values ranging from 2 to 10.
    
    parameters:
        num_list(array) : num_list that is going to convert into 3*3 matrix using numpy lib.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    matrix = arr.reshape(3, 3)
    print(matrix)
    

def main():

    num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    convert_array(num_list)


if __name__ == "__main__":
    main()