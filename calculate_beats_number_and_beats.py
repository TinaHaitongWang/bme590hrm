import numpy as np


def calculate_number_beats_and_bests(data, peaks):
    num_beats = len(peaks)
    beats_list = []
    for i in range(len(peaks) - 1):
        beat = data.iloc[peaks[i]]['time']
        beats_list.append(beat)

    beats = np.array(beats_list)
    return num_beats, beats
