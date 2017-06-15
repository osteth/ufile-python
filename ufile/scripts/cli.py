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
def put(file):
    response = ufile.upload(file, USER, KEY)
    click.echo(response)
    return()

@click.command(help='Download a file from Uploadfiles.io')
@click.option('-s', '--slug', help='Specifies the slug of the file you wish to download.')
@click.option('-p', '--path', help='Specifies the location thats the downloaded file should be saved to.')
def get(slug, path):
    if path:
        path = path
    else:
        path = slug
    response = ufile.download(USER, KEY, slug, path)
    click.echo(response)
    return()

cli.add_command(put)
cli.add_command(get)
