import pytest
from peak_detection import detect_peak
from calculateMean_hr_bpm import calculate_mean_hr_bpm
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
print(t1[100:700])
print(t2[30:600])


@pytest.mark.parametrize("data, expected_bpm, user_input", [
    (df1, 40),
    (df2, 55),
    (df1, 20, [100, 700]),
    (df2, 20, [30, 400])
])
def test_mean_bpm(data, expected_bpm, user_input=None, ):
    peaks = detect_peak(data)
    bpm = calculate_mean_hr_bpm(data, peaks, user_input)
    assert abs(expected_bpm - bpm) <= 5
