"""

@Author: TarunSai
@Date: 2024-07-10
@Last Modified by: 
@Last Modified time:
@Title : Program to attach a text label above each bar displaying its popularity (float value).

"""


def bar_chart(languages, popularity):

    """

    description:
        This function is used to attach a text label above each bar displaying its popularity (float value).
    
    parameters:
        languages, popularity (list): data given and that we are going to plot graph.
            
    return:
        none

    """

    import matplotlib.pyplot as plt
    import numpy as np



    x_pos = np.arange(len(languages))

    plt.bar(x_pos, popularity, color='blue')

    for i, pop in enumerate(popularity):
        plt.text(x_pos[i], pop + 0.5, str(pop), ha='center', va='bottom', fontweight='bold')

    plt.xlabel('Languages')
    plt.ylabel('Popularity')
    plt.title('Popularity of Programming Languages')

    plt.show()  


def main():
    languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    bar_chart(languages, popularity)


if __name__ == "__main__":
    main()