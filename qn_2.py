"""
Write a python code for the following
https://www.openbrewerydb.org/
. Use OOP and  class constructor for taking input from the given URL for the concept for the upcoming task
2. Create a method that will fetch all the data from the above-mentioned URL
3. Create a method that will list all the breweries present in the states of Alaska, Maine, and New York
4. Create a method that will give the count of  breweries in each of the states of Alaska, Maine, and New York
5. Create a method that count the number of types of breweries present in individual cities of the states of  Alaska, Maine, and New York
6. Create a method that count and list how many breweries have websites in the states of Alaska, Maine, and New York
"""


import requests

class BreweryData:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from the URL")
            return None

    def get_breweries(self, states):
        data = self.fetch_data()
        if data:
            breweries = []
            for brewery in data:
                if brewery['state'] in states:
                    breweries.append(brewery)
            return breweries

    def count_breweries_by_state(self, states):
        data = self.fetch_data()
        if data:
            state_counts = {state: 0 for state in states}
            for brewery in data:
                if brewery['state'] in states:
                    state_counts[brewery['state']] += 1
            return state_counts

    def count_brewery_types_by_city(self, states):
        data = self.fetch_data()
        if data:
            city_counts = {}
            for brewery in data:
                if brewery['state'] in states:
                    city = brewery['city']
                    brewery_type = brewery['brewery_type']
                    if city in city_counts:
                        if brewery_type in city_counts[city]:
                            city_counts[city][brewery_type] += 1
                        else:
                            city_counts[city][brewery_type] = 1
                    else:
                        city_counts[city] = {brewery_type: 1}
            return city_counts

    def count_websites_by_state(self, states):
        data = self.fetch_data()
        if data:
            website_counts = {state: 0 for state in states}
            for brewery in data:
                if brewery['state'] in states and 'website_url' in brewery and brewery['website_url']:
                    website_counts[brewery['state']] += 1
            return website_counts

# URL for fetching brewery data
url = "https://api.openbrewerydb.org/breweries"

# Create an instance of BreweryData
brewery_data = BreweryData(url)

# List of states for Data Retrival
states = ['Alaska', 'Maine', 'New York']

# Fetch all breweries in the specified states
breweries = brewery_data.get_breweries(states)
print("Breweries in Alaska, Maine, and New York:", breweries)

# Count the number of breweries in each state
brewery_counts_by_state = brewery_data.count_breweries_by_state(states)
print("\nNumber of breweries in each state:", brewery_counts_by_state)

# Count the number of brewery types in each city
brewery_types_by_city = brewery_data.count_brewery_types_by_city(states)
print("\nNumber of brewery types in each city:", brewery_types_by_city)

# Count and list breweries with websites in each state
website_counts_by_state = brewery_data.count_websites_by_state(states)
print("\nNumber of breweries with websites in each state:", website_counts_by_state)
