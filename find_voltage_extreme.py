import numpy as np


def calcualte_voltage_extreme(data):
    max_voltage = np.max(data.voltage)
    min_voltage = np.min(data.voltage)
    return max_voltage, min_voltage
