"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.

"""


def plot():

    """

    description:
        This function is used to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
.
    
    parameters:
        None
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    with open('../test.txt', 'r') as file:
        data = file.readlines()

    x = []
    y = []
    for line in data:
        line = line.strip()
        if line:
            values = line.split()
            x.append(float(values[0]))
            y.append(float(values[1]))  
    plt.plot(x,y)

    plt.show()

def main():
    plot()


if __name__ == "__main__":
    main()