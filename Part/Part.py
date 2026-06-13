# Class Part for each part
class Part:
    def __init__(self, ID, name, price):
        self.__ID = ID
        self.__name = name
        self.__price = price

    # Getters
    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # Setters
    def set_ID(self, ID):
        self.__ID = ID

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def display_info(self):
        print(f'{self.__ID:<20}{self.__name:<22}{self.__price}')