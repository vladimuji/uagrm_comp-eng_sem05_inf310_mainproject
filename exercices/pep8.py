"""PEP8 style practice - INF310 for python.

Example module to show names, docstrings and a context manager
following the PEP8 conventions
"""

import time


def calculate_distance_cost(distance_km, cost_per_kn):
    """This calculate the total cost of a route based on the distance

    ARgs:
        distance_km (float): Distance in km.
        cost_per_km (float): Cost per traveled km

    Returns:
        float: Total cost of the route.
    """
    return distance_km * cost_per_kn


class Timer:
    """Context manager to calculate the execution time of the code block"""

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exec_tb):
        elapsed = time.time() - self.start_time
        print(f"Elapsed time: {elapsed:.6f} seconds")

def ask_city_name():
    """Request user for the city name

    Returns:
        str: Name entered by the user.
    """
    return input("Enter the city name: ")


if __name__ == "__main__":
    cost = calculate_distance_cost(150.5, 3.72)
    print(f"Average cost: {cost:.2f} Bs")

    with Timer():
        city = ask_city_name()
        print(f"Entered city: {city}")