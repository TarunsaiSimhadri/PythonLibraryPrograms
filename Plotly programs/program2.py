"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw line and scatter plots for random 100 x and y coordinates.

"""

import plotly.express as px
import numpy as np
def draw_plots():

    """

    description:
        This function is used to draw line and scatter plots for random 100 x and y coordinates.
    
    parameters:
        None  
         
    return:
        none

    """
    
    x_points = np.random.randn(100)
    y_points = np.random.randn(100)
    data = {'x': x_points, 'y': y_points}
    fig1 = px.line(data, x='x', y='y', title='line Plot of 100 Random points')
    fig2 = px.scatter(data, x='x', y='y', title='Scatter Plot of 100 Random points')
    fig1.show() 
    fig2.show()
    

def main():

   draw_plots()


if __name__ == "__main__":
    main()