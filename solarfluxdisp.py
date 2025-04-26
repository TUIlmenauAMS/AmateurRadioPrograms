"""
ChatGPT with WebPilot:
On the website "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-4-en.php" is a field "Observed Flux Density". Can you write a python program, which reads out its number and displays it?
See also:
https://www.darc.de/der-club/distrikte/n/ortsverbaende/20/funkausbreitung/begriffsbestimmungen/
https://heartlandhams.org/sfi-number/#:~:text=Solar%20flux%20is%20measured%20in,the%2010.7%20cm%20flux%20index).
Roughly: Values > 120: somewhat good conditions, > 150 good shortwave propagation conditions.
Does not need a web browswer.
Gerald Schuller, March 2024
"""

import requests
from bs4 import BeautifulSoup

print("Program to read and display the solar flux value from www.spaceweather.gc.ca")

# URL of the page to scrape
url = "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-4-en.php"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assuming the date and time are described in a specific section before "Observed Flux Density"
    # Find the section containing "Flux Density Values in sfu" as it includes the date and time
    content_section = soup.find(string=lambda string: string and "Flux Density Values in sfu" in string)
    
    # Extract the date and time from the content section
    if content_section:
        # The date and time are part of the content_section string, extract them
        date_time_info = content_section.split('for')[1].strip()
        date, time = date_time_info.split('at')
        date = date.strip()
        time = time.strip()
    else:
        date, time = "Date not found", "Time not found"
    
    # Extract the Observed Flux Density
    observed_flux_density = soup.find(string="Observed Flux Density").find_next().string.strip() if soup.find(string="Observed Flux Density") else "Flux Density not found"
    
    print(f"Date: {date}\nTime: {time}\nObserved Flux Density: {observed_flux_density} sfu")
else:
    print("Failed to retrieve the webpage")



