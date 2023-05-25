class Human():
    def __init__(self, name, continent = 'Asia'):
        self.continent = continent
        self.name = name


    def change_continent(self, newname):
        self.continent = newname
        return "Successfuly changed."


x = Human('Shahzaib')
y = Human('Subhan', continent='Africa')


x.continent = 'North America'

print(f'{x.name} is from {x.continent}.')
print(f'{y.name} is from {y.continent}.')

status = y.change_continent('Europe')

print(status)
print(f'{y.name} moved to {y.continent}.')
