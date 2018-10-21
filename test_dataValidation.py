from dataValidation import is_data_number
from readCSV import importData
import pytest


@pytest.mark.parametrize("input,expected", [
    ("test_data1.csv", 10000),
    ("test_data5.csv", 10000),
    ("test_data17.csv", 10000),
    ("test_data23.csv", 10000),
    ("test_data28.csv", 9998),
    ("test_data29.csv", 9998),
    ("test_data31.csv", 9996),
    ("test_data32.csv", 10000),
])
def test_is_data_number(input, expected):
    testdata = importData(input)
    output = is_data_number(testdata)
    len = output.shape[0]
    assert len == expected