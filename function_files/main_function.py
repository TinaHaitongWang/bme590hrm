from function_files.readCSV import importdata
from function_files.dataValidation import is_data_number
from function_files.filter_data import filter_data
from function_files.peak_detection import detect_peak
from function_files.calculate_beats_number_and_beats import calculate_number_beats_and_bests
from function_files.calculate_voltage_extreme_and_duration import calculate_duration, \
    calculate_voltage_extreme
from function_files.calculateMean_hr_bpm import calculate_mean_hr_bpm
from function_files.metrics_dictionary import create_dictionary
import fnmatch
import os


class EcgTest:

    def __init__(self, filename_arg):
        self.filename = filename_arg
        self.data = importdata(self.filename + '.csv')
        self.peaks = None
        self.mean_hr_bpm = None
        self.voltage_extreme = None
        self.time_duration = None
        self.num_beats = None
        self.beats = None

    @classmethod
    def validate_data(cls, data):
        valid_data = is_data_number(data)
        return valid_data

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    @staticmethod
    def filter_input_data(data):
        filtered_data = filter_data(data)
        return filtered_data

    @classmethod
    def find_peaks(cls, data):
        peaks = detect_peak(data)
        return peaks

    def set_peaks(self, peaks):
        self.peaks = peaks

    def get_peaks(self):
        return self.peaks

    @classmethod
    def calculate_bpm(cls, data, peaks, user_input=None):
        mean_bpm = calculate_mean_hr_bpm(data, peaks, user_input)
        return mean_bpm

    def set_mean_bpm(self, mean_bpm):
        self.mean_hr_bpm = mean_bpm

    @classmethod
    def calculate_duration(cls, data):
        duration = calculate_duration(data)
        return duration

    def set_duration(self, duration):
        self.time_duration = duration

    @classmethod
    def calculate_extreme_voltage(cls, data):
        voltage = calculate_voltage_extreme(data)
        return voltage

    def set_voltage_extreme(self, voltage):
        self.voltage_extreme = voltage

    @classmethod
    def calculate_num_beats(cls, data, peaks):
        number_of_beats, beats = calculate_number_beats_and_bests(data, peaks)
        return number_of_beats, beats

    def set_num_beats(self, num_beats):
        self.num_beats = num_beats

    def set_beats(self, beats):
        self.beats = beats

    def generate_metrics(self):
        if not self.peaks:
            print("no peaks")
        elif not self.mean_hr_bpm:
            print("no mean bpm")
        elif not self.voltage_extreme:
            print("no voltage extreme")
        elif not self.time_duration:
            print("no time duration")
        elif not self.num_beats:
            print("no number of beats")
        elif not self.beats:
            print("no beats")
        else:
            create_dictionary(self)


def main_function():
    dirpath = os.path.join(os.getcwd(), 'test_data')
    number_of_csv = len(fnmatch.filter(os.listdir(dirpath), '*.csv'))
    for i in range(number_of_csv):
        print("current file: ", i+1)
        filename = 'test_data' + str(i + 1)
        test = EcgTest(filename)
        valid_data = test.validate_data(test.get_data())
        filtered_data = test.filter_input_data(valid_data)
        peaks_ecg = test.find_peaks(filtered_data)
        test.set_peaks(peaks_ecg)
        bpm = test.calculate_bpm(filtered_data, peaks_ecg)
        test.set_mean_bpm(bpm)
        time_duration = test.calculate_duration(filtered_data)
        test.set_duration(time_duration)
        voltage = test.calculate_extreme_voltage(filtered_data)
        test.set_voltage_extreme(voltage)
        numbeats, beats = test.calculate_num_beats(filtered_data, peaks_ecg)
        test.set_num_beats(numbeats)
        test.set_beats(beats.tolist())
        test.generate_metrics()


if __name__ == '__main__':
    main_function()
