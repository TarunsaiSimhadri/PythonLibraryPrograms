"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a scatter plot for a given dataset and show datalabels on hover.

"""

import plotly.express as px
import pandas as pd
def draw_plots():

    """

    description:
        This function is used to draw a scatter plot for a given dataset and show datalabels on hover.
    
    parameters:
        None  
         
    return:
        none

    """
    
    url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"
    data = pd.read_csv(url)
    fig1 = px.line(data, x='Population', y='Rank', hover_name='State')
    fig1.show() 
    

def main():

   draw_plots()


if __name__ == "__main__":
    main()