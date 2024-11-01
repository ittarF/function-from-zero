"""
This module deals with logistics and calculates distances between two points
and the time it takes to travel between two points and other logistics related questions
for a given speed"""

from geopy import distance

# build a list of 10 cities in Italy
CITIES = [
    ("Rome", (41.9028, 12.4964)),
    ("Milan", (45.4642, 9.1900)),
    ("Naples", (40.8518, 14.2681)),
    ("Turin", (45.0703, 7.6869)),
    ("Palermo", (38.1157, 13.3615)),
    ("Genoa", (44.4072, 8.9341)),
    ("Bologna", (44.4949, 11.3426)),
    ("Florence", (43.7696, 11.2558)),
    ("Bari", (41.1177, 16.8512)),
    ("Catania", (37.5079, 15.0830)),
]


def distance_between_two_points(point1, point2):
    """
    Calculate the distance between two points
    """
    return distance.distance(point1, point2).km


# return the coordinates of a city
def get_coordinates(city):
    """
    Return the coordinates of a city
    """
    for city_name, coordinates in CITIES:
        if city_name == city:
            return coordinates


def cities_list():
    """
    Return the list of cities
    """
    return [city[0] for city in CITIES]


# estimate the travel time between two cities by car.
# assume the speed is 60 miles per hour
def travel_time(city1, city2, speed=90):
    """
    Estimate the travel time between two cities by car.
    Assume the default speed is 90 km per hour
    """

    point1 = get_coordinates(city1)
    point2 = get_coordinates(city2)
    total_distance = distance_between_two_points(point1, point2)
    hours = round(total_distance / speed)
    return hours


def total_distance(city_list):
    """
    Calculate the total distance between a list of cities
    """
    total_distance = 0
    for i in range(len(city_list) - 1):
        total_distance += distance_between_two_points(
            city_list[i][1], city_list[i + 1][1]
        )
    print(f"Total distance: {total_distance} km")
    return total_distance
