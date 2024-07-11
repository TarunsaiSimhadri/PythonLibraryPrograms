"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to print array values with precision 3.

"""


def modify_array(num_list):

    """

    description:
        This function is to used print array values with precision 3:
    
    parameters:
        num_list(array) : num_list that is going to modify using numpy lib.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    round_arr = np.round(arr, 3)
    print(round_arr)


def main():

    num_list = [0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349, 0.35399976, 0.99469633, 0.0694458, 0.54711478]
    modify_array(num_list)


if __name__ == "__main__":
    main()