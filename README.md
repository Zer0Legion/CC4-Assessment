# CC4-Assessment

## Overview
Take-home assignment for Data Engineer Intern.
I have completed the following subtasks of **Task 1**:
1. Extract the following fields and store the data as restaurants.csv.
2. Extract the list of restaurants that have past event in the month of April 2019 and store the data as restaurant_events.csv.
3. From the dataset (restaurant_data.json), determine the threshold for the different rating text based on aggregate rating.

## Setup
1. Clone this repository to your desktop.
2. Navigate to the main folder of the source code using your CLI. On Unix terminals (Git Bash), 'ls' will return the following:

'''
README.md
cc4_io.py
in/
main.py
restaurants.py
'''
3. In the CLI, type the following to install the required python packages:
   'pip install -r requirements.txt'
4. To run the program, type the following command
  'python main.py' or
  'python main.py [minimum_rating]',
  which will generate a separate filtered list of restaurants that fit Steven's needs of having good enough user ratings.
5. The output CSV files will be located in the out directory.

## Assumptions
1. The restaurant_data.json may be populated with different data, but its structure will not change.
2. Subtask 3: As the current dataset has a lowest rating of 2.2, but lower rated restaurants will likely to have a "Poor" rating, the threshold for "Poor" being the lowest rated category is set to 0.0.
3. Subtask 3: As the output method is not specified, the output is both printed to stdout and stored in a csv file for reference.

## Decisions
1. For CSV related subtasks, commas in strings (like cuisine types) are replaced with ; to prevent interference with CSV's commas, and its similarity in meaning to a comma.
2. Constants / Environment variables like output file names are stored in main.py file. As they are task requirements they are not changed, but functionality is added to accomodate changing of these path/file variables.
3. Docstrings are used to document the code.
4. Python's built-in json package was used to parse information from the json files.
5. pandas Dataframe was used to parse information from the Excel Sheet.
