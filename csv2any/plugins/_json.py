
from csv2any.base import PluginBase
import json

class JSONPlugin(PluginBase):

    def convert(self, fp, obj):
        with open(fp, 'w') as f:
            json.dump(obj, fp=f)
