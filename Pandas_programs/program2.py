"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to convert a Panda module Series to Python list and it's type.

"""


def convert_to_list(num_list):

    """

    description:
        This function is used to convert a Panda module Series to Python list and it's type.
    
    parameters:
        num_list(array) : num_list that is going to convert into a series and converting into list.
            
    return:
        none

    """

    import pandas as pd
    
    arr = pd.Series(num_list)
    arr1 = arr.tolist()
    print(arr1, type(arr1))
    

def main():

    num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    convert_to_list(num_list)


if __name__ == "__main__":
    main()