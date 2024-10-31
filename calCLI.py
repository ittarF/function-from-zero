#!/usr/bin/env python3

# chmod +x calCLI.py

from mylib.calc import add, sub, mul, div, power
import click


@click.group()
def cli():
    """
    A calculator CLI
    """


@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_cmd(a, b):
    """
    Add two numbers together

    Example:
    ./calCLI.py add 1 2
    """

    # use colored output to print the result
    click.secho(f"{a} + {b} = {add(a, b)}", fg="green")


@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_cmd(a, b):
    """
    Subtract two numbers

    Example:
    ./calCLI.py sub 1 2
    """

    # use colored output to print the result
    click.secho(f"{a} - {b} = {sub(a, b)}", fg="green")


@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_cmd(a, b):
    """
    Multiply two numbers

    Example:
    ./calCLI.py mul 1 2
    """

    # use colored output to print the result
    click.secho(f"{a} * {b} = {mul(a, b)}", fg="green")


@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_cmd(a, b):
    """
    Divide two numbers

    Example:
    ./calCLI.py div 1 2
    """

    # use colored output to print the result
    click.secho(f"{a} / {b} = {div(a, b)}", fg="green")


@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def pow_cmd(a, b):
    """
    Raise a to the power of b

    Example:
    ./calCLI.py power 2 3
    """

    # use colored output to print the result
    click.secho(f"{a} ** {b} = {power(a, b)}", fg="green")


if __name__ == "__main__":
    cli()
