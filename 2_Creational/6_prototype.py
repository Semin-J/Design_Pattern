import copy

class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'



if __name__ == "__main__":
    '''
    # Issue of using this, if Jane moves out, we can't Jane's address by itself
    address = Address('55 Yonge street', 'Toronto', 'Canada')
    mini = Person('Mini', address)
    print(mini)

    #jane = mini  # This is shallow copy
    jane = Person('Jane', address)
    '''

    mini = Person('Mini', Address('55 Yonge street', 'Toronto', 'Canada'))
    jane = copy.deepcopy(mini)  # deepy copy of the object recursively
    jane.name = 'Jane'
    jane.address.street_address = '33 Yonge street'
    print(jane)
    print(mini)