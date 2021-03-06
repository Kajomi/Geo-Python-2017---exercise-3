# -*- coding: utf-8 -*-
"""
Prints the temperatures of different temperature classes based on FMI observations from Helsinki Malmi airport station.

Description:
    This script is only a test for a planned version that would read in temperature
    information from a file and allow users to analyze hourly-based temperature observations 
    in the FMI network. 

Note:
    The data has been aggregated from hourly based data into a night-time, day-time and evening time average 
    temperatures. 

Limitations:
    This code will not work if the temperatures are not classified, and the information in Task 3
    are not solved.

Usage:
    ./classify_temperatures.py

Author:
    Henrikki Tenkanen - 19.9.2017

Modified by:
    Mira Kajo - 22.9.2017
"""

# A list of night-time (00-08), day-time (08-16) and evening (16-24) temperatures for April 2013 
# measured in Helsinki Malmi Airport
temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4,
                -2.5, -4.6, 5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8,
                -0.1, -4.7, -5.6, 2.6, -2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4,
                1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,
                3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8,
                4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5,
                4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6,
                -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]

# Task 1 - Create empty lists for different temperature classes
# i.e. freezing, cold, slippery, comfortable, warmish, warm
# -------------------------------------------------------------

# Add your code here.
freezing = []
cold = []
slippery = []
comfortable = []
warmish = []
warm = []


# Task 2 - Iterate over temperatures and add temperatures to different temperature classes
# as defined below:
#  1. Cold --> temperatures below -2 degrees (Celsius)
#  2. Slippery --> temperatures between -2 and +2 degrees (Celsius)
#  3. Comfortable --> temperatures between +2 and +15 degrees (Celsius)
#  4. Warm --> temperatures above +15 degrees (Celsius)
# ------------------------------------------------------------------------------------------

# Add your code here. 
for temp in range(len(temperatures)):
    # create a variable to fetch the value in each index: 
    value = temperatures[temp]
    # initiate a if loop to process/ compare the lists values to specific conditions:
    if value < -2:
        cold.append(value)
    elif (value >= -2) and (value < 2):
        slippery.append(value)
    elif (value >= 2) and (value <=15):
        comfortable.append(value)
    elif value > 15:
        warm.append(value)

# Task 3 - Questions - Print the answers
# --------------------------------------

# 1. How many times was it slippery during the study period?

# Edit these variable (i.e. replace XXX) by finding out how many values are withing different lists
slippery_times = len(slippery)
print("In April 2013 it was slippery ", slippery_times, "times.")

# 2. How many times was it warmish?
warm_times = len(warm)
print("In April 2013 it was warmish ", warm_times, "times.")

# 3. How many times was it cold?
cold_times = len(cold) 
print("In April 2013 it was cold ", cold_times, "times.")



# Task 4 - EXTRA (optional)
# --------------------------

# Data values in the 'temperatures' list are grouped in a way that three values always comprise
# a single day. I.e. 
# The first value in the list is temperature for night-time (00-08) at day 1, 
# the second for day-time (08-16) at day 1, 
# and the third for evening (16-24) temperatures at day 1,
# whereas the fourth value is temperature for night-time (00-08) on the next day (day 2), etc.

# 1. Create empty lists for night, day, and evening temperatures

# Add your code here
night = []
day = []
evening = []

# 2. Iterate over the temperature values and add the temperatures to corresponding lists

# Add your code here
x = 0

for i in range(len(temperatures)):
    
    if  x == 0:
        value = temperatures[i]
        night.append(value) 
        x = 1
         
    elif x == 1:       
        value = temperatures[i]
        day.append(value)          
        x = 2
    
    elif x == 2:
        value = temperatures[i]
        evening.append(value) 
        x = 0     

print('Night values: ', night)
print('Evening values: ', evening)
print('Day values: ', day)

# 3. What was the mean day-time temperature in April 2013?

# Add your code here that answers to the question
mean_temperature = sum(day)/ len(day)
print("Mean day-time temperature was", round(mean_temperature, 1))
                                                         
                                                         
