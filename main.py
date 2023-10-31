import WeightedGraph as wg

# Create a weighted graph object
g = wg.WeightedGraph()

# Add nodes for each district with their names as data
g.add_node("Kasungu", "Kasungu")
g.add_node("Ntchisi", "Ntchisi")
g.add_node("Nkhotakota", "Nkhotakota")
g.add_node("Mchinji", "Mchinji")
g.add_node("Dowa", "Dowa")
g.add_node("Salima", "Salima")
g.add_node("Lilongwe", "Lilongwe")
g.add_node("Dedza", "Dedza")
g.add_node("Ntcheu", "Ntcheu")

# Add edges for each road with their distances as weights
g.add_edge("Kasungu", "Ntchisi", 66)
g.add_edge("Kasungu", "Mchinji", 117)
g.add_edge("Ntchisi", "Dowa", 38)
g.add_edge("Nkhotakota", "Salima", 141)
g.add_edge("Mchinji", "Lilongwe", 112)
g.add_edge("Dowa", "Lilongwe", 67)
g.add_edge("Salima", "Lilongwe", 92)
g.add_edge("Lilongwe", "Dedza", 74)
g.add_edge("Dedza", "Ntcheu", 66)

# Find the shortest path and its distance between "Kasungu" and "Ntcheu"
shortest_path, distance = g.shortest_path("Kasungu", "Ntcheu")
print("Shortest Path:", shortest_path)
print("Shortest Distance:", distance)