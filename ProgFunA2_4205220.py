#Name : vishnu Gopakumar
#ID: 4205220
#Level 3

from datetime import datetime #datetime imported for getting time stamp

#Class customer for each normal customer
class Customer:
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name #Made ID and name into private variables
    
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

#Class Member for each member which is child class with parent class as Customer
class Member(Customer):
    discount_rate = 0.1  # Static variable
    
    def __init__(self, ID, name, discount_rate = None):
        super().__init__(ID, name)
        if (discount_rate == None):
            self.__discount_rate = Member.discount_rate
        else:
            self.__discount_rate = discount_rate

    # Getter
    def get_discount_rate(self):
        return self.__discount_rate
    
    def get_discount(self,service_cost):
        discount = service_cost * float(self.__discount_rate)
        return discount
    
    # Setter
    def set_discount_rate(self, discount_rate):
        self.__discount_rate = discount_rate

    def display_info(self):
        print(f'{self.get_ID():<42}{self.get_name():<44}{self.__discount_rate:<44}na')

#Class Premium Member for each premium member which is child class of Mmeber class
class PremiumMember(Member):
    def __init__(self, ID, name, discount_rate, service_credit):
        super().__init__(ID, name, discount_rate)
        self.__service_credit = service_credit
    
    # Getter
    def get_service_credit(self):
        return self.__service_credit
    
    def get_credit(self,discount_price):
        credit = discount_price//100
        return credit
    
    # Setter
    def set_service_credit(self, service_credit):
        self.__service_credit = service_credit

    def update_credit (self,credit):
        self.__service_credit=int(float(self.__service_credit)+credit)
        self.__service_credit = str(self.__service_credit)
    
    def display_info(self):
        print(f'{self.get_ID():<42}{self.get_name():<44}{self.get_discount_rate():<44}{self.__service_credit}')

#Class for service Package
class ServicePackage:

    def __init__(self,ID,name,service_list,service_hour_list = None,part_list = None):
        self.ID = ID
        self.name = name
        self.service_list = service_list
        self.service_hour_list = service_hour_list
        self.part_list = part_list
        self.cost_per_hour_list = []
    
    #Getters
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
    
    #Setters
    def set_ID (self,ID):
        self.ID = ID
    
    def set_name (self,name):
        self.name = name
    
    def set_service_list (self,service_list):
        self.service_list = service_list
    
    def set_service_hour_list(self,service_hour_list):
        self.service_hour_list = service_hour_list
    
    def set_part_list(self,part_list):
        self.part_list = part_list
    
    def set_cost_per_hour_list(self,cost_per_hour_list):
        self.cost_per_hour_list = cost_per_hour_list
    
    def display_info(self):
        service_string = ''
        #logic to get list of servies in string format
        for service in self.service_list:
            if service_string == '':
                service_string = service_string + service
            else:
                service_string = service_string + ',' + service
        print(f'{self.ID:<17}{self.name:<34}{service_string}')


#Class Service for each service
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
    
    def compute_service_cost(self,service_hour):
        cost = self.__cost_per_hour * service_hour
        return cost

    def display_info(self):
        print(f'{self.__ID:<17}{self.__name:<19}{self.__cost_per_hour:<28}{self.__require_user_input_hour:<38}{self.__service_hour:<27}{self.__require_part}')

#Class Part for each part 
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
    

#Class Record to read and keep record of all details for customers,service and part
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
    
    #For reading customers/ Mmbers/ Premium Members form customers file
    def read_customers(self):
        try:
            customer_file = open('customers.txt')
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
                premium_member = PremiumMember(customer_details[0], customer_details[1], customer_details[2], customer_details[3])
                self.customer_list.append(premium_member)

    #For reading services from service file        
    def read_services(self):
        try :
            service_file = open('services.txt')
        except FileNotFoundError:
            return True
        for i in service_file:
            service_details = [detail.strip() for detail in i.split(',')]
            #Logic for adding service_apckage into the service list
            if(service_details[0][:2] == 'SP'):
                service_package_list=[]
                service_list =[]
                for i in range (len(service_details)):
                    if i>1:
                        service_list.append(service_details[i])
                    else :
                        service_package_list.append(service_details[i])
                service_package_list.append(service_list)
                service = ServicePackage(service_package_list[0],service_package_list[1],service_package_list[2])
            else:
                service = Service(service_details[0], service_details[1], service_details[2], service_details[3], service_details[4], service_details[5])
            self.service_list.append(service)
    
    #For reading parts from parts file
    def read_parts(self):
        try :
            parts_file = open('parts.txt')
        except FileNotFoundError:
            return True

        for i in parts_file:
            part_details = [detail.strip() for detail in i.split(',')]
            part = Part(part_details[0], part_details[1], part_details[2])
            if (int(part_details[0][1:])>self.max_part_id):
                self.max_part_id = int(part_details[0][1:])
            self.part_list.append(part)
    
    #For reading service_jobs
    def read_service_job(self):
        try :
            service_jobs_file = open('service_jobs.txt')
        except FileNotFoundError:
            return True
        for i in service_jobs_file:
            service_job_details =  [detail.strip() for detail in i.split(',')]
            customer = self.find_customer(service_job_details[0])
            service = self.find_service(service_job_details[1])
            part = None
            service_hour = ''
            service_hour_list =[]
            service_list = []
            part_list =[]
            if (service.get_ID()[:2] == 'SP'):
                i=2
                while i<=(len(service_job_details)-5):
                    if (self.find_service(service_job_details[i]) != None):
                        service_list.append(service_job_details[i])
                        service_hour_list.append(service_job_details[i+1])
                        i+=1
                    if (self.find_part(service_job_details[i]) != None):
                        part_list.append(service_job_details[i])
                    i+=1
                service.set_service_hour_list(service_hour_list)
                service.set_part_list(part_list)
                service.set_service_list(service_list)
            else :
                service_hour = service_job_details[2]
                if (service_job_details[3] != 'na'):
                    part = self.find_part(service_job_details[3])
                service.set_service_hour(service_hour)
            original_cost = service_job_details[len(service_job_details)-5]
            discount = service_job_details[len(service_job_details)-4]
            total_cost = service_job_details[len(service_job_details)-3]
            credits = service_job_details[len(service_job_details)-2]
            time_stamp = service_job_details[len(service_job_details)-1]
            service_job = ServiceJob(customer,service,False,None,part)
            service_job.set_original_cost(original_cost)
            service_job.set_discount(discount)
            service_job.set_total_cost(total_cost)
            service_job.set_credit(credits)
            service_job.set_time_stamp(time_stamp)
            self.service_job_list.append(service_job)
    
    #function to update services
    def update_service(self):
        update_string = input('Enter list of services and service hours to be updated in the format [service1,service_hour1,service2,na...] \n')
        temp_list = update_string.split(',')
        update_list = []
        for service in temp_list:
            update_list.append(service.strip())
        index =0
        for index in range(len(update_list)):
            #even index will be service name or ID and odd index will be na or service_hour
            if (index%2 == 0):
                for service in self.service_list:
                    if(service.get_name() == update_list[index] or service.get_ID() == update_list[index]):
                        if update_list[index+1] == 'na':
                            service.set_service_hour('na')
                            service.set_require_user_input_hour('yes')
                        else :
                            service.set_service_hour(update_list[index+1])
                        
            
    #function to update parts
    def update_parts(self):
        choice = input ("Please enter a for adding/updating part or r for removing part \n")
        #logic for adding/updating parts
        if(choice == 'a'):
            update_string = input('Enter list of parts and prices to be updated in the format [part_1,price_1...] \n')
            temp_list = update_string.split(',')
            update_list = []
            for service in temp_list:
                update_list.append(service.strip())
            length = len(update_list)
            #every even index will be part_name and the odd index will be 
            for i in range(0,length ):
                if (i%2 == 0):
                    for part in self.part_list:
                        if(part.get_name() == update_list[i] or part.get_ID() == update_list[i]):
                           part.set_price(update_list[i+1])
                        elif (self.find_part(update_list[i]) == None):
                            ID=''
                            if(self.max_part_id+1<10):
                                ID = 'P0' + str(self.max_part_id +1)
                            else:
                                ID = 'P' + str(self.max_part_id +1)
                            part_object = Part(ID,update_list[i],update_list[i+1])
                            self.part_list.append(part_object)
       
       #logic for deleting
        else:
            delete_string = input('Enter list of parts and prices to be updated in the format [part_1,part_2...] \n')
            delete_string = delete_string.strip()
            delete_list = delete_string.split(',')
            for item in delete_list:
                for part in self.part_list:
                    if part.get_name() == item or part.get_ID() == item:
                        self.part_list.pop(self.part_list.index(self.find_part(item)))
                    

    #For displaying list of exisitng customers
    def list_customer(self):
        print('Customers List: ')
        print(f"{'ID':<42}{'Name':<44}{'discount_rate':<44}{'service_credit'}")
        for customer in self.customer_list:
            customer.display_info()
        print('\n')

    #For displaying list of services
    def list_services(self):
        print('Services List:')
        service_package_check = True
        print(f"{'ID':<17}{'Name':<19}{'cost_per_hour':<28}{'require_user_input_hour':<38}{'service_hour':<27}{'require_part'}")
        for service in self.service_list:
            if service.get_ID()[:2] == 'SP' and service_package_check :
                print ("Service Packages:")
                print(f"{'ID':<17}{'Name':<34}{'Service_names'}")
                service_package_check = False
            service.display_info()
            service_package_check
        print('\n')
    
    #For displaying list of parts
    def list_parts(self):
        print('Parts List:')
        print(f"{'ID':<20}{'Name':<22}{'price'}")
        for part in self.part_list:
            part.display_info()
        print('\n')
    
    #For displaying service jobs
    def list_service_jobs(self):
        print ('Service Jobs list for service packages:')
        print(f'{"Customer":<15}{"Package":<8}{"S1 ID":<8}{"S1 Hrs":<8}{"S1 Part":<10}{"S2 ID":<8}{"S2 Hrs":<8}{"S2 Part":<10}{"S3 ID":<8}{"S3 Hrs":<8}{"S3 Part":<10}{"Orig $":<9}{"Disc":<7}{"Total":<9}{"Credits":<9}{"Timestamp"}')
        print('-' * 130)
        for service_job in self.service_job_list:
            if service_job.get_service().get_ID()[:2] == 'SP':
                service_job.disp_info(service_job.get_service().get_ID())
        print ('\n')
        print ('Service Job list for normal services :')
        print(f'{"Customer":<15}{"Service":<8}{"Hours":<7}{"Part":<10}{"Orig $":<9}{"Disc":<7}{"Total":<9}{"Credits":<9}{"Timestamp"}')
        print('-' * 80)
        for service_job in self.service_job_list:
            if service_job.get_service().get_ID()[:2] != 'SP':
                service_job.disp_info(service_job.get_service().get_ID())
        print('\n')

    
    #To find customer based on customer name 
    def find_customer(self,customer_name):
        customer_check = False
        for customer in self.customer_list:
            if customer_name[1:].isdigit() and customer_name[0] in ['C','M','P'] and customer.get_ID() == customer_name:
                customer_check = True
                return customer
            elif customer.get_name() == customer_name:
                customer_check = True
                return customer
        if (customer_check == False):
            return None
    
    #To find service based on service_ID
    def find_service(self,service_ID):
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
    
    #To find parts based on part_ID
    def find_part(self,part_ID):
        part_check = False
        for part in self.part_list:
            if   part_ID[1:].isdigit() and part_ID[0] == 'P' and part.get_ID() == part_ID :
                part_check = True
                return part
            elif part.get_name() == part_ID:
                part_check = True
                return part
        if (part_check == False):
            return None
    
    #To find the larget ID for customer/ member/ premium member
    def largest(self,ID):
        ID_prefix = ID[0]
        ID_num = int (ID[1:])
        if (ID_prefix == 'P'):
            if (ID_num >= self.max_prem_id):
                self.max_prem_id = ID_num
        elif (ID_prefix == 'M'):
            if (ID_num >= self.max_mem_id):
                self.max_mem_id = ID_num
        else:
            if (ID_num >= self.max_mem_id):
                self.max_cust_id = ID_num
    #Function to create update customer/member/premium member value in string format to update the file
    def cust_update(self):
        update_list = []
        for customer in self.customer_list:
            if (customer.get_ID()[0] == 'C'):
                cust_string= customer.get_ID() + ',' + customer.get_name() + ',' +'na' +',' + 'na'+'\n'
                update_list.append(cust_string)
            elif (customer.get_ID()[0] == 'M'):
                cust_string = customer.get_ID() + ',' + customer.get_name() + ',' + customer.get_discount_rate() + ',' + 'na'+'\n'
                update_list.append(cust_string)
            elif (customer.get_ID()[0] == 'P'):
                cust_string = customer.get_ID() + ',' + customer.get_name() + ',' + customer.get_discount_rate() + ',' + customer.get_service_credit() + '\n'
                update_list.append(cust_string)
        return update_list
    
     #Function to create update service value in string format to update the file
    def service_update(self):
        update_list = []
        for service in self.service_list:
            if service.get_ID()[:2]=='SP':
               service_string = service.get_ID() + ',' + service.get_name() + ',' + ','.join(self.find_service(svc).get_name() for svc in service.get_service_list()) + '\n'
            else:
                service_string = service.get_ID() + ',' + service.get_name() + ',' + service.get_cost_per_hour() + ',' + service.get_require_user_input_hour() + ',' + service.get_service_hour() + ',' + service.get_require_part() + '\n'
            update_list.append(service_string)
        return update_list
    
    #Function to create update part value in string format to update the file
    def part_update(self):
        update_list = []
        for part in self.part_list:
            part_string = part.get_ID() + ',' + part.get_name() + ',' + part.get_price() + '\n'
            update_list.append(part_string)
        return update_list
    
#Class for performing a service and printing the reciept       
class ServiceJob: 

    membership_fee = 50 #static variable as it should not be changed
    service_package_discount =0.25 #the discount percentage of service_package is kept at 75% and static as its value should not change

    def __init__(self,customer,service,cust_check,service_hour = None,part = None):
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
        
    
    #Getters 
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
    
    def get_total_cost (self):
        return self.__total_cost
    
    def get_credit(self):
        return self.__credit
    
    def get_time_stamp(self):
        return self.__time_stamp
    
    #Setters
    def set_customer(self,customer):
        self.__customer = customer
    
    def set_service(self,service):
        self.__service = service
    
    def set_part(self,part):
        self.__part = part
    
    def set_service_hour(self,service_hour):
        self.__service_hour = service_hour
    
    def set_cust_check(self,cust_check):
        self.__cust_check = cust_check
    
    def set_original_cost(self,original_cost):
        self.__original_cost = original_cost
    
    def set_discount(self,discount):
        self.__discount = discount
    
    def set_total_cost (self,total_cost):
        self.__total_cost = total_cost
    
    def set_credit(self,credit):
        self.__credit = credit
    
    def set_time_stamp(self,time_stamp):
        self.__time_stamp = time_stamp
    
    # function to check if customer is a member or premium member 
    def mem_check(self,customer): 
        customer_ID = customer.get_ID()
        if (customer_ID[0]== 'M'):
            return 'M'
        elif (customer_ID[0] == 'P'):
            return 'P'
        else:
            return 'C'
    
    #function that computes cost and gives service credit based on member or premium meber or parts required
    def compute_cost(self): 
        cost_per_hour = float(self.__service.get_cost_per_hour())
        total_cost = 0
        discount = 0
        service_fee = 0
        service_credit = 0

        #Logic for calculation based on part required or not
        if (self.__part == None):
            service_fee = cost_per_hour * float(self.__service_hour)
        else :
            service_fee = cost_per_hour * float(self.__service_hour) + float(self.__part.get_price())
        #Logic for calculation based on customer status i.e customer/ member/ premium member
        if self.__cust_check:
            total_cost = service_fee 
        elif (self.mem_check(self.__customer)== 'M'):
            discount = self.__customer.get_discount(service_fee)
            total_cost = service_fee - (discount)
        elif (self.mem_check(self.__customer)== 'P'):
            discount = self.__customer.get_discount(service_fee)
            total_cost = service_fee - (discount)
            service_credit = self.__customer.get_credit(total_cost)

            #Logic to remove credits from premium member in case the service is inspection and keeo the fee free of cost
            customer_credit = self.__customer.get_service_credit()
            if (int(customer_credit)>=5 and self.__service.get_ID()=='S01'):
                total_cost = 0
                discount = 0  
                service_credit = -5

            self.__customer.update_credit(service_credit)
            return [service_fee,discount,total_cost,service_credit]
        else:
            total_cost = service_fee
        return [service_fee,discount,total_cost]
    
    #function that computes cost and gives service credit based on member or premium meber or parts required for packages
    #In this function we are assuming that discount is only for the service package not the customer status i.e member or premium member
    def compute_package_cost(self): 
        service_hour_list = self.__service.get_service_hour_list()
        part_list = self.__service.get_part_list()
        cost_per_hour_list = self.__service.get_cost_per_hour_list()
        
        total_cost = 0
        discount = 0
        service_fee = 0
        service_credit = 0

        #calcualting service fee and discount after using service package
        for i in range (len(service_hour_list)):
            service_fee += float (cost_per_hour_list[i]) * float (service_hour_list[i]) 
        discount = service_fee * self.service_package_discount

        #calculating price after including the part_price
        for part in part_list:
            service_fee += float(part.get_price())
        total_cost = service_fee - discount
       
        #Logic for getting service_credit for premium member
        if (self.__cust_check == False and self.mem_check(self.__customer)== 'P'):
            service_credit = self.__customer.get_credit(total_cost)
            self.__customer.update_credit(service_credit)
            return [service_fee,discount,total_cost,service_credit]
        else:
            return [service_fee,discount,total_cost]
    
    #Function to display bill and to add membership for new customer
    def disp_bill(self,payment_list,customer_name='', package_choice = '', service_list = [],service_package_name='',part_list = []):
        record = Main.records
        premium_choice = ''
        if(self.__cust_check):
            choice = input("We see that you are a new customer would you like to take a membership please answer with [Y or N] \n")
            choice_check = True
            while(choice_check):
                if (choice == 'Y'):
                    print("Thank you for chosing to be a member with us we have two options Standard (FREE of cost) and Premium (50 AUD with store credits)")
                    premium_choice = input("Please chose : [P or M] according to your requirement \n")
                    if (premium_choice == 'M') :
                        record.max_mem_id += 1 #Logic to create new member_ID
                        member = Member ('M'+ str(record.max_mem_id),customer_name,'0.10')
                        record.customer_list.append(member)
                        print ("You have been succesfully registered as a standard member.")
                    elif (premium_choice == 'P'):
                        record.max_prem_id += 1 #Logic to create new Permium member ID
                        premium_member = PremiumMember('P'+ str(record.max_prem_id),customer_name,'0.10','0')
                        record.customer_list.append(premium_member)
                        print ("You have been succesfully registered as a premium member.Please note a membership fee of 50 AUD will be added to the bill")
                        payment_list[2] += ServiceJob.membership_fee
                        service_credit = premium_member.get_credit(payment_list[2])
                        premium_member.update_credit(service_credit)
                    choice_check = False
                elif (choice == 'N'):
                    print ("You will be registered as a regualr customer.")
                    record.max_cust_id += 1 #logic to create new customer_ID
                    customer = Customer('C'+ str(record.max_cust_id),customer_name)
                    record.customer_list.append(customer)
                    choice_check = False
                else:
                    print ("The input entered was not the expected input please try again")
                    choice = input("We see that you are a new customer would you like to take a membership please answer with [Y or N]")

        print('---------------------------------------------------------------------------')
        print('                                  Reciept                                  ')
        print('---------------------------------------------------------------------------')
        if package_choice == 'Y':
            print(service_package_name)
            for service in service_list:
                print(f'{service.get_name():11}:{float(service.get_service_hour()):56,.2f} X {service.get_cost_per_hour()}')
            for part in part_list:
                print(f'{part.get_name():11}:{float(part.get_price()):63,.2f}')
        else:
            print(f'{self.__service.get_name():11}:{float(self.__service.get_service_hour()):56,.2f} X {self.__service.get_cost_per_hour()}')
            if(self.__part != None):
                print(f'{self.__part.get_name():11}:{float(self.__part.get_price()):63,.2f}')
        print('---------------------------------------------------------------------------')
        print(f'Original cost:{payment_list[0]:56,.2f}(AUD)')
        print(f'discount:{payment_list[1]:61,.2f}(AUD)')
        if (premium_choice == 'P'):
            print(f'Membership fee:{ServiceJob.membership_fee:55,.2f}(AUD)')
        print(f'Total cost:{payment_list[2]:59,.2f}(AUD)')
        if (self.__cust_check != True):
            if (self.mem_check(self.__customer)== 'P'):
                print(f'Credit:{payment_list[3]:63,.2f}(AUD)')
        elif (premium_choice == 'P'):
            print(f'Credit:{0.0:63,.2f}(AUD)')
        print('\n')

    #To display all service jobs done
    def disp_info(self,service):
        record = Main.records
        if (record.find_service(service).get_ID()[:2] != 'SP'):
            print(f'{self.__customer.get_name():<15}{self.__service.get_ID():<8}{self.__service.get_service_hour():<7}',end="")
            if (self.__part != None):
                print(f'{self.__part.get_ID():<10}',end="")
            else :
               print(f"{'na':<10}",end="")
            print(f'{self.get_original_cost():<9}{self.get_discount():<7}{self.get_total_cost():<9}{self.get_credit():<9}{self.get_time_stamp()}')

        else :
            print(f'{self.__customer.get_name():<15}{self.__service.get_ID():<8}',end="")
            part_count = 0 
            service_count = 0
            for service_iterator in self.__service.get_service_list():
                print(f'{record.find_service(service_iterator).get_ID():<8}{record.find_service(service_iterator).get_service_hour():<8}',end ="")
                if (record.find_service(service_iterator).get_require_part() == 'yes'):
                    print(f'{record.find_service(service).get_part_list()[part_count]:<10}',end="")
                    part_count+=1
                else:
                    print(f'{'na':<10}',end="")
                service_count+=1
            for i in range(service_count,3):
                print(f'{'na':<8}{'na':<8}{'na':<8}',end ="")
            print(f'{self.get_original_cost():<9}{self.get_discount():<7}{self.get_total_cost():<9}{self.get_credit():<9}{self.get_time_stamp()}')

    
  
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
    
    #Function to check that customer name is correct format
    def getcust_name(self):
        customer_name = input('Enter name or ID of the customer [e.g. Tim] : \n')
        cust_validity = True
        while(cust_validity):
            if (customer_name[0] in ['C','P','M']):
                if (customer_name[1:].isdigit()):
                    cust_validity = False
                elif (customer_name.isalpha()):
                    cust_validity = False
            if (customer_name.isalpha()):
                cust_validity = False
            else:
                 print ("The name is not in correct format please try again \n")
                 customer_name = input('Enter name or ID of the customer [e.g. Tim] : \n')
        return customer_name
    
    #Function to check if service is valid
    def getservice_ID(self):
        self.__service_ID = input ('Enter the service ID or name \n')
        self.__service = Main.records.find_service(self.__service_ID)
        while (self.__service == None):
            print ("The entered service does not exist please enter a valid service")
            self.__service_ID = input ('Enter the service ID or name \n')
            self.__service = Main.records.find_service(self.__service_ID)

    #Function to get service_package and check if it exists
    def getservice_package(self):
        self.__service_package_ID = input('Enter service package ID or name \n')
        self.__service_package = Main.records.find_service(self.__service_package_ID)
        while (self.__service_package == None):
            print ("The entered service package does not exist please try again")
            self.__service_package_ID = input('Enter service package ID or name \n')
            self.__service_package = Main.records.find_service(self.__service_package_ID)

    
    #Function to check the validity of service hours
    def getservice_hours(self):
        try:
            self.__service_hour = float(input('Enter the hours of service required [enter valid hours e.g 2.5]: \n'))
        except:
            print ("Service hour is not a number. Please try again \n")
            return False
        if (self.__service_hour < 1 or self.__service_hour%0.5 != 0):
            print("Service is less than 1 or not in increments of 0.5 please try again \n")
            return False
        else:
            return True
    
    #Function to check validity of part entered by the user
    def getpart_ID(self):
        self.__part_ID = input('Enter the part ID or name \n')
        self.__part = Main.records.find_part(self.__part_ID)
        while (self.__part == None):
            print ("The entered part does not exist please enter correct part_ID")
            self.__part_ID = input('Enter the part ID or name \n')
            self.__part = Main.records.find_part(self.__part_ID)
   
    #Function to check if customer is new or exists
    def customer_check(self):
        if self.__customer == None:
            return True
        else :
            return False
    
    #Function to check if part is required for the service entered
    def part_required_check (self,service): 
        if service.get_require_part() == 'yes':
            return True
        else :
            return False
    
     #Function to check if service hours needs to be inputted by user   
    def service_hour_check (self,service): 
        if service.get_require_user_input_hour() == 'yes' :
            return True
        else :
            return False
    
    #Function to get all inputs required by the user to perform a service
    def get_details(self):
        self.__customer_name = self.getcust_name()
        self.__customer = Main.records.find_customer(self.__customer_name)
        self.__cust_check = self.customer_check() # Variable to check if customer is present in the datbase or not it is true when customer is new
        choice = input("Would you like to use a service package instead of a service. Please answer [ Y or N ] \n")
        package_check = True #Boolean value to make sure user enters correct input for package choice
        while package_check:
            if (choice == 'Y'):
                self.getservice_package()
                service_list = self.__service_package.get_service_list()
                #For loop to filter each service and get service hour or part
                parts_list = []
                service_hour_list = []
                cost_per_hour_list = []
                for service_name in service_list:
                    self.__service = Main.records.find_service(service_name)
                    if (self.part_required_check(self.__service)): #Program will ask for part only if the service requires it
                        self.getpart_ID()
                        parts_list.append(self.__part)
                    if (self.service_hour_check(self.__service)):
                        service_hour_valid = self.getservice_hours()
                        while( service_hour_valid == False): #While loop in case user inputs inoccrect format for service hours
                            service_hour_valid = self.getservice_hours()
                        self.__service.set_service_hour(self.__service_hour)
                    else :
                        self.__service_hour = self.__service.get_service_hour()
                    self.__service_list.append(self.__service)
                    service_hour_list.append(self.__service_hour)
                    cost_per_hour_list.append(self.__service.get_cost_per_hour())
                self.__service_package.set_cost_per_hour_list(cost_per_hour_list) #To keep a list of cost_per_hour for each service
                self.__service_package.set_service_hour_list(service_hour_list) #Added service hours to the list of service hours
                self.__service_package.set_part_list(parts_list)  #Added parts to the parts list in service job
                package_check = False
            elif choice == 'N':
                self.getservice_ID()
                if (self.part_required_check(self.__service)): #Program will ask for part only if the service requires it
                    self.getpart_ID()
                if (self.service_hour_check(self.__service)):
                    service_hour_valid = self.getservice_hours()
                    while( service_hour_valid == False): #While loop in case user inputs inoccrect format for service hours
                        service_hour_valid = self.getservice_hours()
                    self.__service.set_service_hour(self.__service_hour)
                else :
                    self.__service_hour = self.__service.get_service_hour()
                package_check = False
            else :
                print("Choice entered was not in correct format please try again")
                choice = input("Would you like to use a service package instead of a service. Please answer [ Y or N ]")
        return choice
        
        
    
    #Logic to update users after menu driven program is completed
    def update_cust_file(self,file_list):
        customer_file = open('customers.txt','w')
        for customer in file_list: 
            customer_file.writelines(customer)
   
    #Logic to update services after menu driven program in completed
    def update_service_file(self,file_list):
        service_file = open('services.txt','w')
        for service in file_list: 
            service_file.writelines(service)
    
    #Logic to update parts after menu driven program in completed
    def update_part_file(self,file_list):
        parts_file = open('parts.txt','w')
        for parts in file_list: 
            parts_file.writelines(parts)

    def menu_logic(self):
        cust_file_check = Main.records.read_customers()
        service_file_check =  Main.records.read_services()
        part_file_check = Main.records.read_parts()
        service_job_file_check = Main.records.read_service_job()
        if (not(cust_file_check and service_file_check and part_file_check and service_job_file_check)):
            cust_file_check = False
            service_file_check =  False
            part_file_check = False
            self.disp_menu()
            while (self.option != 8):
                if self.option == 1:
                    choice = self.get_details()
                    if (choice == 'Y'):
                        service_job = ServiceJob(self.__customer, self.__service_package, self.__cust_check, self.__service_hour, self.__part)
                        payment_list = service_job.compute_package_cost()
                        service_job.disp_bill(payment_list,self.__customer_name,choice,self.__service_list,self.__service_package.get_name(), self.__service_package.get_part_list())
                        self.__service_package.set_part_list([]) #Necessary step so that in the next run parts of the previous run are not included
                        self.__service_package.set_service_hour_list([])#Necessary step so that in the next run service_hours of the previous run are not included
                        time_stamp = datetime.now()
                        formatted_time = time_stamp.strftime("%d/%m/%Y %H:%M:%S") #formatting time_Stamp to required format
                        service_job.set_time_stamp(formatted_time) #setting time stamp for particular service job
                        self.__part = None
                        self.__service_list = []
                    else:
                        service_job = ServiceJob(self.__customer, self.__service, self.__cust_check, self.__service_hour, self.__part)
                        payment_list = service_job.compute_cost()
                        service_job.disp_bill(payment_list,self.__customer_name)
                        time_stamp = datetime.now()
                        formatted_time = time_stamp.strftime("%d/%m/%Y %H:%M:%S") #formatting time_Stamp to required format
                        service_job.set_time_stamp(formatted_time) #setting time stamp for particular service job
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
        else :
            print ("One of the files does not exist please add the files to the current directory and please try again")

menu = Main()
menu.menu_logic()

#References 
#[1] W3schools.com (no date) Python - List Comprehension. Available at: https://www.w3schools.com/python/python_lists_comprehension.asp (Accessed: 13 May 2026).

#Problems faced 
#1. Am unable to provide the lgic for updating service job file after termination of the program
#2. First time members do not get discounts only existent members get 10% discount