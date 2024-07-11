"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to reverse an array (first element becomes last).

"""


def reverse_array(num_list):

    """

    description:
        This function is used to to reverse an array (first element becomes last).
    
    parameters:
        num_list(array) : num_list that is going to into reverse.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    print(arr[::-1])
    

def main():

    num_list = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
    reverse_array(num_list)


if __name__ == "__main__":
    main()