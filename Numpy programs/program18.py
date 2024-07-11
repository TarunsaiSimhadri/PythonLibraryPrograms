"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to print identity matrix.

"""


def identity_matrix():

    """

    description:
        This function is used to print identity matrix.
    
    parameters:
        None

    return:
        none

    """

    import numpy as np
    
    identity_matrix = np.eye(3)
    print(identity_matrix)
    

def main():

    identity_matrix()


if __name__ == "__main__":
    main()