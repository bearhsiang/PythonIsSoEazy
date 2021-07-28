class Pet:

    sound = 'woof'

    def __init__(self, name):

        self.name = name

    def sayHello(self):

        print(self.sound)

class Dog(Pet):

    sound = 'woof'

    def __init__(self, name):

        super().__init__(name)

class Cat(Pet):
    
    sound = 'meow'

    def __init__(self, name):

        super().__init__(name)

if __name__ == '__main__':

    d = Dog('haah')
    c = Cat('dfjs')
    print(isinstance(d, Dog))
    print(isinstance(d, Pet))
    print(isinstance(c, Dog))
    print(isinstance(c, Pet))