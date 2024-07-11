"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to find to size, itemsize, byte of array.

"""


def properties_of_array(num_list):

    """

    description:
        This function is used to find to size, itemsize, byte of array.
    
    parameters:
        num_list : num_lists that is going to find to size, itemsize, byte of array.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    arr_size = arr.size
    arr_item_size = arr.itemsize
    arr_bytes = arr.nbytes

    print("size of the array:", arr_size)
    print("Length of one array element in bytes:", arr_item_size)
    print("Total bytes consumed by the elements of the array:", arr_bytes)



def main():

    num_list = [0, 10, 20, 40, 60]
    properties_of_array(num_list)


if __name__ == "__main__":
    main()