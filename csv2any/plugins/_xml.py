
from csv2any.base import PluginBase
from xml.etree.ElementTree import Element, tostring

class XMLPlugin(PluginBase):

    def convert(self, fp, dataset, tag='row'):
        rows = Element('rows')
        row = Element(tag)
        for rec in dataset:
            for keu, value in rec.items():
                child = Element(key)
                child.text = value
                row.append(child)

        rows.append(row)
        with open(fp, 'w') as f:
            f.write(tostring(rows))
