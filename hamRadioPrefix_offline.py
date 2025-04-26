"""
A python program, which allows to enter the prefix of an amateur radio call sign, and it displays the corresponding country.
It uses this csv file containing the prefixes: 'https://github.com/k0swe/dxcc-json/blob/main/dxcc-2020-02.csv'. 
The csv file has the columns "Prefix, name,	continent,	itu,	cq,	entityCode,	deleted,	outgoingQslService,	thirdPartyTraffic,	validStart,	validEnd,	notes,	countryCode,	flag,	prefixRegex", where prefixRegex is a regular expression for the possible prefixes for each country. It searches according to this regular expression, and then outputs the name, continent, itu, cq fields.
The flags show in MacOs terminals, but not quite on Linux.
With the help of ChatGPT.

For more detailed call lookup, see also: https://hamcall.net/call
It can be used without a browser and also offline.
Gerald Schuller, March 2024
Avoid identifying empty string as prefix
Make it offline capable
Gerald Schuller, April 2024
"""

import requests
import re
import csv
import os
#import sys

# URL to the CSV file
csv_url = 'https://raw.githubusercontent.com/k0swe/dxcc-json/main/dxcc-2020-02.csv'
# Local file path to store the CSV
local_csv_path = 'dxcc.csv'

def fetch_and_store_csv_data(url, local_path):
    try:
        # Attempt to fetch the CSV data
        response = requests.get(url)
        response.raise_for_status()  # Ensure we notice bad responses

        # Write the fetched data to a local file
        with open(local_path, 'wb') as f:
            f.write(response.content)

        print("CSV data downloaded and stored locally.")
    except Exception as e:
        print(f"Failed to fetch CSV data: {e}. Using local data if available.")

def load_csv_data(local_path):
    # Check if the file exists locally
    if not os.path.exists(local_path):
        print("Local CSV data not found. Please ensure you're online to download it.")
        return []

    # Load the local CSV data
    with open(local_path, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        data_lines = list(csv_reader)
        # Skip the first data row (header)
        return data_lines[1:]  # Adjust indexing based on your needs


def find_country_by_prefix(data, prefix):
    for row in data:
        # Assuming the columns are as follows: 
        # Prefix, Name, Continent, ITU, CQ, EntityCode, Deleted, OutgoingQslService, ThirdPartyTraffic, ValidStart, ValidEnd, Notes, CountryCode, Flag, PrefixRegex
        _, name, continent, itu, cq, _, _, _, _, _, _, _, _, flag, prefix_regex = row
        if prefix_regex=="":
           prefix_regex="_" #Avoid identifying empty string as prefix
        if re.search(prefix_regex, prefix, re.IGNORECASE):
            return {
                'name': name,
                'continent': continent,
                'itu': itu,
                'cq': cq,
                'flag': flag
            }
    return None

def main():
    fetch_and_store_csv_data(csv_url, local_csv_path)
    data = load_csv_data(local_csv_path)
    
    while True: #infinite loop for input, end with ctrl-C
       prefix_input = input("Enter call sign prefix: ").upper()
       result = find_country_by_prefix(data, prefix_input)
       
       if result:
           print(f"Name: {result['name']}, Continent: {result['continent']}, ITU: {result['itu']}, CQ: {result['cq']}, Flag: {result['flag']}")
           #print("Flag: ", result['flag'])
           #sys.stdout.buffer.write(result['flag'].encode('utf8'))
       else:
           print("Country not found for given prefix.")

if __name__ == "__main__":
    main()

