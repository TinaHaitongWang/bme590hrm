import numpy as np
"""This is a calculation function file 
Author: Haitong Wang (Tina)
"""


def calculate_voltage_extreme(data):
    """
    this function calculate the maximum and minimum voltage
    with the ecg data
    :param data: ecg data with time and voltage
    :return: maximum and minimum voltage
    """
    max_voltage = np.max(data.voltage)
    min_voltage = np.min(data.voltage)
    return max_voltage, min_voltage


def calculate_duration(data):
    """
    this function calculates the time span of ecg data
    :param data: ecg data with time and voltage
    :return: total time of the data
    """
    return data['time'].iloc[-1]
