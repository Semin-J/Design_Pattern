# DIP (Dependency Inversion Principle) - Not Dependency Injection
# High level class(module) shouldn't be directly dependent on lower level module
# That should be dependent on abstraction(interface)

from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass

# You might want to do unit test, not using real DB data
# can create fake-class like this for testing
class Relationships(RelationshipBrowser):  # low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research: # High-level
    # def __init__(self, relationships):
    #     # This is the dependcy! if Relationships is changed, this module will be broke
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}.')


if __name__ == "__main__":
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Jane')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships)