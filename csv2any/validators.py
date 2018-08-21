
from csv2any.base import Base
import re

_URL_REGEX = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\\(\)\*\+,;=.]+$"
_URL = re.compile(_URL_REGEX)


class Tyoed(Base):
    type = None

    @classmethod
    def check(cls, value):
        assert isinstance(value, cls.type), f"Expected {cls.type}"

class Integer(Tyoed):
    type = int

class String(Tyoed):
    type = str

class UTF8(Base):

    @classmethod
    def check(cls, value):
        try:
            value.decode('utf-8')
        except:
            raise UnicodeError("string is not UTF-8")

class URL(Base):

    @classmethod
    def check(cls, value):
        assert _URL.match(value), 'Invalid URL'

class Rating(Base):

    @classmethod
    def check(cls, value):
        assert 0 <= int(value) <= 5, 'Expected 0-5'

class NonEmpty(Base):
    @classmethod
    def check(cls, value):
        assert len(value) > 0, "Must be nonempty"
