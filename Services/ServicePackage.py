# Class for service Package
class ServicePackage:

    def __init__(self, ID, name, service_list, service_hour_list=None, part_list=None):
        self.ID = ID
        self.name = name
        self.service_list = service_list
        self.service_hour_list = service_hour_list
        self.part_list = part_list
        self.cost_per_hour_list = []

    # Getters
    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_service_list(self):
        return self.service_list

    def get_service_hour_list(self):
        return self.service_hour_list

    def get_part_list(self):
        return self.part_list

    def get_cost_per_hour_list(self):
        return self.cost_per_hour_list

    # Setters
    def set_ID(self, ID):
        self.ID = ID

    def set_name(self, name):
        self.name = name

    def set_service_list(self, service_list):
        self.service_list = service_list

    def set_service_hour_list(self, service_hour_list):
        self.service_hour_list = service_hour_list

    def set_part_list(self, part_list):
        self.part_list = part_list

    def set_cost_per_hour_list(self, cost_per_hour_list):
        self.cost_per_hour_list = cost_per_hour_list

    def display_info(self):
        service_string = ''
        # logic to get list of servies in string format
        for service in self.service_list:
            if service_string == '':
                service_string = service_string + service
            else:
                service_string = service_string + ',' + service
        print(f'{self.ID:<17}{self.name:<34}{service_string}')