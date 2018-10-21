import pandas as pd
import os
import glob

cwd = os.getcwd()
folderPath = "test_data/"
# filename = "test_data1.csv"

def importData(filename):
    # add exception error
    fullpath = os.path.join(cwd, folderPath, filename)
    # print(fullpath)
    headers = ['time', 'voltage']
    data = pd.read_csv(fullpath, names=headers)
    # [pd.read_csv(file) for file in glob.glob(fullpath)]
    # print(data)
    return data


if __name__ == '__main__':
    importData(filename)


