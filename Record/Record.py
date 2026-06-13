
from Customer.Customer import Customer
from Customer.Member import Member
from Customer.PremiumMember import PremiumMember
from Part.Part import Part
from Services.Service import Service
from Services.ServiceJob import ServiceJob
from Services.ServicePackage import ServicePackage

# Class Record to read and keep record of all details for customers,service and part

class Record:
    def __init__(self):
        self.customer_list = []
        self.part_list = []
        self.service_list = []
        self.service_job_list = []
        self.max_cust_id = 0
        self.max_mem_id = 0
        self.max_prem_id = 0
        self.max_part_id = 0

    # For reading customers/ Mmbers/ Premium Members form customers file
    def read_customers(self):
        try:
            customer_file = open('meta_data/customers.txt')
        except FileNotFoundError:
            return True
        for cust in customer_file:
            customer_details = [detail.strip() for detail in cust.split(',')]
            if customer_details[2] == 'na' and customer_details[3] == 'na':
                self.largest(customer_details[0])
                customer = Customer(customer_details[0], customer_details[1])
                self.customer_list.append(customer)
            elif customer_details[2] != 'na' and customer_details[3] == 'na':
                self.largest(customer_details[0])
                member = Member(customer_details[0], customer_details[1], customer_details[2])
                self.customer_list.append(member)
            else:
                self.largest(customer_details[0])
                premium_member = PremiumMember(customer_details[0], customer_details[1], customer_details[2],
                                               customer_details[3])
                self.customer_list.append(premium_member)

    # For reading services from service file
    def read_services(self):
        try:
            service_file = open('meta_data/services.txt')
        except FileNotFoundError:
            return True
        for i in service_file:
            service_details = [detail.strip() for detail in i.split(',')]
            # Logic for adding service_apckage into the service list
            if (service_details[0][:2] == 'SP'):
                service_package_list = []
                service_list = []
                for i in range(len(service_details)):
                    if i > 1:
                        service_list.append(service_details[i])
                    else:
                        service_package_list.append(service_details[i])
                service_package_list.append(service_list)
                service = ServicePackage(service_package_list[0], service_package_list[1], service_package_list[2])
            else:
                service = Service(service_details[0], service_details[1], service_details[2], service_details[3],
                                  service_details[4], service_details[5])
            self.service_list.append(service)

    # For reading parts from parts file
    def read_parts(self):
        try:
            parts_file = open('meta_data/parts.txt')
        except FileNotFoundError:
            return True

        for i in parts_file:
            part_details = [detail.strip() for detail in i.split(',')]
            part = Part(part_details[0], part_details[1], part_details[2])
            if (int(part_details[0][1:]) > self.max_part_id):
                self.max_part_id = int(part_details[0][1:])
            self.part_list.append(part)

    # For reading service_jobs
    def read_service_job(self):
        try:
            service_jobs_file = open('meta_data/service_jobs.txt')
        except FileNotFoundError:
            return True
        for i in service_jobs_file:
            service_job_details = [detail.strip() for detail in i.split(',')]
            customer = self.find_customer(service_job_details[0])
            service = self.find_service(service_job_details[1])
            part = None
            service_hour = ''
            service_hour_list = []
            service_list = []
            part_list = []
            if (service.get_ID()[:2] == 'SP'):
                i = 2
                while i <= (len(service_job_details) - 5):
                    if (self.find_service(service_job_details[i]) != None):
                        service_list.append(service_job_details[i])
                        service_hour_list.append(service_job_details[i + 1])
                        i += 1
                    if (self.find_part(service_job_details[i]) != None):
                        part_list.append(service_job_details[i])
                    i += 1
                service.set_service_hour_list(service_hour_list)
                service.set_part_list(part_list)
                service.set_service_list(service_list)
            else:
                service_hour = service_job_details[2]
                if (service_job_details[3] != 'na'):
                    part = self.find_part(service_job_details[3])
                service.set_service_hour(service_hour)
            original_cost = service_job_details[len(service_job_details) - 5]
            discount = service_job_details[len(service_job_details) - 4]
            total_cost = service_job_details[len(service_job_details) - 3]
            credits = service_job_details[len(service_job_details) - 2]
            time_stamp = service_job_details[len(service_job_details) - 1]
            service_job = ServiceJob(customer, service, False, None, part)
            service_job.set_original_cost(original_cost)
            service_job.set_discount(discount)
            service_job.set_total_cost(total_cost)
            service_job.set_credit(credits)
            service_job.set_time_stamp(time_stamp)
            self.service_job_list.append(service_job)

    # function to update services
    def update_service(self):
        update_string = input(
            'Enter list of services and service hours to be updated in the format [service1,service_hour1,service2,na...] \n')
        temp_list = update_string.split(',')
        update_list = []
        for service in temp_list:
            update_list.append(service.strip())
        index = 0
        for index in range(len(update_list)):
            # even index will be service name or ID and odd index will be na or service_hour
            if (index % 2 == 0):
                for service in self.service_list:
                    if (service.get_name() == update_list[index] or service.get_ID() == update_list[index]):
                        if update_list[index + 1] == 'na':
                            service.set_service_hour('na')
                            service.set_require_user_input_hour('yes')
                        else:
                            service.set_service_hour(update_list[index + 1])

    # function to update parts
    def update_parts(self):
        choice = input("Please enter a for adding/updating part or r for removing part \n")
        # logic for adding/updating parts
        if (choice == 'a'):
            update_string = input('Enter list of parts and prices to be updated in the format [part_1,price_1...] \n')
            temp_list = update_string.split(',')
            update_list = []
            for service in temp_list:
                update_list.append(service.strip())
            length = len(update_list)
            # every even index will be part_name and the odd index will be
            for i in range(0, length):
                if (i % 2 == 0):
                    for part in self.part_list:
                        if (part.get_name() == update_list[i] or part.get_ID() == update_list[i]):
                            part.set_price(update_list[i + 1])
                        elif (self.find_part(update_list[i]) == None):
                            ID = ''
                            if (self.max_part_id + 1 < 10):
                                ID = 'P0' + str(self.max_part_id + 1)
                            else:
                                ID = 'P' + str(self.max_part_id + 1)
                            part_object = Part(ID, update_list[i], update_list[i + 1])
                            self.part_list.append(part_object)

        # logic for deleting
        else:
            delete_string = input('Enter list of parts and prices to be updated in the format [part_1,part_2...] \n')
            delete_string = delete_string.strip()
            delete_list = delete_string.split(',')
            for item in delete_list:
                for part in self.part_list:
                    if part.get_name() == item or part.get_ID() == item:
                        self.part_list.pop(self.part_list.index(self.find_part(item)))

    # For displaying list of exisitng customers
    def list_customer(self):
        print('Customers List: ')
        print(f"{'ID':<42}{'Name':<44}{'discount_rate':<44}{'service_credit'}")
        for customer in self.customer_list:
            customer.display_info()
        print('\n')

    # For displaying list of services
    def list_services(self):
        print('Services List:')
        service_package_check = True
        print(
            f"{'ID':<17}{'Name':<19}{'cost_per_hour':<28}{'require_user_input_hour':<38}{'service_hour':<27}{'require_part'}")
        for service in self.service_list:
            if service.get_ID()[:2] == 'SP' and service_package_check:
                print("Service Packages:")
                print(f"{'ID':<17}{'Name':<34}{'Service_names'}")
                service_package_check = False
            service.display_info()
            service_package_check
        print('\n')

    # For displaying list of parts
    def list_parts(self):
        print('Parts List:')
        print(f"{'ID':<20}{'Name':<22}{'price'}")
        for part in self.part_list:
            part.display_info()
        print('\n')

    # For displaying service jobs
    def list_service_jobs(self):
        print('Service Jobs list for service packages:')
        print(
            f'{"Customer":<15}{"Package":<8}{"S1 ID":<8}{"S1 Hrs":<8}{"S1 Part":<10}{"S2 ID":<8}{"S2 Hrs":<8}{"S2 Part":<10}{"S3 ID":<8}{"S3 Hrs":<8}{"S3 Part":<10}{"Orig $":<9}{"Disc":<7}{"Total":<9}{"Credits":<9}{"Timestamp"}')
        print('-' * 130)
        for service_job in self.service_job_list:
            if service_job.get_service().get_ID()[:2] == 'SP':
                service_job.disp_info(service_job.get_service().get_ID(),self)
        print('\n')
        print('Service Job list for normal services :')
        print(
            f'{"Customer":<15}{"Service":<8}{"Hours":<7}{"Part":<10}{"Orig $":<9}{"Disc":<7}{"Total":<9}{"Credits":<9}{"Timestamp"}')
        print('-' * 80)
        for service_job in self.service_job_list:
            if service_job.get_service().get_ID()[:2] != 'SP':
                service_job.disp_info(service_job.get_service().get_ID())
        print('\n')

    # To find customer based on customer name
    def find_customer(self, customer_name):
        customer_check = False
        for customer in self.customer_list:
            if customer_name[1:].isdigit() and customer_name[0] in ['C', 'M',
                                                                    'P'] and customer.get_ID() == customer_name:
                customer_check = True
                return customer
            elif customer.get_name() == customer_name:
                customer_check = True
                return customer
        if (customer_check == False):
            return None

    # To find service based on service_ID
    def find_service(self, service_ID):
        service_check = False
        for service in self.service_list:
            if service_ID[1:].isdigit() and service_ID[0] == 'S' and service.get_ID() == service_ID:
                service_check = True
                return service
            elif service_ID[2:].isdigit() and service_ID[:2] == 'SP' and service.get_ID() == service_ID:
                service_check = True
                return service
            elif service.get_name() == service_ID:
                service_check = True
                return service
        if (service_check == False):
            return None

    # To find parts based on part_ID
    def find_part(self, part_ID):
        part_check = False
        for part in self.part_list:
            if part_ID[1:].isdigit() and part_ID[0] == 'P' and part.get_ID() == part_ID:
                part_check = True
                return part
            elif part.get_name() == part_ID:
                part_check = True
                return part
        if (part_check == False):
            return None

    # To find the larget ID for customer/ member/ premium member
    def largest(self, ID):
        ID_prefix = ID[0]
        ID_num = int(ID[1:])
        if (ID_prefix == 'P'):
            if (ID_num >= self.max_prem_id):
                self.max_prem_id = ID_num
        elif (ID_prefix == 'M'):
            if (ID_num >= self.max_mem_id):
                self.max_mem_id = ID_num
        else:
            if (ID_num >= self.max_mem_id):
                self.max_cust_id = ID_num

    # Function to create update customer/member/premium member value in string format to update the file
    def cust_update(self):
        update_list = []
        for customer in self.customer_list:
            if customer.get_ID()[0] == 'C':
                cust_string = customer.get_ID() + ',' + customer.get_name() + ',' + 'na' + ',' + 'na' + '\n'
                update_list.append(cust_string)
            elif customer.get_ID()[0] == 'M':
                cust_string = customer.get_ID() + ',' + customer.get_name() + ',' + customer.get_discount_rate() + ',' + 'na' + '\n'
                update_list.append(cust_string)
            elif customer.get_ID()[0] == 'P':
                cust_string = customer.get_ID() + ',' + customer.get_name() + ',' + customer.get_discount_rate() + ',' + customer.get_service_credit() + '\n'
                update_list.append(cust_string)
        return update_list

    # Function to create update service value in string format to update the file
    def service_update(self):
        update_list = []
        for service in self.service_list:
            if service.get_ID()[:2] == 'SP':
                service_string = service.get_ID() + ',' + service.get_name() + ',' + ','.join(
                    self.find_service(svc).get_name() for svc in service.get_service_list()) + '\n'
            else:
                service_string = service.get_ID() + ',' + service.get_name() + ',' + service.get_cost_per_hour() + ',' + service.get_require_user_input_hour() + ',' + service.get_service_hour() + ',' + service.get_require_part() + '\n'
            update_list.append(service_string)
        return update_list

    # Function to create update part value in string format to update the file
    def part_update(self):
        update_list = []
        for part in self.part_list:
            part_string = part.get_ID() + ',' + part.get_name() + ',' + part.get_price() + '\n'
            update_list.append(part_string)
        return update_list