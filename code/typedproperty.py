# from David Beazley o'reilly course. 

def typed_property(name, expected_type):
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Value expected: {expected_type}')
        setattr(self, private_name, value)

        return prop

Integer = lambda name: typed_property(name, int)
Float = lambda name: typed_property(name, float)
String = lambda name: typed_property(name, str)

class Holding:
#   shares = typed_property('shares', int)
#   price = typed_property('price', float)
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

if __name__ == '__main__':
    h = Holding(1, 2.0)
