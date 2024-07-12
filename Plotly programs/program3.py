"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a scatter plot for random 500 x and y coordinates and style it

"""

import plotly.express as px
import numpy as np
def draw_plots():

    """

    description:
        This function is used to draw a scatter plot for random 500 x and y coordinates and style it
    
    parameters:
        None  
         
    return:
        none

    """
    
    x_points = np.random.randn(100)
    y_points = np.random.randn(100)
    data = {'x': x_points, 'y': y_points}
    fig1 = px.line(data, x='x', y='y', title='line Plot of 1000 Random points')
    fig1.update_traces(marker=dict(size=8,  # Marker size
                              color='orange',  # Marker color
                              opacity=0.6,  # Marker opacity
                              line=dict(width=1, color='DarkSlateGray')  # Marker border width and color
                              ),
                  selector=dict(mode='markers'))  # Selecting the marker mode
    fig1.update_layout(
    xaxis_title='X-axis',  # X-axis label
    yaxis_title='Y-axis',  # Y-axis label
    title_font_size=20,  # Title font size
    title_font_family='Arial'  # Title font family
    )
    fig1.show() 
    

def main():

   draw_plots()


if __name__ == "__main__":
    main()