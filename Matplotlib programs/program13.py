"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot a graph and customize with given customizations using given data.

"""


def draw_plot(data):

    """

    description:
        This function is used to plot a graph and customize with given customizations using given data.
    
    parameters:
        data : gievn data that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.DataFrame(data)
    
    plt.plot(df['Date'], df['Close'], linewidth = 0.5, color = 'blue')
    plt.grid(True, linestyle = '--')
    plt.xlabel('Date')
    plt.ylabel('Closing Value')
    plt.title('Closing Value of Stock between October 3, 2016 to October 7, 2016')
    plt.show()  
    

def main():

    data = {
    "Date": ["03-10-16", "04-10-16", "05-10-16", "06-10-16", "07-10-16"],
    "Close": [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
    }
    draw_plot(data)


if __name__ == "__main__":
    main()