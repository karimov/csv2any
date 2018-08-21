"""csv2any - A tool that converts the data from one format to other formats."""

from csv2any.plugins._json import JSONPlugin
from csv2any.plugins._xml import XMLPlugin
from csv2any.models import Row
from operator import attrgetter

class CSVDataset(object):

    def __init__(self, path):
        self.path = path
        self.dataset = []

    def load(self, sort=None, group=None):
        import csv
        with open(self.path, encoding='utf8') as f:
            reader = csv.DictReader(f, delimiter=',')
            self.headers = reader.fieldnames
            for rec in reader:
                try:
                    print('in try block')
                    row = Row(**rec)
                except Exception as e:
                    print('exception catch: ', e)
                    continue
                print('row: ', row)
                self.dataset.append(row.to_dict())
        if sort:
            self.dataset.sort(key=lambda obj: obj[sort])
        if group:
            self.group_by_fields()

    def group_by_fields():
        from collections import defaultdict
        d = defaultdict(list)
        new = [d[k].append(v)
                for k,v in obj.items()
                for obj in self.dataset
            ]
        self.dataset = new

    def save(self, output_path, format):
        fmt = format()
        try:
            fmt.convert(output_path, self.dataset)
        except Exception as e:
            print('Something went wrong at converting!', e)


__version__ = '0.1.0'
__author__ = 'Davron Karimov <davron.sh.karimov@gmail.com>'
__all__ = ['CSVDataset', 'JSONPlugin', 'XMLPlugin']
