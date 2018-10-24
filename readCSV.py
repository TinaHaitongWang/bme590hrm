import pandas as pd
import os
import matplotlib.pyplot as plt

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

    # print(data)
    # data.plot()
    # plt.show()
    return data
<<<<<<< HEAD


if __name__ == '__main__':
    filename = "test_data30.csv"
    importdata(filename)
=======
>>>>>>> 8c53e0d39c421d364cb70ee74e2e2dccdcb23efc
