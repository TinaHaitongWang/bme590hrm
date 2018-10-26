# BME 590 Heart Rate Monitor Project 
 
[![Build Status](https://travis-ci.com/TinaHaitongWang/bme590hrm.svg?branch=master)](https://travis-ci.com/TinaHaitongWang/bme590hrm)

##### Author: Haitong Wang (Tina)
##### Date: Oct 20, 2018 

----

_This is a project for BME 590 Medical Device Development class. The goal of this 
project is to analyze an unknown electrocardiography to understand heart's activity 
over a period of time. We compute mean heart rate BPM, maximum and minimum
lead voltage, duration of ECG, number of beats, and the time when a beat takes place. 
Besides the technical analysis, this project also emphasizes on git control and unit
testing._

-----
**1.1 Content**

_Folders and Files Required to Run the Applications_

`bme590hrm` 
    
      |___function_files
 
      |___test_data
  
      |___test_files
      
      |___.travis.yml
      
      |___README.md
      
      |___requirement.txt
      
_Following table contains all functional files for this application_

 | Function name                       | Unit test                            |
 |-------------------------------------|--------------------------------------|
 | main_function.py                    | test_json_output.py                  |
 | dataValidation.py                   | test_dataValidation.py               |
 | filter_data.py                      | test_filterdata.py                   |
 | peak_detection.py                   | test_peak_detection.py               |
 | metrics_dictionary.py               | test_json_output.py                  |
 | calculateMean_hr_bpm.py             | test_calculate_mean_hr_bpm.py        |
 | calculate_beats_number_and_beats.py | test_voltage_extreme_and_duration.py |
 | plot_data.py                        |                                      |       
---
**1.2 Instruction for use the program**

    1.2.1 Download all requirement files including function_files, test_files and test_data
          and requirement files 
    1.2.2 Install all requirement package 
    1.2.3 Run main_function.py in the function_files folder (if you want to run the function
          using data provided, otherwise please update the file name and file path in the 
          main_function.py )
    1.2.4 Resultant json files should be stored under the same path in the folder called 
          Metrics_test_data in the orginial .csv file name
    1.2.5 for pytest, please use the following code to avoid subdirectory problem
            python -m pytest test_files -v --pep8 
          
    Note: for calculating mean bpm, user can specify the length of data to calculate bpm. 
          Default setting has not input on that part. 

---
**1.3 Schematic**
    1.1 Import data 
  
    1.2 Data verification 
  
    1.3 Data Processing 
        
        1.3.1 mean_hr_bpm: estimated average heart rate over a user-specified number of minutes (can choose a default        interval) 
          
        1.3.2 Unit testing for mean_hr_bpm
          
        1.3.3 voltage_extremes: tuple containing minimum and maximum lead voltages
          
        1.3.4 Unit testing for voltage_extremes 
          
        1.3.5 duration: time duration of the ECG strip
          
        1.3.6 Unit testing for duration
          
        1.3.7 num_beats: number of detected beats in the strip
          
        1.3.8 Unit testing for num_beats
          
        1.3.9 beats: numpy array of times when a beat occurred
          
        1.3.10 Unit testing for beats
      
    1.5 Generate Output, metrics dics ---> JSON file 
      
      
          
