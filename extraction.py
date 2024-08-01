"""
Extraction File
"""

import csv
from typing import List, Tuple, Dict

def get_data(filename: str) -> Dict[str, List[Tuple[int, float]]]:
    """
    Return a dictionary mapping a country to a list of tuples. Each tuple contains a year and carbon emission amount.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # Get headers for dates
        headers = next(reader)
        data = next(reader)
        country = data[3]

        # Format data and return it
        country_data = {
            country: [(int(headers[pos]), float(data[pos])) for pos in range(4, len(headers))]
        }
    return country_data

def get_gdp(filename: str) -> List[float]:
    """
    Return a list of a country's GDP from 1970 to 2018.
    """
    gdp_data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # Skip header
        next(reader)

        for row in reader:
            try:
                year = int(row[0])
                if 1970 <= year <= 2018:
                    gdp_data.append(float(row[1]))
            except ValueError:
                # Skip rows with invalid data
                continue

    # Reverse the list so the last item is the first item
    gdp_data.reverse()

    return gdp_data

if __name__ == "__main__":
    # Example usage
    data_filename = "datasets/CanadaCO2_emissions.csv"
    gdp_filename = "datasets/Canada_GDP.csv"

    data = get_data(data_filename)
    print(data)

    gdp_data = get_gdp(gdp_filename)
    print(gdp_data)
