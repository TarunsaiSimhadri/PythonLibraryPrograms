"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create a null vector of size 10 and update sixth value to 11.

"""


def update_array():

    """

    description:
        This function is used to create a null vector of size 10 and update sixth value to 11.
    
    parameters:
        None

    return:
        none

    """

    import numpy as np
    
    null_vector = np.zeros(10)
    null_vector[5] = 11
    print(null_vector)
    

def main():

    update_array()


if __name__ == "__main__":
    main()