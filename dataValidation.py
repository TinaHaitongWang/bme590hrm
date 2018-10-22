from readCSV import importdata
import pandas as pd


def is_data_number(test_data):
    # remove nan/ empty
    # print(test_data)
    new_data = test_data[pd.to_numeric(test_data.time,
                                       errors='coerce').notnull()]
    test_data2 = new_data[pd.to_numeric(new_data.voltage,
                                        errors='coerce').notnull()]
    # print(test_data2)
    return test_data2


if __name__ == '__main__':
    filename = "test_data32.csv"
    data = importdata(filename)
    is_data_number(data)
