"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a scatter plot for random 1000 x and y coordinates

"""

import plotly.express as px
import numpy as np
def scatter_plot():

    """

    description:
        This function is used to draw a scatter plot for random 1000 x and y coordinates
    
    parameters:
        None  
         
    return:
        none

    """
    
    x_points = np.random.randn(100)
    y_points = np.random.randn(100)

    # data = {'x': x_points, 'y': y_points}
    fig = px.scatter(x = x_points, y = y_points, title='Scatter Plot of 1000 Random points')
    fig.show() 
    

def main():

   scatter_plot()


if __name__ == "__main__":
    main()