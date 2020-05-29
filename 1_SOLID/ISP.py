# ISP (Interface Segregation Principle)
from abc import abstractmethod

# Not a good interface design
class Machine:
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass

# Still problematic with not used methods
class OldFashionedPrinter(Machine):
    def print(self, document):
        #ok
        pass
    def fax(self, document):
        pass #noop (no operation)
    def scan(self, document):
        """Not supported"""
        raise NotImplementedError('Printer cannot scan!')


# These interfaces are better practice
# Break into small interfaces
# Let user implement essential functionalities only
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)