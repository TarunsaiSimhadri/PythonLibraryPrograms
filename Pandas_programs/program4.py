"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to get the powers of an array values element-wise.

"""


def perform_multiply(num_list):

    """

    description:
        This function is used to get the powers of an array values element-wise.

    parameters:
        num_list(array) : num_list that is going to get the powers of an array values element-wise.
            
    return:
        none

    """

    import pandas as pd
    
    arr = []
    arr1 = pd.Series(num_list)
    def operation(x):
        return x**3
    for i in arr1:
        arr.append(operation(i))
    arr3 = pd.Series(arr)
    print(arr3)      
    

def main():

    num_list = [0, 1, 2, 3, 4, 5, 6]
    perform_multiply(num_list)


if __name__ == "__main__":
    main()