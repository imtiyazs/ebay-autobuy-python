import sys, csv, os
import pandas as pd

# Global variables
filename = ""

# Check for commandline args
if len(sys.argv) < 2:
    print("Usage: python main.py <csv_file.csv>")
    sys.exit(1)

filename = sys.argv[1]
_, fileExtension = os.path.splitext(filename)

# File validation
if fileExtension != '.csv':
    print("File is not a valid CSV file")
    sys.exit(1)


def read_input_csv():
    data = {}
    # Load spreadsheet
    df = pd.read_csv(filename)
    # Drop missing values
    df.dropna(axis=0, inplace=True)
    # Check columns
    for singleColumn in df.columns:
        #Sent all column data
        data[singleColumn] = df[singleColumn].values.tolist()

    return data


# MAIN EXECUTION
print("Starting Program...")

read_input_csv()