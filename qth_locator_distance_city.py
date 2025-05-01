"""
ChatGPT1o:
Given the QTH Locator or Maidenhead Grid square of a received ham radio station, 
and my own QTH Locator (e.g. JO33), can you make a Python program that returns the name of 
the nearest city with more than 100000 inhabitants of the received station, 
and the distance between my QTH locator and that of the received station in Kilometer? 
Gerald Schuller, February 2025
"""

import math

############################################################
# 1) CONVERT MAIDENHEAD (QTH) LOCATOR TO LAT/LON
############################################################

def maidenhead_to_latlon(locator: str) -> (float, float):
    """
    Convert a Maidenhead grid locator (e.g., 'JO33') to approximate latitude, longitude in degrees.
    This function handles up to 8-character locators.
    """

    # Ensure uppercase
    locator = locator.strip().upper()

    # Maidenhead basics:
    #   First two chars (Field):   lon = (ord(locator[0]) - ord('A')) * 20 - 180
    #                              lat = (ord(locator[1]) - ord('A')) * 10 - 90
    #   Next two chars (Square):   lon += int(locator[2]) * 2
    #                              lat += int(locator[3])
    #
    # Then each pair of characters refines the position further.
    # 6-char locators add sub-square, 8-char locators add extended square, etc.

    # Validate length (4–8 typical)
    if len(locator) < 2:
        raise ValueError("Locator must have at least 2 characters.")

    # Field (first two characters)
    lon_field = (ord(locator[0]) - ord('A')) * 20 - 180
    lat_field = (ord(locator[1]) - ord('A')) * 10 - 90

    # Start lat/lon
    lon = lon_field
    lat = lat_field

    # Square (the next two digits), if present
    if len(locator) >= 4:
        lon += int(locator[2]) * 2
        lat += int(locator[3])

    # Subsquare (the next two letters), if present
    if len(locator) >= 6:
        lon += (ord(locator[4]) - ord('A')) * 5.0 / 60.0
        lat += (ord(locator[5]) - ord('A')) * 2.5 / 60.0

    # Extended square (the next two digits), if present
    if len(locator) == 8:
        lon += int(locator[6]) * 5.0 / 600.0
        lat += int(locator[7]) * 2.5 / 600.0

    # Center of cell adjustment
    # Usually we add half of the smallest digit’s square dimension
    # For a 4-character locator, this is typically 1 deg in lon / 0.5 deg in lat offset, etc.
    # For simplicity, we do an approximate center offset:
    if len(locator) == 4:
        lon += 1.0  # half of 2 degrees
        lat += 0.5  # half of 1 degree
    elif len(locator) == 6:
        lon += 2.5 / 60.0  # half of 5 minutes
        lat += 1.25 / 60.0 # half of 2.5 minutes
    elif len(locator) == 8:
        lon += (2.5 / 60.0) / 10.0
        lat += (1.25 / 60.0) / 10.0

    return (lat, lon)


############################################################
# 2) DISTANCE CALCULATION (HAVERSINE)
############################################################
def haversine_km(lat1, lon1, lat2, lon2):
    # Convert lat/lon to radians
    rlat1 = math.radians(lat1)
    rlon1 = math.radians(lon1)
    rlat2 = math.radians(lat2)
    rlon2 = math.radians(lon2)

    # Haversine formula
    dlon = rlon2 - rlon1
    dlat = rlat2 - rlat1
    a = (math.sin(dlat / 2) ** 2
         + math.cos(rlat1) * math.cos(rlat2) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Earth's mean radius in km
    R = 6371
    distance = R * c
    return distance


############################################################
# 3) FIND NEAREST CITY >100K POPULATION
############################################################

# For demonstration, we’ll use just a few city records with lat, lon, population:
# (Name, Latitude, Longitude, Population)
# You should use a larger, more comprehensive dataset in practice.
large_cities_db = [
    ("Hamburg",         53.5511,   9.9937,   1841179),
    ("Berlin",          52.5200,   13.4050,  3644826),
    ("Munich",          48.1351,   11.5820,  1471508),
    ("Cologne",         50.9375,   6.9603,   1085664),
    ("Vienna",          48.2082,   16.3738,  1897491),
    ("Amsterdam",       52.3676,   4.9041,   872757),
    ("London",          51.5074,   -0.1278,  8908081),
    ("Paris",           48.8566,   2.3522,   2148327),
    # Add many more cities worldwide...
]

#Once you have large_cities.csv, you can load it in your QTH-locator Python script:
import csv

def load_large_cities(csv_file):
    """ Load the filtered CSV into a list of (city, country, lat, lon, pop). """
    cities = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            city_name = row['city']
            country_name = row['country']
            lat = float(row['lat'])
            lon = float(row['lng'])
            state= row['admin_name']
            pop = float(row['population'])
            cities.append((city_name, country_name, lat, lon, state, pop))
    return cities
    
#Subset of cities > 100000 inhabitants from:
#Cities data base: https://simplemaps.com/data/world-cities

large_cities_list = load_large_cities("large_cities.csv")


def find_nearest_large_city(lat, lon, city_db, popul=100000):
    """
    Given a latitude/longitude and a city database,
    return the nearest city with population > 100,000.
    """
    nearest_city = None
    min_distance = float('inf')

    for city_name, country_name, city_lat, city_lon, admin_name, pop in city_db:
        if pop < popul:  # skip cities under 100k
            continue
        dist = haversine_km(lat, lon, city_lat, city_lon)
        #print("dist=", dist, "city=", city_name)
        if dist < min_distance:
            min_distance = dist
            nearest_city = city_name
            country=country_name
            state=admin_name
            population = pop

    return nearest_city, country, min_distance, state, population


############################################################
# MAIN DEMO
############################################################
if __name__ == "__main__":
    print("Compute distance and print info on nearest large city given the the own QTH locator and that of a received station. End with 'q'.")
    # Your QTH locator
    #my_locator = "JO33rl"  # example
    #my_locator = "JO62pl" 
    my_locator = input("My locator (e.g. JO62pl for Berlin) = ")
    # Received station’s QTH locator
    while True: #loop until 'q' is pressed
        #received_locator = "JN88"  # example, near Vienna
        received_locator = input("Received_locator (4 characters also work) or 'q' = ")
        if received_locator=='q':
            break
        # Convert both to lat/lon
        my_lat, my_lon = maidenhead_to_latlon(my_locator)
        rx_lat, rx_lon = maidenhead_to_latlon(received_locator)

        # Calculate distance in km between the two locators
        distance = haversine_km(my_lat, my_lon, rx_lat, rx_lon)
        print(f"My locator: {my_locator} => lat={my_lat:.3f}, lon={my_lon:.3f}")
        print(f"Received locator: {received_locator} => lat={rx_lat:.3f}, lon={rx_lon:.3f}")
        print(f"Distance between locators: {distance:.1f} km")
        
        # Find nearest city of size >100k and 1M to the received locator
        for popul in {100000, 1000000}:
           #city, city_dist, population = find_nearest_large_city(rx_lat, rx_lon, large_cities_db)
           city, country, city_dist, state, population = find_nearest_large_city(rx_lat, rx_lon, large_cities_list, popul)
           #print(f"Nearest large city > {popul} inhabitants to {received_locator}: {city}, {state}, {country} (approx {city_dist:.1f} km away from center of {received_locator}), population: {population}")
           print(f"Nearest large city > {popul} inhabitants: {city}, {state}, {country} (approx {city_dist:.1f} km away from center of {received_locator}), population: {population}")
