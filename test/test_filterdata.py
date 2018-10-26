from filter_data import filter_data
from readCSV import importdata
from dataValidation import is_data_number
import numpy as np
import random


def test_is_filter_data_valid():
    filename = "test_data28.csv"
    test_data = importdata(filename)
    data_valid = is_data_number(test_data)
    source = filter_data(data_valid)
    sample = len(source)
    noise = 0.000000000000008*np.asarray(random.sample(range(0, sample),
                                                       sample))
    source.voltage = source.voltage + noise
    filtered = filter_data(source)
    corr = filtered.voltage.corr(source.voltage)
    assert corr >= 0.95
