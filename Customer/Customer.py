# Class customer for each normal customer
class Customer:
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name  # Made ID and name into private variables

    # Getters
    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    # Setters
    def set_ID(self, ID):
        self.__ID = ID

    def set_name(self, name):
        self.__name = name

    def display_info(self):
        print(f"{self.__ID:<42}{self.__name:<44}{'na':<44}{'na'}")
