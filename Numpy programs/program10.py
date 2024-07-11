"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to find the real and imaginary parts of an array of complex numbers.

"""


def real_imaginary(num_list):

    """

    description:
        This function is used to find the real and imaginary parts of an array of complex numbers.
    
    parameters:
        num_list : num_lists that is going to find the real and imaginary parts of an array of complex numbers.
            
    return:
        none

    """

    import numpy as np
    
    arr = np.array(num_list)
    real_part = np.real(arr)
    print(real_part)
    imag_part = np.imag(arr)
    print(imag_part) 


def main():

    num_list = [ 1.00000000+0.j, 0.70710678+0.70710678j]
    real_imaginary(num_list)


if __name__ == "__main__":
    main()