# Skeleton of a CLI

import click
import ufile

USER = ''
KEY = ''
        
@click.group()
def cli():
    """This is a command line utility to aid in handling file transfers to and from Uploadfiles.io.
    Additional information is avilable at https://github.com/osteth/ufile-tools/"""
    pass

@click.command(help='upload a file to Uploadfiles.io')
@click.option('-f', '--file', help='Specifies the File that should be uploaded.')
def up(file):
    response = ufile.upload(file, USER, KEY)
    click.echo(response)
    return()

@click.command(help='Download a file from Uploadfiles.io')
@click.option('-s', '--slug', help='Specifies the slug of the file you wish to download.')
def down(slug):
    ufile.download(USER, KEY, slug)
    return()

cli.add_command(up)
cli.add_command(down)
