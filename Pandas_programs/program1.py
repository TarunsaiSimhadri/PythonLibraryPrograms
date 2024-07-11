"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to create and display a one-dimensional array-like object

"""


def onedim_array(num_list):

    """

    description:
        This function is used to create and display a one-dimensional array-like object.
    
    parameters:
        num_list(array) : num_list that is going to convert into a one-dimensional array-like object.
            
    return:
        none

    """

    import pandas as pd
    
    arr = pd.Series(num_list)
    print(arr)
    

def main():

    num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    onedim_array(num_list)


if __name__ == "__main__":
    main()