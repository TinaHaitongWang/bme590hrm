import pandas as pd
import os
import logging
"""This is a function file Author: Haitong Wang (Tina)"""
""" if the test data is not save in the source path, you
need to update it in the following code """

cwd = os.getcwd()
folderPath = "test_data"


def importdata(file_name):
    """
    this function import data into a dataframe with time and
    voltage
    :param file_name: test data name
    :return: dataframe
    """
    # add exception error
    fullpath = os.path.join(cwd, folderPath, file_name)
    # print(fullpath)
    headers = ['time', 'voltage']
    data = []
    try:
        data = pd.read_csv(fullpath, names=headers)
    except FileNotFoundError:
        logging.error("The file does not exist, please check the path")
    except PermissionError:
        logging.warning("You don't have the permission to open the file")

    # print(data)
    # data.plot()
    # plt.show()
    return data
