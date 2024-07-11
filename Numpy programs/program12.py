"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to find common values between two arrays.

"""


def common_elements(num_list1, num_list2):

    """

    description:
        This function is used to find common values between two arrays.
    
    parameters:
        num_list1, numlist2(array) : num_lists that is going to find common values between two arrays.
            
    return:
        none

    """

    import numpy as np
    
    common_elements = np.intersect1d(num_list1, num_list2)
    print(common_elements)

def main():

    num_list1 = [0, 10, 20, 40, 60]
    num_list2 = [10, 30, 40]
    common_elements(num_list1, num_list2)


if __name__ == "__main__":
    main()