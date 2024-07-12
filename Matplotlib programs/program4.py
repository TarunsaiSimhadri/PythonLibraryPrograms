"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to plot a graph by using given data.

"""


def draw_line(data):

    """

    description:
        This function is used to plot a graph by using given data.
    
    parameters:
        data : gievn data that we are going to plot a graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.DataFrame(data)
    
    plt.plot(df['Date'], df['Close'], label = 'date vs close')
    plt.xlabel('date')
    plt.ylabel('close')
    plt.legend()
    plt.show()  
    

def main():

    data = {
    "Date": ["03-10-16", "04-10-16", "05-10-16", "06-10-16", "07-10-16"],
    "Open": [774.25, 776.030029, 779.309998, 779, 779.659973],
    "High": [776.065002, 778.710022, 782.070007, 780.47998, 779.659973],
    "Low": [769.5, 772.890015, 775.650024, 775.539978, 770.75],
    "Close": [772.559998, 776.429993, 776.469971, 776.859985, 775.080017],
    }
    draw_line(data)


if __name__ == "__main__":
    main()