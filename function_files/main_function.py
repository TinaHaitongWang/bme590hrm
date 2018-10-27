"""This is the main function of the Heart rat monitor project"""
from function_files.readCSV import importdata
from function_files.dataValidation import is_data_number
from function_files.filter_data import filter_data
from function_files.peak_detection import detect_peak
from function_files.calculate_beats_number_and_beats import\
    calculate_number_beats_and_bests
from function_files.calculate_voltage_extreme_and_duration import \
    calculate_duration, calculate_voltage_extreme
from function_files.calculateMean_hr_bpm import calculate_mean_hr_bpm
from function_files.metrics_dictionary import create_dictionary
import fnmatch
import os
import logging


class EcgTest(object):
    """ this is the public of EcgTest, contains all methods to compute the
    metrics
    Only the filename is required to initiate an instance of the EcgTest class.
    Other parameters are assigned and used through set_ and get_ methods
    """

    def __init__(self, filename_arg):
        """this is the initial function
        :param filename_arg: input the filename for the test_data
        """
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
        """
        this function validate data
        :param data: data output from importdata function,
        ..  input ecg data with time and voltage
        :return: valid_data is data without any non-numeric, blank, over 300 mv
        ..  datapoints

        """
        valid_data = is_data_number(data)
        return valid_data

    def set_data(self, data):
        """
        this function set data
        :param data: input ecg data with time and voltage
        :return: assign data to "data" parameter
        """
        self.data = data

    def get_data(self):
        """
        this function get data
        :return: get data from outside the class
        """
        return self.data

    @staticmethod
    def filter_input_data(data):
        """
        this is a static function only for filter noisy data
        :param data: ecg data with time and voltage
        :return: filtered data without ultra-high frequency
        .. and love frequency
        """
        filtered_data = filter_data(data)
        return filtered_data

    @classmethod
    def find_peaks(cls, data):
        """
        this function to detect the prak of QRS complex in the
        .. ecg data
        :param data: ecg data with time and voltage
        :return: index of peak in the ecg data
        """
        peaks = detect_peak(data)
        return peaks

    def set_peaks(self, peaks):
        """
        this function set peaks from outside of class
        :param peaks: index of peak in the ecg data
        :return: assign peak index as a parameter of the class
        """
        self.peaks = peaks

    def get_peaks(self):
        """
        this function is to get peak parameter
        :return: peak parameter of the class
        """
        return self.peaks

    @classmethod
    def calculate_bpm(cls, data, peaks, user_input=None):
        """
        this function calculate the mean bpm of the given
        .. data, when there is not user_input for specific
        .. time frame, the default is to use the entire
        .. dataset. If user specify the time, then it only
        .. use the time to calculate the bpm

        :param data: ecg data with time and voltage
        :param peaks: index of peak of QRS complex
        :param user_input: array of [start_time, end_time]
        :return: mean_bpm, average beats per minute over the
        .. given time
        """
        mean_bpm = calculate_mean_hr_bpm(data, peaks, user_input)
        return mean_bpm

    def set_mean_bpm(self, mean_bpm):
        """
        this function is to set mean_bpm
        :param mean_bpm: average beats per minute over the given time
        :return: set mean_bpm as the parameter of the EcgTest class
        """
        self.mean_hr_bpm = mean_bpm

    @classmethod
    def calculate_duration(cls, data):
        """
        this function calculate the duration of the ecg data
        :param data: ecg data with time and voltage
        :return: time duration of the data
        """
        duration = calculate_duration(data)
        return duration

    def set_duration(self, duration):
        """
        this function set the duration as parameter of the class
        :param duration: time duration of the data
        :return: instance with parameter of duration
        """
        self.time_duration = duration

    @classmethod
    def calculate_extreme_voltage(cls, data):
        """
        this function calculate extreme voltage values
        :param data: ecg data with time and voltage
        :return: array of [maximum voltage, minimum voltage]
        """
        voltage = calculate_voltage_extreme(data)
        return voltage

    def set_voltage_extreme(self, voltage):
        """
        this function sets the extreme voltage parameters
        :param voltage: array of [maximum voltage, minimum voltage]
        :return: instance with parameter of extreme voltage
        """
        self.voltage_extreme = voltage

    @classmethod
    def calculate_num_beats(cls, data, peaks):
        """
        this function calculate the number of beats
        :param data: ecg data with time and voltage
        :param peaks: index of peak of QRS complex
        :return: number of beats and corresponding starting time
                and end time
        """
        number_of_beats, beats = calculate_number_beats_and_bests(data, peaks)
        return number_of_beats, beats

    def set_num_beats(self, num_beats):
        """
        this function sets the number of beats parameter
        :param num_beats: number of beats detect in the data
        :return: instance with parameter of number of beats
        """
        self.num_beats = num_beats

    def set_beats(self, beats):
        """
        this function sets the beats time
        :param beats: array of starting and ending time of each beat occurred
        :return: instance with parameter of beats time
        """
        self.beats = beats

    def generate_metrics(self):
        """
        this function is to generate metric dictionary for the instance
        :return: it dones't need return, it generate a output json file in
                designated location
        """
        if not self.peaks:
            logging.warning("no peaks")
        elif not self.mean_hr_bpm:
            logging.warning("no mean bpm")
        elif not self.voltage_extreme:
            logging.warning("no voltage extreme")
        elif not self.time_duration:
            logging.warning("no time duration")
        elif not self.num_beats:
            logging.warning("no number of beats")
        elif not self.beats:
            logging.warning("no beats")
        else:
            create_dictionary(self)


def main_function():
    """
    this is the main function that evoke the EcgTest class for each instance
    user needs to update the filename and filepath to run other data
    :return: json file in the folder named Metrics_test_data under the
            same directory
    """
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
    """ this is the intial function call the main function"""
    main_function()
