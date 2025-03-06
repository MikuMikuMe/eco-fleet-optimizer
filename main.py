Certainly! Optimizing delivery routes to reduce carbon emissions is an exciting project. Below is a Python program for a simple Eco-Fleet Optimizer. This program uses the Traveling Salesman Problem (TSP) as a basis to optimize routes. We'll use a simulated algorithm to find a near-optimal route.

Please note, that for a fully functional and optimized production-ready application, integration with real-world data, a more robust algorithm, and additional features for handling dynamic logistics data would be required.

```python
from itertools import permutations
import sys

def calculate_route_distance(route, distance_matrix):
    """Calculate the total distance of a given route."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to the starting point
    return total_distance

def tsp_brute_force(distance_matrix):
    """Solve the Traveling Salesman Problem using a brute-force approach."""
    number_of_locations = len(distance_matrix)
    all_locations = range(number_of_locations)
    
    # Generate all possible routes
    all_possible_routes = permutations(all_locations)
    min_distance = sys.maxsize
    best_route = None

    for route in all_possible_routes:
        current_distance = calculate_route_distance(route, distance_matrix)
        
        # Select the route with the less total distance
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance

def print_route(route, locations):
    """Prints the route in a readable format."""
    route_list = [locations[i] for i in route]
    return ' -> '.join(route_list) + ' -> ' + route_list[0]

def main():
    # Define a list of locations
    locations = ['Warehouse', 'Point A', 'Point B', 'Point C', 'Point D']

    # Distance matrix (symmetric) between the locations
    # The diagonal represents the distance from a location to itself (0)
    distance_matrix = [
        [0, 10, 15, 20, 25],
        [10, 0, 35, 25, 30],
        [15, 35, 0, 30, 20],
        [20, 25, 30, 0, 15],
        [25, 30, 20, 15, 0]
    ]

    try:
        # Find the optimal route
        best_route, min_distance = tsp_brute_force(distance_matrix)
        # Print results
        print("Optimal Route: ", print_route(best_route, locations))
        print("Minimum Distance: ", min_distance)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Key Points & Assumptions:
- **Brute Force Approach**: The program uses a brute-force method to solve the TSP, which is computationally expensive and not suitable for a large number of locations. For a real-world scenario, using more efficient algorithms like Genetic Algorithms or A* might be better.
- **Symmetric Distance Matrix**: This implementation assumes a symmetric distance matrix and the problem is static (same delivery locations every time you run the application).
- **Error Handling**: Basic error handling is present to catch possible exceptions that might happen during execution, ensuring the user is informed of any issues.

Enhancements for real-world applications may include:
- Integrating with mapping APIs for dynamic distances and traffic conditions.
- Incorporating vehicle types for accurate fuel consumption modeling.
- Adding a UI for interfacing with logistics companies' systems.
- Using routing libraries like Google OR-Tools for more scalable solutions.