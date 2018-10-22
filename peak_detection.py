# this function perform peak detection
from scipy.signal import find_peaks, fftconvolve, general_gaussian
import matplotlib.pyplot as plt
from readCSV import importdata
from dataValidation import is_data_number
from filter_data import filter_data
import numpy as np
import pywavelets as pw


def detect_peak(data):
    '''

    :param data:
    :return:
    max_voltage = max(data['voltage'])
    # find the moving average
    # data['rolling_mean_voltage'] = data['voltage'].rolling(window=50).mean()
    hrw = 0.75
    fs = 1 / (np.mean(np.diff(data.time)))
    move_avg = data['voltage'].rolling(int(hrw*fs)).mean()
    avg_sig = np.mean(data.voltage)
    move_avg = [avg_sig if math.isnan(x) else x for x in move_avg]
    data['moving_avg_voltage'] = [x*1.5 for x in move_avg]
    min_voltage = np.mean(move_avg)
    range_voltage = [min_voltage, max_voltage]
    peaks, _ = find_peaks(data.voltage, height=range_voltage)

    plt.plot(data.voltage)
    plt.plot(move_avg)
    plt.plot(peaks, data.voltage[peaks], "o")
    plt.show()

    '''
    # auto-correlation to fit the curve on the ROI region and then
    # peak detection
    plt.plot(data.voltage)
    sample_rate = 1 / (np.mean(np.diff(data.time)))
    max_bpm = 200
    peak = QRS_detection(data.voltage, sample_rate, max_bpm)
    plt.plot(peak)
    plt.show()


def QRS_detection(signal, sample_rate, max_bpm):
    ## Stationary Wavelet Transform
    coeffs = pw.swt(signal, wavelet="haar", level=2, start_level=0, axis=-1)
    d2 = coeffs[1][1]  ##2nd level detail coefficients

    ## Threhold the detail coefficients
    avg = np.mean(d2)
    std = np.std(d2)
    sig_thres = [abs(i) if abs(i) > 2.0 * std else 0 for i in d2 - avg]

    ## Find the maximum modulus in each window
    window = int((60.0 / max_bpm) * sample_rate)
    sig_len = len(signal)
    n_windows = int(sig_len / window)
    modulus, qrs = [], []

    ##Loop through windows and find max modulus
    for i in range(n_windows):
        start = i * window
        end = min([(i + 1) * window, sig_len])
        mx = max(sig_thres[start:end])
        if mx > 0:
            modulus.append((start + np.argmax(sig_thres[start:end]), mx))

    ## Merge if within max bpm
    merge_width = int((0.2) * sample_rate)
    i = 0
    while i < len(modulus) - 1:
        ann = modulus[i][0]
        if modulus[i + 1][0] - modulus[i][0] < merge_width:
            if modulus[i + 1][1] > modulus[i][1]:  # Take larger modulus
                ann = modulus[i + 1][0]
            i += 1

        qrs.append(ann)
        i += 1
        ## Pin point exact qrs peak
    window_check = int(sample_rate / 6)
    # signal_normed = np.absolute((signal-np.mean(signal))/(max(signal)-min(signal)))
    r_peaks = [0] * len(qrs)

    for i, loc in enumerate(qrs):
        start = max(0, loc - window_check)
        end = min(sig_len, loc + window_check)
        wdw = np.absolute(signal[start:end] - np.mean(signal[start:end]))
        pk = np.argmax(wdw)
        r_peaks[i] = start + pk

    return r_peaks




if __name__ == '__main__':
    filename = "test_data3.csv"
    test_data = importdata(filename)
    data_valid = is_data_number(test_data)
    filtered_data = filter_data(data_valid)
    detect_peak(filtered_data)