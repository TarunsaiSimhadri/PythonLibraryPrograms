"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to convert a NumPy array into Python list structure.

"""


def convert_list(num_list):

    """

    description:
        This function is used to convert a NumPy array into Python list structure.
    
    parameters:
        num_list(array) : num_list that is going to modify into list.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    list_arr = arr.tolist()
    print(list_arr)

def main():

    num_list = [[0, 1], [2, 3], [4, 5]]
    convert_list(num_list)


if __name__ == "__main__":
    main()