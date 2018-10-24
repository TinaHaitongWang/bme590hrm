from readCSV import importdata
import pandas as pd


def is_data_number(test_data):
    # print(test_data)
    new_data = test_data[pd.to_numeric(test_data.time,
                                       errors='coerce').notnull()]
    out_data = new_data[pd.to_numeric(new_data.voltage,
                                      errors='coerce').notnull()]

    if out_data.time.dtype == 'object':
        out_data = out_data.copy()
        out_data.loc[:, 'time'] = out_data['time'].apply(pd.to_numeric,
                                                         errors='ignore')
    if out_data.voltage.dtype == 'object':
        out_data.loc[:, 'voltage'] = out_data['voltage'].apply(pd.to_numeric,
                                                               errors='ignore')
    return out_data


if __name__ == '__main__':
    filename = "test_data30.csv"
    data = importdata(filename)
    is_data_number(data)
