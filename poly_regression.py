import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

def polynomial_regression(points: Tuple[List[float], List[float]], title: str):
    """
    Displays a graph showing the polynomial regression with degree 5. Requires list of x and y values.
    Also prints the predicted values for 2021, 2025, and 2050.
    """
    x, y = points
    poly_fit = np.poly1d(np.polyfit(x, y, 5))

    # Plot data
    xx = np.linspace(1970, 2018, 1000)
    plt.plot(xx, poly_fit(xx), c='r', linestyle='-')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Carbon Emissions (Metric Tonnes)')
    plt.axis([1970, 2018, 0, 7000])
    plt.grid(True)
    plt.scatter(x, y)
    plt.show()

    # Predict emissions
    for year in [2020, 2021, 2025, 2050]:
        print(f"Projected emissions for {year}: {poly_fit(year)}")

    # RMSE calculation
    rmse = calculate_rmse(points, poly_fit)
    return rmse

def calculate_rmse(points: Tuple[List[float], List[float]], poly_fit: np.poly1d) -> float:
    """
    Calculates the Root Mean Squared Error (RMSE) for the polynomial regression.
    """
    x_coords, y_coords = points
    sum_of_squares = sum((y_coords[i] - poly_fit(x_coords[i])) ** 2 for i in range(len(x_coords)))
    rmse = np.sqrt(sum_of_squares / len(x_coords))
    return rmse

def iroc(year: int, data: Tuple[List[float], List[float]]) -> float:
    """
    Calculates the instantaneous rate of change (IROC) at a given year.
    """
    x, y = data
    poly_fit = np.poly1d(np.polyfit(x, y, 5))
    iroc_value = (poly_fit(year + 0.001) - poly_fit(year)) / 0.001
    return iroc_value

def aroc(year_start: int, year_end: int, x: List[float], y: List[float]) -> float:
    """
    Calculates the average rate of change (AROC) between two years.
    """
    poly_fit = np.poly1d(np.polyfit(x, y, 5))
    aroc_value = (poly_fit(year_end) - poly_fit(year_start)) / (year_end - year_start)
    return aroc_value

def rmse_polynomial_regression(points: Tuple[List[float], List[float]], x: List[float], y: List[float]) -> float:
    """
    Calculates the RMSE for polynomial regression lines.
    """
    poly_fit = np.poly1d(np.polyfit(x, y, 5))
    return calculate_rmse(points, poly_fit)

# Example usage
if __name__ == "__main__":
    x_values = [1970, 1980, 1990, 2000, 2010, 2018]
    y_values = [1000, 2000, 3000, 4000, 5000, 6000]
    points = (x_values, y_values)
    title = "Carbon Emissions Over Time"

    rmse = polynomial_regression(points, title)
    print(f"RMSE: {rmse}")

    year = 2020
    iroc_value = iroc(year, points)
    print(f"IROC at {year}: {iroc_value}")

    year_start = 1980
    year_end = 2020
    aroc_value = aroc(year_start, year_end, x_values, y_values)
    print(f"AROC from {year_start} to {year_end}: {aroc_value}")
