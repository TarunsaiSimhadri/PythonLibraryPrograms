"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to convert a list and tuple into arrays.

"""


def convert_to_array(num_list, num_tuple):

    """

    description:
        This function is used to convert a list and tuple into arrays.
    
    parameters:
        num_list : num_lists that is going to convert a list and tuple into arrays.
            
    return:
        none

    """

    import numpy as np
    
    arr_list = np.array(num_list)
    arr_tuple = np.array(num_tuple)
    print("list to tuple:", arr_list)
    print("tuple to list:") 
    print(arr_tuple)


def main():

    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    num_tuple = ((8, 4, 6), (1, 2, 3))
    convert_to_array(num_list, num_tuple)


if __name__ == "__main__":
    main()