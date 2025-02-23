
import heapq

def shortest_path_to_birjand(n, adjacency_matrix):
    """
    Computes the shortest distances from each city to the city of Birjand using Dijkstra's algorithm.

    Args:
        n (int): Number of cities (nodes in the graph).
        adjacency_matrix (list[list[int]]): The adjacency matrix representing the graph.
            adjacency_matrix[i][j] is the distance from city i to city j (0 means no connection).
   
    Returns:
        list[int]: A list where the i-th element represents the shortest distance from city i to Birjand.
    """
    # Initialize distances to infinity and set the distance to Birjand (last city) to 0
    inf = float('inf')
    distances = [inf] * n
    distances[-1] = 0  # Distance from Birjand to itself is 0

    # Min-heap for priority queue, starting from Birjand (node n - 1)
    priority_queue = [(0, n - 1)]  # (distance, city_index)

    # Perform Dijkstra's algorithm
    while priority_queue:
        # Extract the city with the smallest distance
        current_distance, current_city = heapq.heappop(priority_queue)

        # Skip processing if we've already found a shorter path
        if current_distance > distances[current_city]:
            continue

        # Check all neighboring cities
        for neighbor_city in range(n):
            weight = adjacency_matrix[current_city][neighbor_city]
            if weight > 0:  # Ensure there is a connection
                new_distance = current_distance + weight
                # If a shorter path to the neighbor is found
                if new_distance < distances[neighbor_city]:
                    distances[neighbor_city] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor_city))

    return distances

# Read input data
n = int(input())  # Number of cities
adjacency_matrix = []

for _ in range(n):
    adjacency_matrix.append(list(map(int, input().split())))

# Compute shortest distances to Birjand
shortest_distances = shortest_path_to_birjand(n, adjacency_matrix)

# Print the results
for distance in shortest_distances:
    print(distance)