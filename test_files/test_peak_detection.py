from filter_data import filter_data
from readCSV import importdata
from dataValidation import is_data_number
import pytest
from peak_detection import detect_peak


@pytest.mark.parametrize("file_name, expected_num_peaks", [
    ("test_data1.csv", 70),
    ("test_data5.csv", 70),
    ("test_data17.csv", 70),
    ("test_data23.csv", 70),
    ("test_data28.csv", 70),
])
def test_peak_detection(file_name, expected_num_peaks):
    test_data = importdata(file_name)
    data_valid = is_data_number(test_data)
    source = filter_data(data_valid)
    peaks = detect_peak(source)
    num_peaks = len(peaks)
    assert num_peaks <= expected_num_peaks
