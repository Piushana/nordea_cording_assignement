# writing Helsinki weather data to csv

# importing the  modules
import requests
import csv

# input parameters for the API
parameters = {
    "lat": "60.19",
    "lon": "24.94",
    "product": "civil",
    "output": "json"
}

response = requests.get("http://www.7timer.info/bin/api.pl", params=parameters)

dataSeries = response.json()['dataseries']
weather_data = open('weather_data.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(weather_data)

# Counter variable used for writing
count = 0

for data in dataSeries:
    if count == 0:
        # Writing headers of CSV file
        header = data.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(data.values())

weather_data.close()