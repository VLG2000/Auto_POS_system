from Customer.Customer import Customer

# Class Member for each member which is child class with parent class as Customer

class Member(Customer):
    discount_rate = 0.1  # Static variable

    def __init__(self, ID, name, discount_rate=None):
        super().__init__(ID, name)
        if (discount_rate == None):
            self.__discount_rate = Member.discount_rate
        else:
            self.__discount_rate = discount_rate

    # Getter
    def get_discount_rate(self):
        return self.__discount_rate

    def get_discount(self, service_cost):
        discount = service_cost * float(self.__discount_rate)
        return discount

    # Setter
    def set_discount_rate(self, discount_rate):
        self.__discount_rate = discount_rate

    def display_info(self):
        print(f'{self.get_ID():<42}{self.get_name():<44}{self.__discount_rate:<44}na')