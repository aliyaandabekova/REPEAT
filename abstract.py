import abc

class Furniture(abc.ABC):

    # @abc.abstractmethod
    def comfort(self):
        pass

    # @abc.abstractmethod
    def construction(self):
        pass


class Chair(Furniture):

    def comfort(self):
        print('comfortable chair')

    def construction(self):
        print('construction of chair')

class Table(Furniture):

    def comfort(self):
        print('comfortable table')

    def construction(self):
        print('construction of table')

chair1 = Chair()
table1 = Table()
print(chair1.__dict__)
print(table1.__dict__)

class Timer:
    import time

    def __enter__(self):
        self.start_time = self.time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.time.time() - self.start_time)

with Timer() as t:
    for i in range(10000000):
        pass