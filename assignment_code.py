# assignment_code.py
# Basic skills for data management assignment code

def calculate_average(data):
    """Calculates the arithmetic mean (average) of a list of numbers."""
    # Check if the list is empty to avoid division by zero
    if not data:
        return 0
    return sum(data) / len(data)

def calculate_median(data):
    """Calculates the median (middle value) of a list of numbers."""
    n = len(data)
    if n == 0:
        return 0

    # The median calculation requires the data to be sorted
    sorted_data = sorted(data)
    
    # Check if the number of elements is odd or even
    if n % 2 == 1:
        # Odd number of elements: return the middle element
        # Integer division n // 2 gives the index of the middle element
        return sorted_data[n // 2]
    else:
        # Even number of elements: return the average of the two middle elements
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

# --- Example Usage ---

data_points = [10, 20, 30, 40, 50, 60]  # Even number of elements
# data_points = [10, 20, 30, 40, 50]  # Example of an odd number of elements

avg = calculate_average(data_points)
median = calculate_median(data_points)

print(f"--- Data Management Assignment Calculations ---")
print(f"The input data points are: {data_points}")
print(f"The calculated average (mean) is: {avg}")
print(f"The calculated median is: {median}")

# --- Output should be:
# The calculated average (mean) is: 35.0
# The calculated median is: 35.0 (average of 30 and 40)

# ... (Your existing code) ...

# --- Added for branching demonstration ---
print("\n--- Branch successfully created and merged! ---")