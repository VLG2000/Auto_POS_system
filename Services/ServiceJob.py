from Customer.Customer import Customer
from Customer.Member import Member
from Customer.PremiumMember import PremiumMember

# Class for performing a service and printing the receipt


class ServiceJob:
    membership_fee = 50  # static variable as it should not be changed
    service_package_discount = 0.25  # the discount percentage of service_package is kept at 75% and static as its value should not change

    def __init__(self, customer, service, cust_check, service_hour=None, part=None):
        self.__customer = customer
        self.__service = service
        self.__part = part
        self.__service_hour = service_hour
        self.__cust_check = cust_check
        self.__original_cost = ""
        self.__discount = ""
        self.__total_cost = ""
        self.__credit = ""
        self.__time_stamp = ""

    # Getters
    def get_customer(self):
        return self.__customer

    def get_service(self):
        return self.__service

    def get_part(self):
        return self.__part

    def get_service_hour(self):
        return self.__service_hour

    def get_cust_check(self):
        return self.__cust_check

    def get_original_cost(self):
        return self.__original_cost

    def get_discount(self):
        return self.__discount

    def get_total_cost(self):
        return self.__total_cost

    def get_credit(self):
        return self.__credit

    def get_time_stamp(self):
        return self.__time_stamp

    # Setters
    def set_customer(self, customer):
        self.__customer = customer

    def set_service(self, service):
        self.__service = service

    def set_part(self, part):
        self.__part = part

    def set_service_hour(self, service_hour):
        self.__service_hour = service_hour

    def set_cust_check(self, cust_check):
        self.__cust_check = cust_check

    def set_original_cost(self, original_cost):
        self.__original_cost = original_cost

    def set_discount(self, discount):
        self.__discount = discount

    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost

    def set_credit(self, credit):
        self.__credit = credit

    def set_time_stamp(self, time_stamp):
        self.__time_stamp = time_stamp

    # function to check if customer is a member or premium member
    def mem_check(self, customer):
        customer_ID = customer.get_ID()
        if (customer_ID[0] == 'M'):
            return 'M'
        elif (customer_ID[0] == 'P'):
            return 'P'
        else:
            return 'C'

    # function that computes cost and gives service credit based on member or premium meber or parts required
    def compute_cost(self):
        cost_per_hour = float(self.__service.get_cost_per_hour())
        total_cost = 0
        discount = 0
        service_fee = 0
        service_credit = 0

        # Logic for calculation based on part required or not
        if (self.__part == None):
            service_fee = cost_per_hour * float(self.__service_hour)
        else:
            service_fee = cost_per_hour * float(self.__service_hour) + float(self.__part.get_price())
        # Logic for calculation based on customer status i.e customer/ member/ premium member
        if self.__cust_check:
            total_cost = service_fee
        elif (self.mem_check(self.__customer) == 'M'):
            discount = self.__customer.get_discount(service_fee)
            total_cost = service_fee - (discount)
        elif (self.mem_check(self.__customer) == 'P'):
            discount = self.__customer.get_discount(service_fee)
            total_cost = service_fee - (discount)
            service_credit = self.__customer.get_credit(total_cost)

            # Logic to remove credits from premium member in case the service is inspection and keeo the fee free of cost
            customer_credit = self.__customer.get_service_credit()
            if (int(customer_credit) >= 5 and self.__service.get_ID() == 'S01'):
                total_cost = 0
                discount = 0
                service_credit = -5

            self.__customer.update_credit(service_credit)
            return [service_fee, discount, total_cost, service_credit]
        else:
            total_cost = service_fee
        return [service_fee, discount, total_cost]

    # function that computes cost and gives service credit based on member or premium meber or parts required for packages
    # In this function we are assuming that discount is only for the service package not the customer status i.e member or premium member
    def compute_package_cost(self):
        service_hour_list = self.__service.get_service_hour_list()
        part_list = self.__service.get_part_list()
        cost_per_hour_list = self.__service.get_cost_per_hour_list()

        total_cost = 0
        discount = 0
        service_fee = 0
        service_credit = 0

        # calcualting service fee and discount after using service package
        for i in range(len(service_hour_list)):
            service_fee += float(cost_per_hour_list[i]) * float(service_hour_list[i])
        discount = service_fee * self.service_package_discount

        # calculating price after including the part_price
        for part in part_list:
            service_fee += float(part.get_price())
        total_cost = service_fee - discount

        # Logic for getting service_credit for premium member
        if (self.__cust_check == False and self.mem_check(self.__customer) == 'P'):
            service_credit = self.__customer.get_credit(total_cost)
            self.__customer.update_credit(service_credit)
            return [service_fee, discount, total_cost, service_credit]
        else:
            return [service_fee, discount, total_cost]

    # Function to display bill and to add membership for new customer
    def disp_bill(self, payment_list, record, customer_name='', package_choice='', service_list=[], service_package_name='',
                  part_list=[]):
        premium_choice = ''
        if (self.__cust_check):
            choice = input(
                "We see that you are a new customer would you like to take a membership please answer with [Y or N] \n")
            choice_check = True
            while (choice_check):
                if (choice == 'Y'):
                    print(
                        "Thank you for chosing to be a member with us we have two options Standard (FREE of cost) and Premium (50 AUD with store credits)")
                    premium_choice = input("Please chose : [P or M] according to your requirement \n")
                    if (premium_choice == 'M'):
                        record.max_mem_id += 1  # Logic to create new member_ID
                        member = Member('M' + str(record.max_mem_id), customer_name, '0.10')
                        record.customer_list.append(member)
                        print("You have been succesfully registered as a standard member.")
                    elif (premium_choice == 'P'):
                        record.max_prem_id += 1  # Logic to create new Permium member ID
                        premium_member = PremiumMember('P' + str(record.max_prem_id), customer_name, '0.10', '0')
                        record.customer_list.append(premium_member)
                        print(
                            "You have been succesfully registered as a premium member.Please note a membership fee of 50 AUD will be added to the bill")
                        payment_list[2] += ServiceJob.membership_fee
                        service_credit = premium_member.get_credit(payment_list[2])
                        premium_member.update_credit(service_credit)
                    choice_check = False
                elif (choice == 'N'):
                    print("You will be registered as a regualr customer.")
                    record.max_cust_id += 1  # logic to create new customer_ID
                    customer = Customer('C' + str(record.max_cust_id), customer_name)
                    record.customer_list.append(customer)
                    choice_check = False
                else:
                    print("The input entered was not the expected input please try again")
                    choice = input(
                        "We see that you are a new customer would you like to take a membership please answer with [Y or N]")

        print('---------------------------------------------------------------------------')
        print('                                  Reciept                                  ')
        print('---------------------------------------------------------------------------')
        if package_choice == 'Y':
            print(service_package_name)
            for service in service_list:
                print(
                    f'{service.get_name():11}:{float(service.get_service_hour()):56,.2f} X {service.get_cost_per_hour()}')
            for part in part_list:
                print(f'{part.get_name():11}:{float(part.get_price()):63,.2f}')
        else:
            print(
                f'{self.__service.get_name():11}:{float(self.__service.get_service_hour()):56,.2f} X {self.__service.get_cost_per_hour()}')
            if (self.__part != None):
                print(f'{self.__part.get_name():11}:{float(self.__part.get_price()):63,.2f}')
        print('---------------------------------------------------------------------------')
        print(f'Original cost:{payment_list[0]:56,.2f}(AUD)')
        print(f'discount:{payment_list[1]:61,.2f}(AUD)')
        if (premium_choice == 'P'):
            print(f'Membership fee:{ServiceJob.membership_fee:55,.2f}(AUD)')
        print(f'Total cost:{payment_list[2]:59,.2f}(AUD)')
        if (self.__cust_check != True):
            if (self.mem_check(self.__customer) == 'P'):
                print(f'Credit:{payment_list[3]:63,.2f}(AUD)')
        elif (premium_choice == 'P'):
            print(f'Credit:{0.0:63,.2f}(AUD)')
        print('\n')

    # To display all service jobs done
    def disp_info(self, service, record):
        if (record.find_service(service).get_ID()[:2] != 'SP'):
            print(f'{self.__customer.get_name():<15}{self.__service.get_ID():<8}{self.__service.get_service_hour():<7}',
                  end="")
            if (self.__part != None):
                print(f'{self.__part.get_ID():<10}', end="")
            else:
                print(f"{'na':<10}", end="")
            print(
                f'{self.get_original_cost():<9}{self.get_discount():<7}{self.get_total_cost():<9}{self.get_credit():<9}{self.get_time_stamp()}')

        else:
            print(f'{self.__customer.get_name():<15}{self.__service.get_ID():<8}', end="")
            part_count = 0
            service_count = 0
            for service_iterator in self.__service.get_service_list():
                print(
                    f'{record.find_service(service_iterator).get_ID():<8}{record.find_service(service_iterator).get_service_hour():<8}',
                    end="")
                if (record.find_service(service_iterator).get_require_part() == 'yes'):
                    print(f'{record.find_service(service).get_part_list()[part_count]:<10}', end="")
                    part_count += 1
                else:
                    print(f'{'na':<10}', end="")
                service_count += 1
            for i in range(service_count, 3):
                print(f'{'na':<8}{'na':<8}{'na':<8}', end="")
            print(
                f'{self.get_original_cost():<9}{self.get_discount():<7}{self.get_total_cost():<9}{self.get_credit():<9}{self.get_time_stamp()}')
