"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw bar plot of sex against survived for a dataset given in the url.

"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def seaborn_bar_plot():

    """

    description:
        This function is used to draw bar plot of sex against survived for a dataset given in the url.
    
    parameters:
        None  
         
    return:
        none

    """
    
    url = "https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv"
    data = pd.read_csv(url)
    sns.barplot(x = "sex", y = "survived", data = data)
    plt.show() 
    

def main():
    seaborn_bar_plot()


if __name__ == "__main__":
    main()