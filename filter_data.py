from dataValidation import is_data_number
from readCSV import importdata
import numpy as np
import matplotlib.pyplot as plt


def filter_data(data):
    voltage = data['voltage']
    # remove low frequency data by applying fft and ifft
    plt.plot(voltage[1:1000])
    fft = np.fft.fft(voltage)
    fft = np.fft.fftshift(fft)
    bandpass_limit = [int(len(fft)/4.5), int(len(fft)/4.5 * 3)]
    # plt.plot(fft)
    for i in range(len(fft)):
        if not bandpass_limit[0] <= i <= bandpass_limit[1]:
            fft[i] = 0
    fft = np.fft.ifftshift(fft)
    filtered_data = np.fft.ifft(fft)
    filtered_data = filtered_data.real
    data['voltage'] = filtered_data
    # plt.plot(filtered_data[1:1000])
    # plt.show()
    return data


if __name__ == '__main__':
    filename = "test_data28.csv"
    test_data = importdata(filename)
    data_valid = is_data_number(test_data)
    data = filter_data(data_valid)
