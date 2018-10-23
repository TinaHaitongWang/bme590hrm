import numpy as np


def calculate_mean_hr_bpm(data,peaks):
    rr_interval_list = []
    for i in range(len(peaks)-1):
        upp = data.iloc[peaks[i+1]]['time']
        low = data.iloc[peaks[i]]['time']
        time = upp-low
        rr_interval_list.append(time)

    mean_hr_bpm = np.mean(rr_interval_list)
    return mean_hr_bpm






