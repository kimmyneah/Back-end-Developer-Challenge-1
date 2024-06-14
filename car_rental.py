from itertools import product

# Define vehicle properties
vehicles = [
    {"type": "S", "capacity": 5, "price": 5000},
    {"type": "M", "capacity": 10, "price": 8000},
    {"type": "L", "capacity": 15, "price": 12000},
    # Add more vehicle types as needed
    # {"type": "XL", "capacity": 20, "price": 15000},
    # {"type": "XXL", "capacity": 30, "price": 20000}
]

def calculate_total_cost(combo, passengers):
    total_capacity = sum(vehicle['capacity'] * qty for vehicle, qty in combo)
    if total_capacity < passengers:
        return None, {}  # Not enough capacity
    
    total_cost = sum(vehicle['price'] * qty for vehicle, qty in combo)
    return total_cost, {vehicle['type']: qty for vehicle, qty in combo}

def find_cheapest_option(passengers):
    min_cost = None
    best_combo = {}
    
    # Determine the maximum number of each type of vehicle we might need
    max_counts = [(passengers // vehicle['capacity']) + 1 for vehicle in vehicles]
    
    # Generate all combinations of vehicle quantities
    for combo in product(*(range(count + 1) for count in max_counts)):
        combination = [(vehicles[i], combo[i]) for i in range(len(vehicles))]
        cost, counts = calculate_total_cost(combination, passengers)
        if cost is not None and (min_cost is None or cost < min_cost):
            min_cost = cost
            best_combo = counts
                
    return min_cost, best_combo

def main():
    # Get the number of passengers from the user
    try:
        passengers = int(input("Enter the number of passengers: "))
        if passengers <= 0:
            raise ValueError("The number of passengers should be a positive integer.")
        
        # Find the cheapest option
        min_cost, count = find_cheapest_option(passengers)
        
        # Filter out vehicle types with zero quantities and sort by capacity in descending order
        filtered_count = {k: v for k, v in count.items() if v > 0}
        sorted_count = sorted(
            filtered_count.items(),
            key=lambda x: next(vehicle['capacity'] for vehicle in vehicles if vehicle['type'] == x[0]),
            reverse=True
        )
        
        # Print the result
        if min_cost is not None:
            print(f"Cheapest combination for {passengers} passengers:")
            for car_size, qty in sorted_count:
                print(f"{car_size} x {qty}")
            print(f"Total cost = PHP {min_cost}")
        else:
            print(f"Cannot accommodate {passengers} passengers with available vehicles.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
