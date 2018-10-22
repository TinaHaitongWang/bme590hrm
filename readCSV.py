import pandas as pd
import os

cwd = os.getcwd()
folderPath = "test_data/"


def importdata(file_name):
    # add exception error
    fullpath = os.path.join(cwd, folderPath, file_name)
    # print(fullpath)
    headers = ['time', 'voltage']
    data = pd.read_csv(fullpath, names=headers)
    # [pd.read_csv(file) for file in glob.glob(fullpath)]
    # print(data)
    return data


if __name__ == '__main__':
    filename = "test_data1.csv"
    importdata(filename)
