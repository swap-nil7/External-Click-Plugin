import click

from pkg_resources import iter_entry_points
from click_plugins import with_plugins


@with_plugins(iter_entry_points('main.plugins'))
@click.group()
def cli():
    """A complex command line interface."""
    pass

@cli.command()
def add():
    """ Adds a module """
    pass

if __name__ == '__main__':
    cli()	

