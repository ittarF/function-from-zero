#!/usr/bin/env python

from mylib.logistics import distance_between_two_points, get_coordinates, cities_list, travel_time, CITIES, total_distance
import click

@click.group()
def cli():
    """
    Tool for calculating distances between a list of cities
    """

@cli.command("total")
def total():
    """
    Calculate the total distance between all the cities in the list
    """
    print(total_distance(CITIES))

if __name__ == "__main__":
    cli()
