# Skeleton of a CLI

import click

import ufile


@click.command('ufile')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(ufile.has_legs)
