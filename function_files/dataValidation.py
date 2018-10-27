import pandas as pd

"""This is a validation function file 
Author: Haitong Wang (Tina)
"""


def is_data_number(test_data):
    """
    this function examines if the data elements exist, and are numeric
    and are below 300 mv
    :param test_data: ecg data with time and voltage
    :return: vlaid float64 number in dataframe
    """
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

    out_data = out_data[abs(out_data.voltage) <= 300]

    return out_data

# if __name__ == '__main__':
#     filename = "test_data23.csv"
#     data = importdata(filename)
#     is_data_number(data)
