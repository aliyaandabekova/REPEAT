class AgeDescriptor:
    def __init__(self,param):
        self.param = param

    def __get__(self, instance, owner):
        return instance.__dict__[self.param]

    def __set__(self, instance, value):
        if isinstance(value,int):
            if 0 < value <= 250:
                instance.__dict__[self.param] = value
            else:
                raise ValueError('Invalid number!')
        else:
            raise ValueError('Must be int!')



class NameDescriptor:
    def __init__(self,param):
        self.param = param

    def __set__(self, instance, value):
        if isinstance(value,str):
            if len(value) < 50:
                if value.isalpha():
                    instance.__dict__[self.param] = value
                else:
                    raise ValueError('Only alphas!')
            else:
                raise ValueError('Too long name!')
        else:
            raise ValueError('Must be str!')


class Human:
     age = AgeDescriptor('age')
     name = NameDescriptor('name')

     def __init__(self, name, age):
         self.name = name
         self.age = age
h1 = Human('john','18')
print(h1.__dict__)
