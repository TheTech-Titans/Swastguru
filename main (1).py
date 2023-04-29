import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Initialize geolocator object
geolocator = Nominatim(user_agent="my-app")

# Read the hospital data from Excel sheet
hospital_data = pd.read_excel("hospital_details.xlsx")

# Get the user's location input
user_location = input("Enter your location: ")

# Convert the user's location to coordinates
user_location_result = geolocator.geocode(user_location)
if user_location_result is not None:
    user_coordinates = user_location_result[1]
else:
    print("Please enter a valid location:")
    exit()

# Add a new column to the hospital data dataframe to store the distance between the hospital and the user's location
# lambda function calculates distance 
# Add a new column to the hospital data dataframe to store the distance between the hospital and the user's location
# lambda function calculates distance
def calculate_distance(x):
    location = geolocator.geocode(x)
    if location is not None:
        return geodesic(user_coordinates, location[1]).km
    else:
        return None

hospital_data["distance"] = hospital_data["ADDRESS"].apply(calculate_distance)

requested_item = input("What do you want to check the availability of? ")

# Filter the hospitals based on the user's requested item and distance
available_hospitals = hospital_data[(hospital_data[requested_item] > 0) & (hospital_data["distance"] <= 15)]

# Print the hospital name and availability for the requested item
if len(available_hospitals) == 0:
    print("Sorry, no hospitals found with availability of", requested_item, "within 15 km of", user_location)
else:
    print("Hospitals with availability of", requested_item, "within 15 km of", user_location, ":\n")
    for index, row in available_hospitals.iterrows():
        print(row["NAME"],"hospital type (PRIVATE/GOVERNMENT):", row["TYPE"],row['ADDRESS'],"ITEM REQUESTED :" , requested_item, ":", row[requested_item])
