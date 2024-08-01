import plotly.graph_objects as go
import random
from typing import List, Tuple

def run_example(points: Tuple[List[float], List[float]], title: str) -> Tuple[float, float]:
    """Creates a linear regression model and plots it"""
    x_coordinates, y_coordinates = points

    # Run simple linear regression to find the slope and intercept (a and b) for y = a + bx
    a, b = simple_linear_regression(points)

    # Plot the data and the regression line
    plot_points_and_regression(x_coordinates, y_coordinates, a, b, min(x_coordinates), max(x_coordinates), title)

    return a, b

def simple_linear_regression(points: Tuple[List[float], List[float]]) -> Tuple[float, float]:
    """Return the slope and intercept of the linear regression line"""
    x_coords, y_coords = points
    mean_x = sum(x_coords) / len(x_coords)
    mean_y = sum(y_coords) / len(y_coords)

    sum1 = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_coords, y_coords))
    sum2 = sum((x - mean_x) ** 2 for x in x_coords)

    b = sum1 / sum2
    a = mean_y - (b * mean_x)
    return a, b

def evaluate_line(a: float, b: float, error: float, x: float) -> float:
    """Evaluate the linear function y = a + bx for the given a, b, and x values with the given error term."""
    if error == 0:
        return a + b * x
    else:
        return a + b * x + random.uniform(-error, error)

def plot_points_and_regression(x_coords: List[float], y_coords: List[float],
                               a: float, b: float, x_min: float, x_max: float, title: str) -> None:
    """Plot the given x- and y-coordinates and the linear regression model using Plotly."""
    fig = go.Figure()

    # Create head title, x-axis title, and y-axis title
    fig.update_layout(title=f'Country: {title} Carbon Emissions', xaxis_title='Year',
                      yaxis_title='Carbon Emission (Metric Tonnes)')

    # Add the raw data
    fig.add_trace(go.Scatter(x=x_coords, y=y_coords, mode='markers', name='Data'))

    # Add the regression line
    fig.add_trace(go.Scatter(x=[x_min, x_max], y=[evaluate_line(a, b, 0, x_min), evaluate_line(a, b, 0, x_max)],
                             mode='lines', name='Regression line'))

    # Display the figure in a web browser
    fig.show()

def rmse_linear_regression(points: Tuple[List[float], List[float]]) -> float:
    """Calculate the Root Mean Squared Error (RMSE) of the linear regression model"""
    x_coordinates, y_coordinates = points
    a, b = simple_linear_regression(points)

    sum_of_squares = sum((y - (a + b * x)) ** 2 for x, y in zip(x_coordinates, y_coordinates))
    return (sum_of_squares / len(x_coordinates)) ** 0.5

def conversion(data: Tuple[List[float], List[float]]) -> None:
    """Convert values from pounds to kilograms by multiplying by 1.01605"""
    data[1] = [value * 1.01605 for value in data[1]]

# Example usage
if __name__ == "__main__":
    example_points = ([2000, 2001, 2002, 2003, 2004], [10, 15, 20, 25, 30])
    run_example(example_points, "Example Country")
