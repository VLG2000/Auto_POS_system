# Class Service for each service
class Service:
    def __init__(self, ID, name, cost_per_hour, require_user_input_hour, service_hour, require_part):
        self.__ID = ID
        self.__name = name
        self.__cost_per_hour = cost_per_hour
        self.__require_user_input_hour = require_user_input_hour
        self.__service_hour = service_hour
        self.__require_part = require_part

    # Getters
    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_cost_per_hour(self):
        return self.__cost_per_hour

    def get_require_user_input_hour(self):
        return self.__require_user_input_hour

    def get_service_hour(self):
        return self.__service_hour

    def get_require_part(self):
        return self.__require_part

    # Setters
    def set_ID(self, ID):
        self.__ID = ID

    def set_name(self, name):
        self.__name = name

    def set_cost_per_hour(self, cost_per_hour):
        self.__cost_per_hour = cost_per_hour

    def set_require_user_input_hour(self, require_user_input_hour):
        self.__require_user_input_hour = require_user_input_hour

    def set_service_hour(self, service_hour):
        self.__service_hour = service_hour

    def set_require_part(self, require_part):
        self.__require_part = require_part

    def compute_service_cost(self, service_hour):
        cost = self.__cost_per_hour * service_hour
        return cost

    def display_info(self):
        print(
            f'{self.__ID:<17}{self.__name:<19}{self.__cost_per_hour:<28}{self.__require_user_input_hour:<38}{self.__service_hour:<27}{self.__require_part}')