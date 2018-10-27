import numpy as np
"""This is a calculation function file 

    Author: Haitong Wang (Tina)

"""


def calculate_mean_hr_bpm(data, peaks, user_input=None):
    """
    this function calculate the mean heart rate beats per minute
    :param data: ecg data with time and voltage
    :param peaks: index of peak location in the ecg data
    :param user_input: user specified time period for calculating
    the bpm, in the form of [starting_time, ending_time]
    :return: beats per minute
    """
    exist_peaks = []
    if user_input:
        try:
            start_time = user_input[0]
            end_time = user_input[-1]
        except IndexError:
            print('No enough user input')

        if end_time <= data['time'].iloc[-1] and \
                start_time <= data['time'].iloc[-1]:
            right_peaks = np.where((data['time'].iloc[peaks] > start_time) &
                                   (data['time'].iloc[peaks] < end_time))
            exist_peaks = [peaks[x] for x in list(right_peaks[0])]
    else:
        exist_peaks = peaks

    rr_interval_list = []
    for i in range(len(exist_peaks)-1):
        upp = data.iloc[exist_peaks[i + 1]]['time']
        low = data.iloc[exist_peaks[i]]['time']
        time = upp - low
        rr_interval_list.append(time)
    beats_in_seconds = np.mean(rr_interval_list)
    mean_hr_bpm = 60 / beats_in_seconds
    return mean_hr_bpm


"""
if __name__ == '__main__':
    filename = "test_data3.csv"
    test_data = importdata(filename)
    data_valid = is_data_number(test_data)
    filtered_data = filter_data(data_valid)
    peaks_real = detect_peak(filtered_data)
    mean_bpm = calculate_mean_hr_bpm(filtered_data, peaks_real)
"""
