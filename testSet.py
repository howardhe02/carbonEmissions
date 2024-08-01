import numpy as np
from matplotlib import pyplot as plt
from typing import List, Tuple

def rmse_polynomial_regression(points: Tuple[List[float], List[float]]) -> float:
    """
    Root Mean Squared Error method used to calculate the error of regression lines.
    Basically a measure of how far the regression line data points are from the actual points.
    This is calculated by squaring the residuals (distance from linear regression and actual points),
    finding the average, and taking the square root of that value.
    """
    x_coords, y_coords = points
    poly_fit = np.poly1d(np.polyfit(x_coords, y_coords, 5))

    sum_of_squares = sum((y - poly_fit(x)) ** 2 for x, y in zip(x_coords, y_coords))
    return np.sqrt(sum_of_squares / len(x_coords))

def polynomial_regression(X: List[float], Y: List[float], points: Tuple[List[float], List[float]]) -> float:
    """
    Displays a graph showing the polynomial regression with degree 5. Requires lists of x and y values.
    Also prints the predicted values for 2021, 2025, and 2050.
    """
    poly_fit = np.poly1d(np.polyfit(X, Y, 5))

    # Plot data
    xx = np.linspace(1970, 2018, 1000)
    plt.plot(xx, poly_fit(xx), c='r', linestyle='-')
    plt.title('Polynomial Regression')
    plt.xlabel('Year')
    plt.ylabel('Carbon Emissions (Metric Tonnes)')
    plt.axis([1970, 2018, 0, 7000])
    plt.grid(True)
    plt.scatter(X, Y)
    plt.show()

    # Predict emissions
    for year in [2020, 2021, 2025, 2050]:
        print(f"Projected emissions for {year}: {poly_fit(year)}")

    # Calculate RMSE
    return rmse_polynomial_regression(points)

# Example usage
if __name__ == "__main__":
    X = [1970, 1980, 1990, 2000, 2010, 2018]
    Y = [1000, 2000, 3000, 4000, 5000, 6000]
    points = (X, Y)

    rmse = polynomial_regression(X, Y, points)
    print(f"RMSE: {rmse}")
