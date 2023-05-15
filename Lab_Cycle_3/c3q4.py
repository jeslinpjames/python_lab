import pickle
from fpdf import FPDF
class Vehicle:
    def __init__(self, engine_number, model, vehicle_type, mileage, vendor, reg_number, owner_name):
        self.engine_number = engine_number
        self.model = model
        self.vehicle_type = vehicle_type
        self.mileage = mileage
        self.vendor = vendor
        self.reg_number = reg_number
        self.owner_name = owner_name    

class Vehicle_Collection:
    def __init__(self):
        self.vehicles = []
    
    def display(self):
        for v in self.vehicles:
            print(f"Engine Number: {v.engine_number}, Model: {v.model}, Type: {v.vehicle_type}, Mileage: {v.mileage}, Vendor: {v.vendor}, Registration Number: {v.reg_number}, Owner Name: {v.owner_name}")

    
    def sort_by_mileage(self):
        self.vehicles.sort(key=lambda v : v.mileage)


    def add_vehicle(self):
        Eng_no=int(input("Enter the Engine Number : "))
        Model = input("Enter the Model : ")
        Ve_Type = input("Enter the type of the Vehicle : ")
        Mile = float(input("Enter the Milage of the Vehicle : "))
        Ven = input("Enter the vendor name : ")
        Reg_no = input("Enter the Registrarion Number of the Vechile : ")
        Own_name = input("Enter the Vehicle Owner Name : ")
        v1 = Vehicle(Eng_no,Model,Ve_Type,Mile,Ven,Reg_no,Own_name)
        self.vehicles.append(v1)
    
    
    def delete_vehicles(self,reg_num):
        new_vehicles = []
        for v in self.vehicles:
            if v.reg_number == reg_num:
                continue
            new_vehicles.append(v)
        self.vehicles = new_vehicles


    def modify_vehicles(self):
        reg_number = input("Enter the Registration number to modify the details : ")
        self.delete_vehicles(reg_number)
        print("Enter details to be modified : ")
        self.add_vehicle()
    

    def save(self):
        filename = input("Enter the filename to save : ")
        with open(filename,"wb") as f:
            pickle.dump(self.vehicles,f)


    def load(self):
        filename = input("Enter the filename to open : ")
        with open (filename, "rb") as f:
            self.vehicles = pickle.load(f)


    def filter_by_attribute(self):
        attribute = input("Enter attribute to filter data : ")
        value = input("Enter value of attribute to filter by : ")
        filtered = [v for v in self.vehicles if getattr(v, attribute) == value]
        for v in filtered:
            v.display()
            print(f"Engine Number: {v.engine_number}, Model: {v.model}, Type: {v.vehicle_type}, Mileage: {v.mileage}, Vendor: {v.vendor}, Registration Number: {v.reg_number}, Owner Name: {v.owner_name}")


    def report(self, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, ln=1, align="C", txt="No.\tEngNo.\tModel\tType\tMileage\tVendor\tRegNo.\tOwner\n")

        for i, entry in enumerate(self.vehicles, start=1):
            pdf.cell(200, 10, ln=1, align="C", txt=f"{i}\t{entry.engine_number}\t{entry.model}\t{entry.vehicle_type}\t{entry.mileage}\t{entry.vendor}\t{entry.reg_number}\t{entry.owner_name}\n")

        pdf.output(filename)

def main():
    choice = 1
    V = Vehicle_Collection()
    while(choice == 1):
        choice_2=0
        print("Enter 1 to Display\nEnter 2 to sort Vehicles by mileage\nEnter 3 to add a new vehicle\nEnter 4 to delete a Vehicles")
        print("Enter 5 to modify vehicles\nEnter 6 to save the file\nEnter 7 to Load a file\nEnter 8 to filter the vehicles by attributes ")
        print("Enter 9 to add it to PDF\nEnter 10 to Exit")
        choice_2=int(input("Enter your choice : "))
        print("---------------------------------------")
        if(choice_2==1):
            V.display()
        elif(choice_2==2):
            V.sort_by_mileage()
        elif(choice_2==3):
            V.add_vehicle()
        elif(choice_2==4):
            reg_num =input("Enter the registration number to delete the vehicle from the list : ")
            V.delete_vehicles(reg_num)
        elif(choice_2==5):
            V.modify_vehicles()
        elif(choice_2==6):
            V.save()
        elif(choice_2==7):
            V.load()
        elif(choice_2==8):
            V.filter_by_attribute()
        elif(choice_2==9):
            V.report('report.pdf')
        elif(choice_2==10):
            break
        else :
            print("Wrong Choice!")
        print("---------------------------------------")
        print("Enter 1 to continue\nEnter 2 or any other number to Exit.")
        choice=int(input("Enter your choice : "))
        print("---------------------------------------")

    print("Thank You!")




main()



    