import matplotlib.pyplot as plt
from readCSV import importdata


def plot_data(input_data):
    input_data.set_index("time", inplace=True)
    input_data = input_data.astype(float)
    input_data.plot()
    plt.show()


if __name__ == '__main__':
    filename = "test_data30.csv"
    data = importdata(filename)
    plot_data(data)
