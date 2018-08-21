
from csv2any.validators import UTF8, URL, NonEmpty, Rating

class Row(object):
    name = UTF8('name')
    uri = URL('uri')
    stars = Rating('stars')
    address = NonEmpty('address')
    contact = NonEmpty('contact')
    phone = NonEmpty('phone')

    def __init__(self, name, uri, stars, address, contact, phone):
        self.name = name
        self.uri = uri
        self.stars = stars
        self.address = address
        self.contact = contact
        self.phone = phone

    def to_dict(self):
        return {
            'name': self.name,
            'uri': self.uri,
            'stars': self.stars,
            'address': self.address,
            'contact': self.contact,
            'phone': self.phone
        }
