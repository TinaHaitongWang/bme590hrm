import pandas as pd
import os

cwd = os.getcwd()
folderPath = "test_data"


def importdata(file_name):
    # add exception error
    fullpath = os.path.join(cwd, folderPath, file_name)
    # print(fullpath)
    headers = ['time', 'voltage']
    data = []
    try:
        data = pd.read_csv(fullpath, names=headers)
    except FileNotFoundError:
        print("The file does not exist, please check the path")
    except PermissionError:
        print("You don't have the permission to open the file")

    # print(data)
    return data


if __name__ == '__main__':
    filename = "test_data70.csv"
    importdata(filename)
