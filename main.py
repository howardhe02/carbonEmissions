"""
Main File
"""
import extraction
import pprint
from typing import Dict, Tuple, List
import linear_regression
import poly_regression
import threeD_graph

def get_all(filenames: List[str]) -> List[Dict[str, List[Tuple[int, float]]]]:
    """
    Return a list of dicts mapping country name to a list of tuples containing year and emissions.
    """
    storage = []
    for data in filenames:
        storage.append(extraction.get_data('datasets/' + data))
    return storage

def convert_all(data: List[Dict[str, List[Tuple[int, float]]]]) -> Dict[str, Tuple[List[int], List[float]]]:
    """
    Return a dict mapping country names to a tuple of a list of years and list of emissions.

    This function is used to format data so that it can be plotted on a graph. The years represent the x-axis and the
    emissions represent the y-axis.
    """
    stored_data = {}
    for dict_set in data:
        country = list(dict_set.keys())[0]
        stored_data[country] = (
            [year[0] for year in dict_set[country]],
            [emission[1] for emission in dict_set[country]]
        )
    return stored_data

def run_project() -> None:
    """
    Main function that runs the entire project.
    """
    all_files = [
        'CanadaCO2_emissions.csv',
        'ChinaCO2_emissions.csv',
        'JapanCO2_emissions.csv',
        'MexicoCO2_emissions.csv',
        'United_KingdomCO2_emissions.csv',
        'United_States_of_AmericaCO2_emissions_2.csv',
        'NigerCO2_emissions.csv'
    ]

    all_data = get_all(all_files)
    all_point_data = convert_all(all_data)

    pprint.pprint(all_point_data)

    # Plot linear regression graphs for every country
    for country, data in all_point_data.items():
        # Remove NA points (if needed)
        # linear_regression.remove_na(data)
        print(data)
        linear_regression.run_example(data, country)
        # Polynomial regression (can cause lag and overlaps)
        # poly_regression.polynomial_regression(data, country)

    # Call 3D graph for Canada
    threeD_graph.call_3d_graph(all_point_data['Canada'][0], all_point_data['Canada'][1])

def compare_canada() -> None:
    """
    Compares Canada to other countries.
    """
    pass  # Implement comparison logic here if needed

if __name__ == "__main__":
    run_project()
