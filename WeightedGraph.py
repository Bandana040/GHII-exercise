import Node as n

class WeightedGraph:
    # Initialize an empty graph
    def __init__(self):
        # Create an empty dictionary for nodes
        self.nodes = {}
        # Create an empty dictionary for edges
        self.edges = {}

    # Add a node to the graph
    def add_node(self, node_id, node_data=None):
        print("Adding node", node_id)
        # Check if the node already exists
        if node_id in self.nodes:
            # Raise an exception
            raise ValueError(f"Node {node_id} already exists")
        else:
            # Create a new node object with the given data
            node = n.Node(node_id, node_data)
            # Add the node to the nodes dictionary
            self.nodes[node_id] = node

    # Add an edge to the graph
    def add_edge(self, node_id1, node_id2, weight):
        print("Adding edge", node_id1, node_id2)
        # Check if both nodes exist
        if node_id1 in self.nodes and node_id2 in self.nodes:
            # Check if the edge already exists
            if (node_id1, node_id2) in self.edges or (node_id2, node_id1) in self.edges:
                # Raise an exception
                raise ValueError(f"Edge ({node_id1}, {node_id2}) already exists")
            else:
                # Add the edge to the edges dictionary with the given weight
                self.edges[(node_id1, node_id2)] = weight
                self.edges[(node_id2, node_id1)] = weight
        else:
            # Raise an exception
            raise ValueError(f"Node {node_id1} or {node_id2} does not exist")
    
    # Define a method for finding the shortest path using Dijkstra's algorithm
    def shortest_path(self, src, dest):
        # Check if both nodes exist
        if src in self.nodes and dest in self.nodes:
            # Create a dictionary to store the distance of each node from the source
            dist = {}
            # Create a dictionary to store the previous node of each node in the path
            prev = {}
            # Create a set to store the visited nodes
            visited = set()
            # Initialize all distances as infinite
            for node in self.nodes:
                dist[node] = float("inf")
            # Initialize the source distance as zero
            dist[src] = 0
            # Loop until all nodes are visited or the destination is reached
            while len(visited) < len(self.nodes) and dest not in visited:
                # Find the node with the smallest distance from the source
                min_node = None
                min_dist = float("inf")
                for node in self.nodes:
                    if node not in visited and dist[node] < min_dist:
                        min_node = node
                        min_dist = dist[node]
                # Mark the node as visited
                visited.add(min_node)
                # Update the distances of its neighbors
                for neighbor in self.nodes:
                    if (min_node, neighbor) in self.edges:
                        new_dist = dist[min_node] + self.edges[(min_node, neighbor)]
                        if new_dist < dist[neighbor]:
                            dist[neighbor] = new_dist
                            prev[neighbor] = min_node
            # Check if the destination is reachable
            if dest in visited:
                # Create a list to store the path
                path = []
                # Trace back the path from the destination to the source
                current = dest
                while current != src:
                    path.append(current)
                    current = prev[current]
                path.append(src)
                # Reverse the path to get the correct order
                path.reverse()
                # Return the path and its length
                return path, dist[dest]
            else:
                # Return None if the destination is not reachable
                return None, None
        else:
            # Raise an exception if either node does not exist
            raise ValueError(f"Node {src} or {dest} does not exist")
