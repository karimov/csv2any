
from abc import ABCMeta, abstractmethod

class PluginBase(metaclass=ABCMeta):

    @abstractmethod
    def convert(self, fp, **kwargs):
        pass

class Base(object):

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.storage_name] = value

    @classmethod
    def check(cls, valus):
        pass
