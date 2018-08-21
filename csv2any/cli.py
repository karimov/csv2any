
from csv2any import CSVDataset, JSONPlugin, XMLPlugin
import click

formats = {
    'json': JSONPlugin,
    'xml': XMLPlugin
    }

@click.command()
@click.option('--src', '-s', default='data/hotel.csv', help='path to csv file.')
@click.option('--format', '-f', type=click.Choise(formats.keys()))
@click.option('--dest', '-d', default='data/')
@click.option('--sort', default='stars', help="To sort the data before writing it")
@click.option('--group', default=False)
def main(src, dest, format, sort, group):
    """The purpose of this tool is to convert the data from one format to other formats.
    ."""
    dataset = CSVDataset(src)
    dataset.save(dest, format=format, sort=sort, group=group)

if __name__ == '__main__':
    main()
