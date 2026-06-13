from Customer.Member import Member

# Class Premium Member for each premium member which is child class of Member class

class PremiumMember(Member):
    def __init__(self, ID, name, discount_rate, service_credit):
        super().__init__(ID, name, discount_rate)
        self.__service_credit = service_credit

    # Getter
    def get_service_credit(self):
        return self.__service_credit

    def get_credit(self, discount_price):
        credit = discount_price // 100
        return credit

    # Setter
    def set_service_credit(self, service_credit):
        self.__service_credit = service_credit

    def update_credit(self, credit):
        self.__service_credit = int(float(self.__service_credit) + credit)
        self.__service_credit = str(self.__service_credit)

    def display_info(self):
        print(f'{self.get_ID():<42}{self.get_name():<44}{self.get_discount_rate():<44}{self.__service_credit}')