import plotly.graph_objects as go
import extraction
from typing import List


def call_3d_graph(x: List[int], y: List[float]) -> None:
    """
    Creates a 3D graph showing the relationship between years, carbon emissions, and GDP per capita.
    """
    z = extraction.get_gdp('datasets/Canada_GDP.csv')

    # Create the 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

    # Update layout with titles and axis labels
    fig.update_layout(
        title='Canada GDP per Capita vs CO2 Emissions',
        scene=dict(
            xaxis_title='Years',
            yaxis_title='Carbon Emission (Metric Tonnes)',
            zaxis_title='GDP per Capita'
        )
    )

    # Display the figure in a web browser
    fig.show()


# Example usage
if __name__ == "__main__":
    x = [2000, 2001, 2002, 2003, 2004]  # Example years
    y = [10, 15, 20, 25, 30]  # Example carbon emissions

    call_3d_graph(x, y)
