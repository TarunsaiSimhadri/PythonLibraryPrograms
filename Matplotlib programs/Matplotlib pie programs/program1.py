"""

@Author: TarunSai
@Date: 2024-07-09
@Last Modified by: 
@Last Modified time:
@Title : Program to display a pie chart of the popularity of programming languages.

"""


def pie_chart(Programming_languages, Popularity):

    """

    description:
        This function is used to display a pie chart of the popularity of programming languages.
    
    parameters:
        None
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array(Programming_languages)
    y = np.array(Popularity)

    plt.pie(y, labels = x)

    plt.show()

def main():
    Programming_languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    Popularity =  [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    pie_chart(Programming_languages, Popularity)


if __name__ == "__main__":
    main()