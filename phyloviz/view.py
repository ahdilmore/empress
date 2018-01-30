import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask
from flask import request

def plot(node_metadata, edge_metadata):
    """ Plot the tree with the given dataframe of coordinates of points

    We are now plotting with matplotlib
    Parameters
    ----------
    node_metadata : pd.DataFrame
       Contains all of the species attributes.
       Every row corresponds to a unique species
       and every column corresponds to an attribute.
       Metadata may also contain ancestors.
    edge_metadata : pd.DataFrame
       Contains all of the edge attributes.
       Every row corresponds to a unique edge
       and every column corresponds to an attribute.

    """
    # Plot nodes
    col_node_x = node_metadata['x']
    col_node_y = node_metadata['y']
    # TODO: annotation on points
    plt.scatter(col_node_x, col_node_y)

    # Plot edges
    # Get the four columns of coordinates
    col_edge_x = edge_metadata['x']
    col_edge_y = edge_metadata['y']
    col_edge_px = edge_metadata['px']
    col_edge_py = edge_metadata['py']

    row_count = len(edge_metadata.index)

    # Loop through each row and plot the edge
    for index in range(row_count):
        plot_x = [col_edge_x[index], col_edge_px[index]]
        plot_y = [col_edge_y[index], col_edge_py[index]]
        plt.plot(plot_x, plot_y)


def color_nodes(node_metadata, color_column='Disease_Type'):
    """
    Parameters
    ------------
    node_metadata : pd.DataFrame
       Contains the metadata + attributes, where the row names are the node ids
       and the column names are the attributes to be plotted
    color_column : pd.DataFrame
       The column that specifies the colors for each node
    ...
    """
    pass

# Constants for REST API
MODEL_PORT = 9001
VIEW_PORT = 9002
LOCALHOST = '127.0.0.1'

# Set up REST API for view
app = Flask(__name__)


@app.route('/nodes', methods=['POST'])
def post_nodes():
    """ Updates the node metadata of viewer object 
    by parsing the json object with index orientation.
    """
    node_json = request.get_json()
    node_metadata = pd.read_json(node_json, orient='index')


@app.route('/edges', methods=['POST'])
def post_edges():
    """ Updates the edge metadata of viewer object
    by parsing the json object with index orientation
    """
    edge_json = request.get_json()
    edge_metadata = pd.read_json(edge_json, orient='index')


# Run Flask app
if __name__ == '__main__':
    app.run(host=LOCALHOST, port=VIEW_PORT, debug=True)