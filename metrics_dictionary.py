import json
import os


def create_dictionary(data):
    metrics = {"Filename": data.filename,
               "Mean HR BPM": data.mean_hr_bpm,
               "Voltage Extreme": data.voltage_extreme,
               "Duration": data.time_duration,
               "Number of Beats": data.num_beats,
               "Beats": data.beats}

    output_metrics_to_json(metrics)


def output_metrics_to_json(metrics):
    cwd = os.getcwd()
    dirpath = os.path.join(cwd, "Metrics_test_data")
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    suffix = '.json'
    outpath = os.path.join(dirpath, metrics["Filename"] + suffix)
    json_metrics = json.dumps(dict)
    write_file = open(outpath, "w")
    write_file.write(json_metrics)
    write_file.close()



