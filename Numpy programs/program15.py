"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to program compare two arrays using numpy.

"""


def compare_arrays(num_list1, num_list2):

    """

    description:
        This function is used to program compare two arrays using numpy.
    
    parameters:
        num_list1, num_list2(array) : num_lists that is going to compare two arrays using numpy.
            
    return:
        none

    """

    import numpy as np
    
    a = np.array(num_list1)
    b = np.array(num_list2)

    print("a > b")
    print(a > b)

    print("a >= b")
    print(a >= b)

    print("a < b")
    print(a < b)

    print("a <= b")
    print(a <= b)
    

def main():

    num_list1 = [1, 2]
    num_list2 = [4, 5]
    compare_arrays(num_list1, num_list2)


if __name__ == "__main__":
    main()