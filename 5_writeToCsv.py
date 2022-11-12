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
weatherData = open('weatherData.csv', 'w')

# create the csv writer object
csvWriter = csv.writer(weatherData)

# Counter variable used for writing
count = 0

for data in dataSeries:
    if count == 0:
        # Writing headers of CSV file
        header = data.keys()
        csvWriter.writerow(header)
        count += 1

    # Writing data of CSV file
    csvWriter.writerow(data.values())

weatherData.close()