class Person:
    def __init(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'


# This approach violates open-close principle
# since it requires to modify parent class
# when it has new child class

class PersonBuilder:
    def __init__(self, person=Person()):
        # good to use default constructor in parameter
        # no need to construct additionally in body
        self.person = person

    @property
    def works(self):
        # now we can use self.person which constructed above!
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


# Fluent Interface in Python (more in google)
# Return 'self' and let user chain other methods on that


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        # parent already had Person(), so no need on here anymore
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self  # fluent interface

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonBuilder()
person = pb\
    .lives\
        .at('55 yonge')\
        .in_city('Toronto')\
        .with_postcode('M1J0n3')\
    .works\
        .at('33 yonge')\
        .as_a('Engineer')\
        .earning(150000)\
    .build()
print(person)