import matplotlib.pyplot as plt
from function_files.readCSV import importdata
"""This is a utility function file 
Author: Haitong Wang (Tina)
"""


def plot_data(input_data):
    """
    this function plots the data
    :param input_data: ecg data with time and voltage
    :return: plot
    """
    input_data.set_index("time", inplace=True)
    input_data = input_data.astype(float)
    input_data.plot()
    plt.show()


# if __name__ == '__main__':
#     filename = "test_data30.csv"
#     data = importdata(filename)
#     plot_data(data)
