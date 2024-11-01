from mylib.logistics import (
    distance_between_two_points,
    get_coordinates,
    cities_list,
    travel_time,
    CITIES,
    total_distance,
)


def test_distance_between_two_points():

    assert distance_between_two_points(CITIES[0][1], CITIES[1][1]) == 477.02546129052047


def test_cities_list():
    assert "Milan" in cities_list()
