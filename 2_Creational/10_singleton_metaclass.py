# metaclass defines the behaviours of class and its instance
# 'type' is a metaclass of all classes
# https://realpython.com/python-metaclasses/


class Singleton(type):
    _instances = {}

    # __call__ enables user to write classes where the instances behave like functions
    # and can be called like a function
    # https://www.geeksforgeeks.org/__call__-in-python/
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)