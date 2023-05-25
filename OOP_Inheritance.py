class Animal():
    def __init__(self) -> None:
        print('Animal Created.')

    def speak(self, spk = 'Animal Speaking'):
        print(spk)
 
    def eat(self):
        print('Eating')


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
        print('Dog Created.')


class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()
        print('Cat Created.')



d = Dog()
d.eat()
d.speak('Woof!')

c = Cat()
c.eat()
c.speak('Meow!')

