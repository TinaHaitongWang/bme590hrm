"""This is a calculation function file,
.. Author: Haitong Wang (Tina)"""

import numpy as np


def calculate_number_beats_and_bests(data, peaks):
    """
    calculate_number_beats_and_beats function calculates
    number of beats in the ecg data and the corresponding
    time.

    :param data: ecg data with time and voltage
    :param peaks: index of peak location in the ecg data
    :return: number of beats and time of beats occur

    """
    num_beats = len(peaks)
    beats_list = []
    for i in range(len(peaks)):
        beat = data.iloc[peaks[i]]['time']
        beats_list.append(beat)

    beats = np.array(beats_list)
    return num_beats, beats
