import pytest
from function_files.peak_detection import detect_peak
from function_files.calculate_beats_number_and_beats import calculate_number_beats_and_bests
import numpy
import scipy.signal as signal
import pandas as pd

r_r_interval1 = [1.0, 1.0, 2.0, 1.5, 1.0, 1.5, 2.0, 1.5, 1.5, 2.0]
r_r_interval2 = [2.0, 2.0, 2.0, 2.0, 1.0, 2.5, 2.5, 1.0]
fs = 8000
ecg = signal.wavelets.daub(10)
signal1 = numpy.concatenate(
    [signal.resample(ecg, int(r * fs)) for r in r_r_interval1])
signal2 = numpy.concatenate(
    [signal.resample(ecg, int(r * fs)) for r in r_r_interval2])
t1 = numpy.arange(len(signal1)) / fs
t2 = numpy.arange(len(signal2)) / fs
d1 = {'time': t1, 'voltage': signal1}
df1 = pd.DataFrame(data=d1)
d2 = {'time': t2, 'voltage': signal2}
df2 = pd.DataFrame(data=d2)
peaks1 = detect_peak(df1)
peaks2 = detect_peak(df2)
num_beats1 = len(peaks1)
num_beats2 = len(peaks2)
expected_beats1 = [df1['time'].iloc[peaks1[0]], df1['time'].iloc[peaks1[-1]]]
expected_beats2 = [df2['time'].iloc[peaks2[0]], df2['time'].iloc[peaks2[-1]]]


@pytest.mark.parametrize("data, peaks, expected_num_beats, expected_beats", [
    (df1, peaks1, num_beats1, expected_beats1),
    (df2, peaks2, num_beats2, expected_beats2)

])
def test_peak_detection(data, peaks, expected_num_beats, expected_beats):
    num_beats, beats = calculate_number_beats_and_bests(data, peaks)
    print(beats)
    beats = [beats[0], beats[-1]]
    assert num_beats == expected_num_beats
    assert beats == expected_beats
