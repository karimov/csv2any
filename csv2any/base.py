
from abc import ABCMeta, abstractmethod

class PluginBase(metaclass=ABCMeta):

    @abstractmethod
    def conver(self, fp, **kwargs):
        pass

class Base(object):

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, values):
        self.check(values)
        self.__dict__[self.name] = values

    @classmethod
    def check(cls, valus):
        pass
