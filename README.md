# bme590hrm
Heart rate monitor project 

[![Build Status](https://travis-ci.com/TinaHaitongWang/bme590hrm.svg?branch=master)](https://travis-ci.com/TinaHaitongWang/bme590hrm)


Author: Haitong Wang 
Date: Oct 20, 2018 

1. Schematic of the project 
      
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
      
      
          
