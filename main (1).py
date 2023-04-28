
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Initialize geolocator object
geolocator = Nominatim(user_agent="my-app")

import google.colab
# pandas used to analyse data
# files - inbuilt google function to access files
from google.colab import files

# Upload the Excel file
uploaded = files.upload()

# Read the Excel file into a pandas dataframe
df = pa.read_excel('hospital_details.xlsx',index_col=None)
# enter name of excel file

# Read the hospital data from Excel sheet
hospital_data = pd.read_excel("hospital_details.xlsx")

# Get the user's location input
user_location = input("Enter your location: ")

# Convert the user's location to coordinates
user_location_result = geolocator.geocode(user_location)
if user_location_result is not None:
    user_coordinates = user_location_result[1]
else:
    print("Please enter a  valid location:")
    exit()

# Loop through each hospital in the data
for index, row in hospital_data.iterrows():
    # Get the hospital address and convert it to coordinates
    hospital_address = row["ADDRESS"]
    hospital_location_result = geolocator.geocode(hospital_address)
    if hospital_location_result is not None:
        hospital_coordinates = hospital_location_result[1]
    else:
        print("Unable to show hospital address:")
        continue
    
    # Calculate the distance between the hospital and the user's location
    distance = geodesic(user_coordinates, hospital_coordinates).km
    
    requested_item = input("What do you want to check the availability of? ")
    #get them to input specific words

    # Step 6: Filter the hospitals based on the user's requested item and distance
    available_hospitals = hospital_data[(hospital_data[requested_item] > 0) & (hospital_data["distance"] <= 15)]
    #available hospitals is a list which stores all the hospitals whih have the requested item and are within radius input by the user
     

    # Step 7: Print the hospital name and availability for the requested item
    if len(available_hospitals) == 0:
        print("Sorry, no hospitals found with availability of", requested_item, "within 15 km of", user_location)
    else:
        print("Hospitals with availability of", requested_item, "within 15 km of", user_location, ":\n")
        for index, row in available_hospitals.iterrows():
            print(row["Hospital Name"], "-", requested_item, ":", row[requested_item])

run = True
print('Enter 1 to find intensive care near you: ')
print('Enter 2 to find intensive care for newborns near you: ')
print('Enter 3 to find intensive care for children near you: ')
print('Enter 4 to find intensive care for pregnancy related issues near you: ')
print('Enter 5 to find vaccines available near you: ')
print('Enter 6 to find ventilators available near you: ')
while run:
    bot=input('what can i help you with?: ')
    
    if bot=='1':
        print('ICUs near here: ')
        break
    elif bot== '2':
        print('NICUs near here: ')
        break
    elif bot== '3':
         print('PICUs near here: ')
         break
    elif bot =='4':
         print('MICUs near here: ')
         break
    elif bot == '5':
        print('Vaccines are available here: ')
        break
    elif bot == '6':
        print('ventilators are available here: ')
        break
    else:
        run = False