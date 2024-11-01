#!/usr/bin/env python

from mylib.logistics import distance_between_two_points, cities_list, get_coordinates
import click


@click.group()
def cli():
    """
    Logistics command-line
    """


@cli.command("cities")
def cities():
    """
    List cities

    Example: ./logisticsCLI.py cities
    """

    click.echo(click.style("List of cities", fg="green"))
    for city in cities_list():
        click.echo(click.style(city, fg="blue"))

@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """
    Calculate the distance between two cities

    Example: ./logisticsCLI.py distance "Milan" "Palermo"
    """

    click.echo(click.style("Distance between two cities", fg="green"))
    click.echo(
        click.style(
            f"The distance between {city1} and {city2} is {distance_between_two_points(get_coordinates(city1), get_coordinates(city2)):.3f} km",
            fg="blue",
        )
    )

if __name__ == "__main__":
    cli()