"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to convert a list of numeric value into a one-dimensional NumPy array.

"""


def convert_array(num_list):

    """

    description:
        This function is used to convert a list of numeric value into a one-dimensional NumPy array.
    
    parameters:
        num_list(array) : num_list that is going to convert into array using numpy lib.
        
    return:
        none

    """

    import numpy as np

    arr = np.array(num_list)
    print(arr)
    

def main():

    num_list = [12.23, 13.32, 100, 36.32]
    convert_array(num_list)


if __name__ == "__main__":
    main()