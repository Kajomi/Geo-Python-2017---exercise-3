# -*- coding: utf-8 -*-
""" Iterating over batch files using for loop.

Usage: 
    ./station_name_generator.py

Author: Mira Kajo, 20.9.2017
"""

#--------------------------------------------------------------------------------
# Performing batch processing on data files using for loop
#--------------------------------------------------------------------------------

# create a variable basename:
basename = 'Station'

# creating the additional strings for the filename:
uscore = '_'
ext = '.txt'

# Create an empty list:
filenames = []

# Iterate over numbers totaling in 20 (as the stop number is excluded the actual number is 21):
for num in range(21):
    # converting the for loop variable 'num' to string so the combination can be performed:
    station_name = basename + uscore + str(num) + ext
    filenames.append(station_name)
    
print(filenames)
