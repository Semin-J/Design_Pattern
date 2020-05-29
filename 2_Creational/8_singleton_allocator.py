 # Example of singleton would be for the entity
 # you want to initialize only once
 # Such as DB for application
 # Since it has no reason to load DB for application several times
 # after the application started

import random



class Database:
    _instance = None

    # We don't want to initialize DB every single time when we create DB object
    def __init__(self):
        id = random.randint(1, 101)
        print('id = ', id)


    # __new__ keyword: https://howto.lintel.in/python-__new__-magic-method-explained
    # __new__ is called to create an object
    # when it returns its own class, it invokes __init__ implicitly
    # if it doesn't return own clas, you need to call __init__ yourself

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # if the _instance was not initalized
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)
        return cls._instance



if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)