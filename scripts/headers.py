from io import BytesIO

import pandas as pd
import requests


# Function to fetch CPS data from FTP server and inspect it
def inspect_cps_data():
    url = 'https://www2.census.gov/programs-surveys/cps/datasets/2024/basic/jul24pub.csv'
    response = requests.get(url)
    try:
        data = pd.read_csv(BytesIO(response.content), encoding='latin1')
        columns = data.columns
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV file: {e}")
        return None
    return columns, data.head(10)

# Inspect the data structure
columns, preview_data = inspect_cps_data()
print("Columns in the CPS data:")
print(columns)
print("Preview of the first few lines of the CPS data:")
print(preview_data)
