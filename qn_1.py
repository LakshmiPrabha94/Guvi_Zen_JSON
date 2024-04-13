"""
Write a python code for the following
Url: https://restcountries.com/v3.1/all
1. Use OOP and  class constructor for taking input from the given url for theconcept for the upcomming task
2. Create a method that will fetach all the data from the Above mentioned url
3. Create a method that will display the  name of countries, currencies & currency symbols.
4. Create a method that will the name of countries who have Dollar as its currency
5. Create a method that will the name of countries who have Euro as its currency

"""

import requests
from requests.exceptions import RequestException

class CountryData:
    def __init__(self, url):
        # Initialize the CountryData object with the provided URL
        self.url = url
        self.response = requests.get(self.url)
        # Fetch data from the URL and store it in self.data

    def fetch_data(self):
        # Fetch data from the provided URL
        if self.response.status_code == 200:
            return self.response.json()
        else:
            print("Failed to fetch data from the URL")
            return None

    def display_country_info(self):
        # Display information for each country
        data = self.fetch_data()
        if data:
            # Iterate over each country in the data
            for country in data:
                # Get the common name of the country
                name = country.get('name', {}).get('common')
                # Get the currencies of the country
                currencies = country.get('currencies', {})
                # If both name and currencies exist
                if name and currencies:
                    # Print the country name
                    print("Country:", name)
                    # Iterate over each currency in the currencies dictionary
                    for currency, info in currencies.items():
                        # Print currency and its symbol
                        print("- Currency:", currency)
                        print("- Currency Symbol:", info.get('symbol'))
                    # Print a blank line for separation
                    print()

    def countries_by_currency(self, currency):
        # Method to retrieve countries based on a given currency
        try:
            # Ensure that data is available
            if self.fetch_data():
                # Initialize an empty list to store countries
                result = []
                # Iterate over each country data
                for data in self.fetch_data():
                    # Check if 'currencies' key exists and if the given currency is in it
                    if 'currencies' in data and currency in data['currencies']:
                        # If so, append the common name of the country to the result list
                        result.append(data['name']['common'])
                # Return the list of countries with the given currency
                return result
        except RequestException as error:
            # Handle any RequestException (e.g., network error)
            print("ERROR : Currency does not exist !", error)

# URL for fetching country data
url = "https://restcountries.com/v3.1/all"

# Create an instance of CountryData
country_data = CountryData(url)

# Display all country information
print("Displaying all country information:\n")
country_data.display_country_info()

# Get countries with Dollar as currency
print("Countries with Dollar as currency:\n", country_data.countries_by_currency('USD'))

# Get countries with Euro as currency
print("\n Countries with Euro as currency:\n",  country_data.countries_by_currency('EUR'))
