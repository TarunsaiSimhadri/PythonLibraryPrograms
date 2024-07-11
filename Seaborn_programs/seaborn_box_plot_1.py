"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw box plot of life expectancy by continent for a data set in the url.

"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def Box_plot():

    """

    description:
        This function is used to draw box plot of life expectancy by continent for a data set in the url.
    
    parameters:
        None  
         
    return:
        none

    """
    
    url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
    data = pd.read_csv(url)
    sns.boxplot(x = "lifeExp", y = "continent", data = data)
    plt.show() 
    

def main():
    Box_plot()


if __name__ == "__main__":
    main()