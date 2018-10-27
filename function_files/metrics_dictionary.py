import json
import os
"""This is a generation function file"""


def create_dictionary(data):
    """
    this function creats a dictionary for the metrics
    :param data: data with metrics parameters
    :return: there is not return, it directly generate json file
    """
    metrics = {"Filename": data.filename,
               "Mean HR BPM": data.mean_hr_bpm,
               "Voltage Extreme (mv)": data.voltage_extreme,
               "Duration (s)": data.time_duration,
               "Number of Beats": data.num_beats,
               "Beats time interval": data.beats}
    output_metrics_to_json(metrics)


def output_metrics_to_json(metrics):
    """
    this function writes dictionary to json file and store in
    a new folder
    :param metrics: metrics dictionary contains all values
    :return:writes a json file
    """
    cwd = os.getcwd()
    dirpath = os.path.join(cwd, "Metrics_test_data")
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    suffix = '.json'
    outpath = os.path.join(dirpath, metrics["Filename"] + suffix)
    with open(outpath, 'w') as fp:
        json.dump(metrics, fp, sort_keys=False, indent=4)
