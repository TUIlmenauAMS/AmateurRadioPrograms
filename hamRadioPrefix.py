"""
Can you make an HTML page with javascript, which allows me to enter the prefix of an amateur radio call sign, and it displays the corresponding country?
Here is a csv file containing the prefixes: 'https://github.com/k0swe/dxcc-json/blob/main/dxcc-2020-02.csv'. Can you use it here?
The csv file has the columns "Prefix, name,	continent,	itu,	cq,	entityCode,	deleted,	outgoingQslService,	thirdPartyTraffic,	validStart,	validEnd,	notes,	countryCode,	flag,	prefixRegex", where prefixRegex is a regular expression for the possible prefixes for each country. Can you search according to this regular expression, and then output the name, continent, itu, cq fields?
Can you remove the first row, with "Spratly Islands", from the CSV table?
Can you make a python program doing the same?
For more detailed call lookup, see also: https://hamcall.net/call
Gerald Schuller, March 2024
Avoid identifying empty string as prefix
Gerald Schuller, April 2024
"""

import requests
import re
import csv
#import sys

# URL to the CSV file
csv_url = 'https://raw.githubusercontent.com/k0swe/dxcc-json/main/dxcc-2020-02.csv'

def fetch_csv_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    # Decode the fetched bytes into a string, split into lines, and skip the first data row
    data_lines = response.content.decode('utf-8').splitlines()[2:]
    csv_reader = csv.reader(data_lines)
    return list(csv_reader)

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
    data = fetch_csv_data(csv_url)
    
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

