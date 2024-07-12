"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw point plot of sex against total_bill for a dataset given in the url.

"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def seaborn_voilon_plot():

    """

    description:
        This function is used to draw point plot of sex against total_bill for a dataset given in the url.
    
    parameters:
        None  
         
    return:
        none

    """
    
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    data = pd.read_csv(url)
    sns.violinplot(x = "sex", y = "total_bill", data = data)
    plt.show() 
    

def main():
    seaborn_voilon_plot()


if __name__ == "__main__":
    main()