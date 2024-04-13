# Python Scripts for Data Retrieval 

## Introduction
This repository contains two Python scripts (`country_data.py` and `brewery_data.py`) that utilize Object-Oriented Programming (OOP) concepts to fetch and analyze data from external APIs. These scripts offer functionalities to retrieve information about countries, currencies, and breweries across different states.

### APIs Used
1. **Rest Countries API**: Provides comprehensive data about countries, including their currencies.
2. **Open Brewery DB API**: Offers a database of breweries with detailed information, such as location and type.

## Instructions for Running the Scripts
To run the scripts locally, follow these instructions:

1. **Clone the Repository**: Clone this repository to your local machine using Git.
2. **Install Dependencies**: Navigate to the repository directory and install the required Python packages using the command `pip install -r requirements.txt`.
3. **Execute the Scripts**: Run the Python scripts using Python 3.x. Use the following commands:
   - For `country_data.py`: `python country_data.py`
   - For `brewery_data.py`: `python brewery_data.py`

## Description of Each Script

### `country_data.py`
This script interacts with the external API to retrieve and display information about countries and their currencies. It offers the following functionalities:
- **Display Country Information**: Lists the names of countries along with their currencies and currency symbols.
- **Filter by Currency**: Identifies and lists countries using a specific currency, such as Dollar or Euro.

### `brewery_data.py`
The `brewery_data.py` script interacts with the external API to fetch brewery data. It provides the following features:
- **List Breweries by State**: Retrieves and lists breweries located in specific states, such as Alaska, Maine, and New York.
- **Count Breweries by State**: Calculates and displays the number of breweries present in each state.
- **Analyze Brewery Types by City**: Counts the types of breweries (e.g., Microbrewery, Brewpub) in individual cities within specified states.
- **Identify Breweries with Websites**: Counts and lists breweries that have websites in selected states.

## Requirements: 
Python 3.x

## Usage

1. To run the test script:
   ```
    python <script_name>.py
    ```
   Replace <script_name> with the name of the Python script you want to run.

```

