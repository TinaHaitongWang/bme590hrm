from readCSV import importData
import pytest
import pandas as pd

# compare the first row and last row of each csv file
test_data1 = pd.DataFrame(data={'time': [0, 27.775], 'voltage': [-0.145, 0.72]}, index=[0, 9999])
test_data5 = pd.DataFrame(data={'time': [0, 27.775], 'voltage': [-0.15, -0.37]}, index=[0, 9999])
test_data17 = pd.DataFrame(data={'time': [0, 13.887], 'voltage': [-0.15, -0.175]}, index=[0, 9999])
test_data23 = pd.DataFrame(data={'time': [0, 39.996], 'voltage': [-0.51, 1.085]}, index=[0, 9999])
test_data28 = pd.DataFrame(data={'time': [0, 27.775], 'voltage': [-0.145, 0.72]}, index=[0, 9999])
test_data29 = pd.DataFrame(data={'time': [0, 13.887], 'voltage': [0.18462, 0.33077]}, index=[0, 9999])
test_data31 = pd.DataFrame(data={'time': [0, 13.887], 'voltage': [-0.0625, -0.0875]}, index=[0, 9999])
test_data32 = pd.DataFrame(data={'time': [0, 13.887], 'voltage': [-243.75, -268.75]}, index=[0, 9999])


@pytest.mark.parametrize("input,expected", [
    ("test_data1.csv", test_data1),
    ("test_data5.csv", test_data5),
    ("test_data17.csv", test_data17),
    ("test_data23.csv", test_data23),
    ("test_data28.csv", test_data28),
    ("test_data29.csv", test_data29),
    ("test_data31.csv", test_data31),
    ("test_data32.csv", test_data32),
])
def test_is_importdata(input, expected):
    output = importData(input)
    output_array = pd.concat([output.head(1), output.tail(1)])
    assert (output_array == expected).all
