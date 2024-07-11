"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to program to append values to the end of an array.

"""


def add_elements(num_list):

    """

    description:
        This function is used to append values to the end of an array.
    
    parameters:
        num_list(array) : num_list that is going to into append some values.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    x = np.append(arr, [40, 50, 60, 70, 80, 90])   
    print(x) 

def main():

    num_list = [10, 20, 30]
    add_elements(num_list)


if __name__ == "__main__":
    main()