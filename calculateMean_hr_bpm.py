import numpy as np


def calculate_mean_hr_bpm(data, peaks):
    rr_interval_list = []
    for i in range(len(peaks) - 1):
        upp = data.iloc[peaks[i + 1]]['time']
        low = data.iloc[peaks[i]]['time']
        time = upp - low
        rr_interval_list.append(time)
    beats_in_seconds = np.mean(rr_interval_list)
    mean_hr_bpm = 60 / beats_in_seconds
    return mean_hr_bpm

# if __name__ == '__main__':
#     filename = "test_data3.csv"
#     test_data = importdata(filename)
#     data_valid = is_data_number(test_data)
#     filtered_data = filter_data(data_valid)
#     peaks_real = detect_peak(filtered_data)
#     mean_bpm = calculate_mean_hr_bpm(filtered_data, peaks_real)
