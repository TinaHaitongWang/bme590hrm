from scipy.signal import find_peaks
from function_files.readCSV import importdata
from function_files.dataValidation import is_data_number
from function_files.filter_data import filter_data
import numpy as np
"""This is a function file Author: Haitong Wang (Tina)"""


def detect_peak(section_data):
    """
    this function detects the peak in each QRS complex of the ecg
    data
    :param section_data: data with the time and voltage
    :return: peak index in the data
    """
    # truncate signal into pieces to avoid problem of drifting
    max_voltage = max(section_data['voltage'])
    min_voltage = min(section_data['voltage'])
    if -1 < min_voltage < 0 and \
            abs(max_voltage - min_voltage) > (2 * abs(min_voltage)):
        low_bound = abs(min_voltage) - 0.2
        upp_bound = max_voltage + 0.1
    else:
        low_bound = min_voltage
        upp_bound = max_voltage + 0.1

    range_voltage = [low_bound, upp_bound]  # add 20% to accommedate the
    peaks, _ = find_peaks(section_data.voltage, height=range_voltage)
    # plt.plot(peaks, data.voltage[peaks], '*', color='orange')
    # check if there is secondary peaks
    # take a sample
    len_sample = round(len(section_data) / 20)
    sample_signal = section_data[1:len_sample]
    index_max_sample = np.where(sample_signal.voltage ==
                                min(sample_signal.voltage))
    index_max_sample = [x[0] for x in index_max_sample]
    der = np.diff(
        sample_signal['voltage']
        [index_max_sample[0]:].multiply(0.001)) / \
        np.diff(sample_signal['time'][index_max_sample[0]:])
    bottom = np.where(der == min(der, key=abs))
    least_range = [x[0] for x in bottom]
    real_peaks = []
    for i in range(len(peaks)):
        if i == 0 or i == len(peaks) - 1:  # first and last peak
            first_peak = section_data.iloc[peaks[i]]['voltage']
            if (max_voltage - first_peak) <= (max_voltage / 4):
                real_peaks.append(peaks[i])
            if i == 0:
                last_peak = peaks[i]
        else:
            current_peak = peaks[i]
            if least_range[0] * 2 <= (current_peak - last_peak):
                real_peaks.append(peaks[i])
                last_peak = current_peak

    # plot and verification for tesitng
    # plt.plot(section_data.voltage)
    # plt.plot(peaks, section_data.voltage[peaks], 'o', color='red')
    # plt.plot(real_peaks, section_data.voltage[real_peaks], '*', color='blue')
    # plt.show()
    # print("peaks:", peaks, len(peaks))
    # print("real peaks:", real_peaks, len(real_peaks))
    return real_peaks


# if __name__ == '__main__':
#     filename = "test_data3.csv"
#     test_data = importdata(filename)
#     data_valid = is_data_number(test_data)
#     filtered_data = filter_data(data_valid)
#     peaks = detect_peak(filtered_data)
