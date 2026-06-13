from datetime import datetime

from Record.Record import Record
from Services.ServiceJob import ServiceJob


#Main class containing menu logic for running the program

class Main:
    records = Record()

    def __init__(self):
        self.option = 0
        self.__customer_name = ""
        self.__part_ID = ""
        self.__service_ID = ""
        self.__service_hour = None
        self.__customer = None
        self.__service = None
        self.__part = None
        self.__service_package = None
        self.__cust_check = False
        self.__service_package_ID = ""
        self.__service_list = []

    def disp_menu(self):
        print('Welcome to the RMIT car repair shop ! \n')
        print('###########################################################################')
        print('You can chose from the following options:')
        print('1. Perform a service')
        print('2. Update Services')
        print('3. Update Parts')
        print('4. Display existing Customer')
        print('5. Display existing Services')
        print('6. Display existing Parts')
        print('7. Display existing Service Jobs')
        print('8. Exit the program')
        print('###########################################################################')
        try:
            self.option = int(input("Enter option to chose: \n"))
        except Exception as e:
            print(f'Error caused: {e}')

    # Function to check that customer name is correct format
    def getcust_name(self):
        customer_name = input('Enter name or ID of the customer [e.g. Tim] : \n')
        cust_validity = True
        while (cust_validity):
            if (customer_name[0] in ['C', 'P', 'M']):
                if (customer_name[1:].isdigit()):
                    cust_validity = False
                elif (customer_name.isalpha()):
                    cust_validity = False
            if (customer_name.isalpha()):
                cust_validity = False
            else:
                print("The name is not in correct format please try again \n")
                customer_name = input('Enter name or ID of the customer [e.g. Tim] : \n')
        return customer_name

    # Function to check if service is valid
    def getservice_ID(self):
        self.__service_ID = input('Enter the service ID or name \n')
        self.__service = Main.records.find_service(self.__service_ID)
        while (self.__service == None):
            print("The entered service does not exist please enter a valid service")
            self.__service_ID = input('Enter the service ID or name \n')
            self.__service = Main.records.find_service(self.__service_ID)

    # Function to get service_package and check if it exists
    def getservice_package(self):
        self.__service_package_ID = input('Enter service package ID or name \n')
        self.__service_package = Main.records.find_service(self.__service_package_ID)
        while (self.__service_package == None):
            print("The entered service package does not exist please try again")
            self.__service_package_ID = input('Enter service package ID or name \n')
            self.__service_package = Main.records.find_service(self.__service_package_ID)

    # Function to check the validity of service hours
    def getservice_hours(self):
        try:
            self.__service_hour = float(input('Enter the hours of service required [enter valid hours e.g 2.5]: \n'))
        except:
            print("Service hour is not a number. Please try again \n")
            return False
        if (self.__service_hour < 1 or self.__service_hour % 0.5 != 0):
            print("Service is less than 1 or not in increments of 0.5 please try again \n")
            return False
        else:
            return True

    # Function to check validity of part entered by the user
    def getpart_ID(self):
        self.__part_ID = input('Enter the part ID or name \n')
        self.__part = Main.records.find_part(self.__part_ID)
        while (self.__part == None):
            print("The entered part does not exist please enter correct part_ID")
            self.__part_ID = input('Enter the part ID or name \n')
            self.__part = Main.records.find_part(self.__part_ID)

    # Function to check if customer is new or exists
    def customer_check(self):
        if self.__customer == None:
            return True
        else:
            return False

    # Function to check if part is required for the service entered
    def part_required_check(self, service):
        if service.get_require_part() == 'yes':
            return True
        else:
            return False

    # Function to check if service hours needs to be inputted by user
    def service_hour_check(self, service):
        if service.get_require_user_input_hour() == 'yes':
            return True
        else:
            return False

    # Function to get all inputs required by the user to perform a service
    def get_details(self):
        self.__customer_name = self.getcust_name()
        self.__customer = Main.records.find_customer(self.__customer_name)
        self.__cust_check = self.customer_check()  # Variable to check if customer is present in the datbase or not it is true when customer is new
        choice = input("Would you like to use a service package instead of a service. Please answer [ Y or N ] \n")
        package_check = True  # Boolean value to make sure user enters correct input for package choice
        while package_check:
            if (choice == 'Y'):
                self.getservice_package()
                service_list = self.__service_package.get_service_list()
                # For loop to filter each service and get service hour or part
                parts_list = []
                service_hour_list = []
                cost_per_hour_list = []
                for service_name in service_list:
                    self.__service = Main.records.find_service(service_name)
                    if (self.part_required_check(
                            self.__service)):  # Program will ask for part only if the service requires it
                        self.getpart_ID()
                        parts_list.append(self.__part)
                    if (self.service_hour_check(self.__service)):
                        service_hour_valid = self.getservice_hours()
                        while (
                                service_hour_valid == False):  # While loop in case user inputs inoccrect format for service hours
                            service_hour_valid = self.getservice_hours()
                        self.__service.set_service_hour(self.__service_hour)
                    else:
                        self.__service_hour = self.__service.get_service_hour()
                    self.__service_list.append(self.__service)
                    service_hour_list.append(self.__service_hour)
                    cost_per_hour_list.append(self.__service.get_cost_per_hour())
                self.__service_package.set_cost_per_hour_list(
                    cost_per_hour_list)  # To keep a list of cost_per_hour for each service
                self.__service_package.set_service_hour_list(
                    service_hour_list)  # Added service hours to the list of service hours
                self.__service_package.set_part_list(parts_list)  # Added parts to the parts list in service job
                package_check = False
            elif choice == 'N':
                self.getservice_ID()
                if (
                self.part_required_check(self.__service)):  # Program will ask for part only if the service requires it
                    self.getpart_ID()
                if (self.service_hour_check(self.__service)):
                    service_hour_valid = self.getservice_hours()
                    while (
                            service_hour_valid == False):  # While loop in case user inputs inoccrect format for service hours
                        service_hour_valid = self.getservice_hours()
                    self.__service.set_service_hour(self.__service_hour)
                else:
                    self.__service_hour = self.__service.get_service_hour()
                package_check = False
            else:
                print("Choice entered was not in correct format please try again")
                choice = input("Would you like to use a service package instead of a service. Please answer [ Y or N ]")
        return choice

    # Logic to update users after menu driven program is completed
    def update_cust_file(self, file_list):
        customer_file = open('meta_data/customers.txt', 'w')
        for customer in file_list:
            customer_file.writelines(customer)

    # Logic to update services after menu driven program in completed
    def update_service_file(self, file_list):
        service_file = open('meta_data/services.txt', 'w')
        for service in file_list:
            service_file.writelines(service)

    # Logic to update parts after menu driven program in completed
    def update_part_file(self, file_list):
        parts_file = open('meta_data/parts.txt', 'w')
        for parts in file_list:
            parts_file.writelines(parts)

    def menu_logic(self):
        cust_file_check = Main.records.read_customers()
        service_file_check = Main.records.read_services()
        part_file_check = Main.records.read_parts()
        service_job_file_check = Main.records.read_service_job()
        if (not (cust_file_check and service_file_check and part_file_check and service_job_file_check)):
            cust_file_check = False
            service_file_check = False
            part_file_check = False
            self.disp_menu()
            while (self.option != 8):
                if self.option == 1:
                    choice = self.get_details()
                    if (choice == 'Y'):
                        service_job = ServiceJob(self.__customer, self.__service_package, self.__cust_check,
                                                 self.__service_hour, self.__part)
                        payment_list = service_job.compute_package_cost()
                        service_job.disp_bill(payment_list, Main.records, self.__customer_name, choice, self.__service_list,
                                              self.__service_package.get_name(), self.__service_package.get_part_list())
                        self.__service_package.set_part_list(
                            [])  # Necessary step so that in the next run parts of the previous run are not included
                        self.__service_package.set_service_hour_list(
                            [])  # Necessary step so that in the next run service_hours of the previous run are not included
                        time_stamp = datetime.now()
                        formatted_time = time_stamp.strftime(
                            "%d/%m/%Y %H:%M:%S")  # formatting time_Stamp to required format
                        service_job.set_time_stamp(formatted_time)  # setting time stamp for particular service job
                        self.__part = None
                        self.__service_list = []
                    else:
                        service_job = ServiceJob(self.__customer, self.__service, self.__cust_check,
                                                 self.__service_hour, self.__part)
                        payment_list = service_job.compute_cost()
                        service_job.disp_bill(payment_list, Main.records, self.__customer_name)
                        time_stamp = datetime.now()
                        formatted_time = time_stamp.strftime(
                            "%d/%m/%Y %H:%M:%S")  # formatting time_Stamp to required format
                        service_job.set_time_stamp(formatted_time)  # setting time stamp for particular service job
                elif self.option == 2:
                    Main.records.update_service()
                    service_file_check = True
                elif self.option == 3:
                    Main.records.update_parts()
                    part_file_check = True
                elif self.option == 4:
                    Main.records.list_customer()
                elif self.option == 5:
                    Main.records.list_services()
                elif self.option == 6:
                    Main.records.list_parts()
                elif self.option == 7:
                    Main.records.list_service_jobs()
                else:
                    print('Wrong input was provided for option please try again')
                    print('\n')
                self.option = 0
                self.disp_menu()
            file_list = Main.records.cust_update()
            self.update_cust_file(file_list)
            if (service_file_check):
                file_list = Main.records.service_update()
                self.update_service_file(file_list)
            if (part_file_check):
                file_list = Main.records.part_update()
                self.update_part_file(file_list)

            print("Thank you exiting the program")
        else:
            print("One of the files does not exist please add the files to the current directory and please try again")
