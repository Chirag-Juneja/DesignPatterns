# Interface Segregation Principle (ISP)
# ISP states that no code should be forced to depend on methods it does not use.

from abc import abstractmethod


class Machine:
    def print(self,document):
        raise NotImplementedError()
    def scan(self,document):
        raise NotImplementedError()
    def fax(self,document):
        raise NotImplementedError()

class MultiFunctionPrinter(Machine):
    def print(self,document):
        pass
    def scan(self,document):
        pass
    def fax(self,document):
        pass

# does not support scan and fax
class OldPrinter(Machine):
    def print(self,document):
        pass

# Interface Segregation 
class Printer:
    @abstractmethod
    def print(self,document):
        pass

class Scanner:
    @abstractmethod
    def scan(self,document):
        pass

class Fax:
    @abstractmethod
    def fax(self,document):
        pass

class Photocopier(Printer,Scanner):
    def print(self,document):
        pass
    def scan(self,doumnet):
        pass