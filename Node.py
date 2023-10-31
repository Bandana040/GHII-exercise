# Define a class for node object
class Node:
    # Initialize a node with an identifier and optional data
    def __init__(self, node_id, node_data=None):
        # Store the identifier as an attribute
        self.id = node_id
        # Store the data as an attribute
        self.data = node_data

    # Define a string representation of the node
    def __str__(self):
        return f"Node({self.id}, {self.data})"
