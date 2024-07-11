"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to find the unique values of two arrays.

"""


def unique_values(num_list1, num_list2):

    """

    description:
        This function is used to find unique values of arrays.
    
    parameters:
        num_list1, num_list2(array) : num_list that is going to to find the unique values of two arrays
            
    return:
        none

    """

    import numpy as np
    
    arr1 = np.array(num_list1)
    arr2 = np.array(num_list2)
    unique_set = np.setxor1d(arr1, arr2)
    print(unique_set)



def main():

    num_list1 = [0, 10, 20, 40, 60, 80]
    num_List2 = [10, 30, 40, 50, 70]
    unique_values(num_list1, num_List2)


if __name__ == "__main__":
    main()