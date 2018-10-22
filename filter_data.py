from dataValidation import is_data_number
from readCSV import importdata
import numpy as np


def filter_data(data):
    voltage = data['voltage']
    # remove low frequency data by applying fft and ifft
    fft = np.fft.fft(voltage)
    #plt.plot(fft[1500:11000])
    for i in range(len(fft)):
        if 1200 <= i <= 6500:
            # remove high frequency noise
            fft[i] = 0
    filtered_data = np.fft.ifft(fft)
    filtered_data = filtered_data.real
    #plt.plot(voltage[1:1000])
    #plt.plot(data_remove_low[1:1000])
    #plt.show()
    data['voltage'] = filtered_data
    return data


if __name__ == '__main__':
    filename = "test_data1.csv"
    test_data = importdata(filename)
    data_valid = is_data_number(test_data)
    filter_data(data_valid)