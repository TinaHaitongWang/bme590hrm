from dataValidation import is_data_number
from readCSV import importdata
import numpy as np
import matplotlib.pyplot as plt


def filter_data(data):
    voltage = data['voltage']
    # remove low frequency data by applying fft and ifft
    fft = np.fft.fft(voltage)
    # plt.plot(fft[1500:11000])
    for i in range(len(fft)):
        if 1200 <= i <= 6500:
            # remove high frequency noise
            fft[i] = 0
    filtered_data = np.fft.ifft(fft)
    filtered_data = filtered_data.real
    data['voltage'] = filtered_data
    return data


if __name__ == '__main__':
    filename = "test_data20.csv"
    test_data = importdata(filename)
    data_valid = is_data_number(test_data)
    data = filter_data(data_valid)
