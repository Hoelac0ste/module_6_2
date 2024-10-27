class Vehicle:

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['white', 'black', 'gray', 'metallic']

    def get_model(self):
        return (f'Модель: {self.__model}')

    def get_horsepower(self):
        return (f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return (f'Цвет: {self.__color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец {self.owner}')

    def set_color(self, new_color):
        able_to_change = False
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() in i.lower():
                able_to_change = True
            else:
                continue
        if able_to_change:
            self.__color = new_color
            print(f'Цвет {self.__model} изменён на {new_color}')
        else:
            print(f'Нельзя изменить цвет {self.__model} на {new_color}')


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5


v1 = Vehicle('Max', 'Chevrolet Impala 1967', 155, 'black')
s1 = Sedan('Andrew', 'Genesis G70', 197, 'metallic')
s1.print_info()
v1.set_color('green')
s1.set_color('bLaCK')
