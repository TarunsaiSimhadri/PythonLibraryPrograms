"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to change into immutable.

"""


def immutable_array(num_list):

    """

    description:
        This function is used to change into immutable.
    
    parameters:
        None

    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    arr.flags.writeable = False

    print("array is converted into immutable")

    try:
        arr[0] = 10
    except ValueError as e:
        print(e)



def main():

    num_list = [2, 4, 6, 8, 10]
    immutable_array(num_list)


if __name__ == "__main__":
    main()