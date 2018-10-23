# this function perform peak detection
from scipy.signal import find_peaks, find_peaks_cwt
import matplotlib.pyplot as plt
from readCSV import importdata
from dataValidation import is_data_number
from filter_data import filter_data
import numpy as np


def detect_peak(data, min_voltage, is_secondary_peak):
    plt.plot(data.voltage)
    max_voltage = max(data['voltage'])
    # find the moving average
    # data['rolling_mean_voltage'] = data['voltage'].rolling(window=50).mean()
    range_voltage = [min_voltage, max_voltage]
    peaks, _ = find_peaks(data.voltage, height=range_voltage)
    # correlation check for the
    """"
    signal_range = np.arange(peaks[0], peaks[1])
    sample_signal = data.iloc[signal_range]['voltage']
    corr = np.correlate(sample_signal, data.voltage, mode= "same")
    threshold = np.correlate(sample_signal, sample_signal)
    print(threshold)
    peaks_corr, _ = find_peaks(corr)
    plt.plot(peaks_corr, data.voltage[peaks_corr], "o")
    """
    if is_secondary_peak:
        num = 1
        real_peaks = []
        for i in range(len(peaks)-1):
            if i == 0:# first peak
                if data.iloc[peaks[i]]['voltage'] > data.iloc[peaks[i+1]]['voltage']:
                    # true local maxiumum
                    real_peaks.append(peaks[i])
                    num += 1
            elif i == len(peaks)-1: # last peak
                if real_peaks[-1] != peaks[-2] and data.iloc[peaks[-1]]['voltage'] > data.iloc[peaks[-2]]['voltage']:
                    real_peaks[num] = peaks[-1]

            else:
                if (data.iloc[peaks[i]]['voltage'] > data.iloc[peaks[i+1]]['voltage']) \
                        and (data.iloc[peaks[i]]['voltage'] > data.iloc[peaks[i-1]]['voltage']):
                    real_peaks.append(peaks[i])
                    num += 1
    else: real_peaks = peaks

    #plt.plot(peaks, data.voltage[peaks], '*', color='red')
    #plt.plot(real_peaks, data.voltage[real_peaks], "o")
    plt.show()
    return real_peaks


if __name__ == '__main__':
    filename = "test_data1.csv"
    test_data = importdata(filename)
    data_valid = is_data_number(test_data)
    filtered_data = filter_data(data_valid)
    real_peaks = detect_peak(filtered_data, min_voltage=0, is_secondary_peak=False)
