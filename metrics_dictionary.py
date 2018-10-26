import json
import os


def create_dictionary(data):
    metrics = {"Filename": data.filename,
               "Mean HR BPM": data.mean_hr_bpm,
               "Voltage Extreme (mv)": data.voltage_extreme,
               "Duration (s)": data.time_duration,
               "Number of Beats": data.num_beats,
               "Beats time interval": data.beats}
    output_metrics_to_json(metrics)


def output_metrics_to_json(metrics):
    cwd = os.getcwd()
    dirpath = os.path.join(cwd, "Metrics_test_data")
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    suffix = '.json'
    outpath = os.path.join(dirpath, metrics["Filename"] + suffix)
    with open(outpath, 'w') as fp:
        json.dump(metrics, fp, sort_keys=False, indent=4)




