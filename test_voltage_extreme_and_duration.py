from calculate_voltage_extreme_and_duration import calculate_duration,\
    calculate_voltage_extreme
import pytest
import numpy
import scipy.signal as signal
import pandas as pd

r_r_interval1 = [1.0, 1.0, 2.0, 1.5, 1.0, 1.5, 2.0, 1.5, 1.5, 2.0]
fs = 8000
ecg = signal.wavelets.daub(10)
signal1 = numpy.concatenate(
    [signal.resample(ecg, int(r * fs)) for r in r_r_interval1])
t1 = numpy.arange(len(signal1)) / fs
d1 = {'time': t1, 'voltage': signal1}
df1 = pd.DataFrame(data=d1)
expected_voltage = [max(signal1), min(signal1)]
expected_duration = max(t1)


def test_voltage_extreme(df1, expected_voltage):
    voltage_max, voltage_min = calculate_voltage_extreme(df1)
    assert voltage_max, voltage_min == expected_voltage


def test_duration(df1, expected_duration):
    duration = calculate_duration(df1)
    assert duration == expected_duration
