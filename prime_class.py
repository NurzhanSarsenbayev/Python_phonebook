class Car:

    class_atr = 0

    def __init__(self, label: str, color: str, year: int, audio: str = 'No'):
        self.label = label
        self.color = color
        self.year = year
        self.audio = audio

    def __str__(self):
        return f'Car label is {self.label}, color is {self.color}, was produced in {self.year}'

    def drive(self):
        print('Vroom')


my_car = Car('Mazda', 'black', 2019)
my_car.drive()
print(my_car.label)
print(my_car.color)
print(my_car.year)

my_car.audio = 'Dolby'

new_car = Car('BMW', 'white', 2023)
print(new_car.label)
print(new_car.color)
print(new_car.year)

old_car = Car('Audi', 'green', 1992)

auto_park = [my_car, new_car, old_car]
for car in auto_park:
    print(car.audio)

# b = 'string of text'
# print (b)
print(my_car)
print(new_car)
print (old_car)