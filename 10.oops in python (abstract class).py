from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def abc(self):
        pass

class bike(vehicle):
    def __init__(self, name):
        self.name = name

    def name_dif(self):
        print(f"name of the bike is {self.name}")

    def abc(self):
        print("Implementing abc in bike class")

b = bike("Rx")
print(b.name)
b.name_dif()
b.abc()
