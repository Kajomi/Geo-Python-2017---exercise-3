# Exercise 3 - `for` loops and conditional statements

The exercise for this week is meant to help you to understand `for` loops and conditional statements in Python.
Below you have a series of problems in which you are asked to create (or edit) script files and write the code necessary to produce the desired results.
After making your changes, you will need to upload these files to GitHub.


- **Exercise 3 is due by the start of lecture on 27.9**.

- Don't forget to check out the [hints for this week's exercise](https://geo-python.github.io/2017/lessons/L3/exercise-3-hints.html) if you're having trouble.

- Scores on this exercise are out of **20 points**.

**Contents:**
 - [Problem 0 - Initialize Grading repository](#problem-0---initialize-grading-repository)
 - [Problem 1 - Batch processing](#problem-1---batch-processing-data-files-with-a-for-loop-4-points)
 - [Problem 2 - Classifying temperatures](#problem-2---classifying-temperatures-8-points)
 - [Problem 3 - Allocating locations](#problem-3---allocating-locations-8-points)
 - [Extra problem (optional)](#extra-problem---nested-for-loops)

## Problem 0 - Initialize Grading repository

We will gather all your results of the course to a single repository where you can easily follow
how many points you have received from the exercises.

Initilize your grading repository by accepting [this Classroom](https://classroom.github.com/a/19wUpQ4S).

## Problem 1 - Batch processing data files with a `for` loop (**4 Points**)

This problem is meant to simulate a common problem dealing with data files: batch processing.
Batch processing involves using scripts to process many data files, and one common task is generating a list of filenames that will be processed.
For this problem you will need to create a new script file `station_name_generator.py` that does the following:

1. Create a new variable `basename` that contains text `"Station"`.
2. Create a new variable `filenames` that is an empty list.
3. Iterate over the number range 0-20 and
  1. Create a variable `station` that contains the 1) text from `basename` variable, 2) the number, and 3) the file extension `.txt`
  2. Add the content of `station` to `filenames` list which should have following content in the end:

      ```
      ['Station_0.txt', 'Station_1.txt', 'Station_2.txt', 'Station_3.txt',
       'Station_4.txt', 'Station_5.txt', 'Station_6.txt', 'Station_7.txt',
       'Station_8.txt', 'Station_9.txt', 'Station_10.txt', 'Station_11.txt',
       'Station_12.txt', 'Station_13.txt', 'Station_14.txt', 'Station_15.txt',
       'Station_16.txt', 'Station_17.txt', 'Station_18.txt', 'Station_19.txt',
       'Station_20.txt']
      ```

**Your score on this problem will be based on following criteria:**

 - Creating and using variables to produce the desired text format
 - Successfully using for loop to iterate over desired set of numbers
 - Successfully producing the desired filename
 - Having your script printing all filenames as shown above
 - Including comments that explain what most lines in the code do
 - Uploading your script to your GitHub repository for this week's lesson with the name `station_name_generator.py`.

## Problem 2 - Classifying temperatures (**8 points**)

This problem is meant to introduce you to a very commonly used and useful concept of data classification.
In this problem your aim is to classify daily temperatures stored in `temperatures` list into four different classes:

  1. **Cold** ==> temperatures below -2 degrees (Celsius)
  2. **Slippery** ==> temperatures between -2 and +2 degrees (Celsius)
  3. **Comfortable** ==> temperatures between +2 and +15 degrees (Celsius)
  4. **Warm** ==> temperatures above +15 degrees (Celsius)

To solve this problem, you should modify and fill in the missing parts in the starter code [classify_temperatures.py](classify_temperatures.py).
In total, there are three tasks that you should solve according the directions in the starter-script. In addition, there is
one additional task (Task 4) that is **optional** for the students that are quicker (*does not affect grading*).

**Your score on this problem will be based on following criteria:**

 - Using for loop to iterate over the temperature values
 - Using conditional statements to find out if a value is within certain value range
 - Printing information for the user
 - Including comments that explain what most lines in the code do
 - Uploading your script to your GitHub repository for this week's lesson with the name `station_name_generator.py`.

## Problem 3 - Allocating locations (**8 points**)

Following map shows the locations of the weather stations (as blue points) in Finland that are more than 70 years old [1].
In this problem we are interested to find out whether the station network was equally distributed across Finland
seventy years ago. We have divided Finland into four geographical zones (i.e. North West, North East, South West, South East)
according the approximate center point of Finnish mainland located at `26.3, 64.5` (lon-lat in decimal degrees).

[1]: The locations and the age of weather stations were obtained from: http://en.ilmatieteenlaitos.fi/observation-stations

![](img/FMI_stations_70_years_older.png)

In [allocate_locations.py](allocate_locations.py) starter-script we have given you the coordinates of 34 weather stations.
The location of a single station is determined with a pair of latitude and longitude coordinates.
The coordinates of all the stations are separated into two lists (`lat` and `lon`) and the names of the stations are in `stations`
list. From these lists, you would get e.g. the location of the first station by combining the latitude and longitude coordinates
from coordinate lists, and the name of that station from `stations` list at index[0]:

  ```python
  # Example showing the information for the first 8 stations
  stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi',
            'Helsinki Malmi airfield', 'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho',
            'Juuka Niemelä', 'Jyväskylä airport']

  # Latitude coordinates (North - South)
  lat = [59.77, 61.2, 60.18, 60.25, 60.6, 61.88, 63.23, 62.4]

  # Longitude coordinates (West - East)
  lon = [22.95, 26.05, 24.94, 25.05, 24.8, 26.09, 29.23, 25.67]
  ```

**Overview**: In this problem your job is to print the names of weather stations located in different zones. **Optionally** you should also report the share
of weather stations that allocated to each zone that could be used to evaluate if certain zone was over/under-represented seventy years ago
(optional task).

To solve this problem, you should modify and fill in the missing parts
in the starter code [allocate_locations.py](allocate_locations.py).

**In general, the script should do following (also the criteria for grading):**

 1. Create four lists for geographical zones in Finland (i.e. NW, NW, SW, SE)
 2. Iterate over values and determine to which geographical zone the station belongs
    1. You should use a conditional statement to find out if the latitude coordinate of a station is either North or South of the center point of Finland (`26.3, 64.5`) **AND** if the longitude location is West or East from that center point.
    2. You should insert the name of the station into the correct geographical zone list (step 1)
 3. Print out the names of stations at each geographical zone
 4. **Optional:** Calculate and print the share of stations at each zone (the total number of stations equals to 100 %)

## Extra Problem (optional) - Nested `for` loops
In addition to having single `for` loops that iterate across some variable range, it is possible to *nest* `for` loops within one another.
Consider the example below:

```python
>>> for char in 'dog':
...     for char2 in 'cat':
...         print (char, char2)
    d c
    d a
    d t
    o c
    o a
    o t
    g c
    g a
    g t
```

Here, you can see that in the first pass through the first `for` loop, the value of `char` is `d`.
Entering the inner (or nested) loop, `char2` is set to `c`.
After this, the output is written to the screen and since there are more letters to loop over in the inner `for` loop, the value of `char2` will be updated upon the next pass.
The second time through the inner loop, `char2` is set to `a` while `char` remains `d`.
Like this, the inner loop will run through all of the letters in `cat` for each time that `char` is updated in the outer loop.
It doesn't take too much imagination to figure out this is a very useful concept.

For this problem you should create a new Python script `make_flag.py` that does the following:

1. Creates a variable `star` with text `"*"` and an empty string variable `text`. Recall, you can created empty string variables by assigning `""` as their value.
2. Uses nested `for` loops and the variables above to produce the text formation below when `print(text)` is run at the end of your script.

    ```
    *******
    *******
    *******
    ```
3. Creates a variable `line` with text `"-"` and an empty string variable `flag`.
4. Uses nested `for` loops and the variables above to produce the text formation below when `print(flag)` is run at the end of your script. **Note**: You will need to use conditional statements to produce the desired output.

    ```
    *******------------
    *******------------
    *******------------
    -------------------
    -------------------
    ```
