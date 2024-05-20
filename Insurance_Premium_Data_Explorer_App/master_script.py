"""
========================
Master Script (Practice)
========================

--- Instructions ---
    1.  Activate your virtual environment, which should have the "shiny" library installed in it.
    2.  Execute "cd Insurance_Premium_Data_Explorer_App" to go into the "Insurance_Premium_Data_Explorer_App" directory.
    3.  Execute "python3 master_script.py -in <input_dataset>".

--- Output(s) ---
    -   <add>
"""

# region: --- Importing Modules ---

import argparse
import os

# endregion

# region: --- Parsing Arguments ---

# Create an argument parser.
parser = argparse.ArgumentParser(description='This script explores and visualizes data in a dataset, which must be in CSV format.')

# Create an argument for the input dataset.
parser.add_argument(
    '-in',
    '--in_file',
    action='store',
    dest='in_file',
    required=False,
    default='insurance_dataset.csv',
    help='Provide the name of the file containing the dataset of interest.'
    )
# The arguments i) define the short option string, ii) define the long option string, iii) specify that this argument will store the inputted value, iv) specify the name of the attribute used to store the inputted value, v) specify that this argument is not required, vi) set a default input in case the user does not provide any, and vii) provide a descriptive help message for the argument.

# Test a block of code for errors by:
try:
    # Parsing the argument inputted by the user.
    args = parser.parse_args()
# Handle errors by:
except:
    # 1) Printing the help message.
    parser.print_help()
    # 2) Terminating the program.
    sys.exit(0)

# Store the argument in a variable.
dataset = args.in_file

# endregion

# region: --- Command-Line Prompt ---

# Run multiple command-line prompts in succession.
os.system('shiny run --reload')

# TEMP: For testing.
#os.system(f'python3 histogram_outputter.py -in {dataset}')
#os.system('shiny run --reload')

# TEMP: For testing.
#os.system(f'python3 test_script.py -in {dataset}')

# endregion