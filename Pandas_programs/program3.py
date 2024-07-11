"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to perform arthmetic operation on two panda series.

"""


def arthmetic_operations(num_list1, num_list2):

    """

    description:
        This function is used to perform arthmetic operation on two panda series.
    
    parameters:
        num_list1, num_list2(array) : num_lists that are going to perform operations.
            
    return:
        none

    """

    import pandas as pd
    
    series1 = pd.Series(num_list1)
    series2 = pd.Series(num_list2)

    add = series2 + series1
    sub = series1 - series2
    mul = series2 * series1
    div = series1 / series2

    print("add :", add ,"sub :", sub, "mul :", mul, "div : ", div)         
    

def main():

    num_list1 = [2, 4, 6, 8, 10]
    num_list2 = [1, 3, 5, 7, 9]
    arthmetic_operations(num_list1, num_list2)


if __name__ == "__main__":
    main()