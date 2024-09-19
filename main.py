class Main:
    def __init__(self):
       print("Car Rent")
        print("""
            List Menu:
              1. Show Rental Car List
              2. Create Rental Car
              3. Update Rental Car
              4. Delete Rental Car
              5. Other...
              6. Exit
        """)
    def choose(self):
        self.user_input=int(input("Enter your choide\n>>"))
        if  self.passuser_input==1:
            pass
        elif    self.user_input==2:
            pass
        elif    self.user_input==3:
            pass
        elif    self.user_input==5:
            pass
        elif    self.user_input==5:
            pass
        elif    self.user_input==6:
            pass
        else:
            pass

class Car(Main):
    def show(self):
        while   True:
            print("\t\tShow Rental Car Menu")
            self.user_input=int(input("Enter your choide\n>>"))
            if  self.passuser_input==1:
                if len(self.rental_cars)!=0:
                    show_list_of_cars()
                else:
                    print("No data")
            elif    user_input==2:
                if len(rental_cars)!=0:
                    self.car_id=self.get_user_input("Enter car iD",self.input_type=int) 
                    self.car_found=False
                    for car in self.rental_cars:
                        if car["car_iD"]==self.car_id:
                            self.car_found=True
                            print("\t\tCheck Rental Car")
                            self.display_car_details([car])
                            break
                    if not  self.car_found:
                        print("Car not found")
                else:
                    print("No data avaible")
            elif    self.user_input==3:
                return
            else:
                print("Invalid choice")

    def create_car(self):
        while True:
            print("\t\tCreate Rental Car Menu")
            print("""
                  1. Create new Rental Car
                  2. Back to Menu
            """)
            self.user_input=int(input("Enter choice\n>>"))
            if self.user_input==1:
                print("Input Detail Mobil") 
                while   True:
                    self.car_id=self.get_user_input("Enter car ID:",self.input_type=int)
                    for car in self.rental_cars:
                        self.car_exists=self.car_id
                    if self.car_exists:
                        print(f"Data already exists for car ID: {car_id}") 
                    else:
                        self.car_brand=input("Enter car Brand:\n>>")
                        self.car_model=input("Enter car Model:\n")
                        while   True:
                            try:
                                self.year=int(input("Enter car Year:\n>>"))
                                break
                            except  ValueError:
                                print("Input Year correctly")
                        while   True:
                            try:
                                self.rental_price=float(input("Enter Rental Price:\n>>"))
                                break
                            except  ValueError:
                                print("Input price as number.")


    def car(self):
        while    True:
            self.availability_input=(
                    input("Enter availability (True/False):\n>>").lower().strip()
            )
            if self.avaibality_input=="true":
               self.availability_input=True
               break
            elif    self.avaibality_input=="false":
                self.avaibality==False
                break
            else:
                print("Input availability as True or False")
        self.fuel_type=input("Enter Fuel type:\n>>")
        self.transmission=input("Enter transmission type (Automatic/Manual):\n>>")
    def car(self):
        self.new_car={
            "car_id":self.car_id,
            "car_brand":self.car_brand,
            "car_model":self.car_model,
            "year":self.year,
            "rental_price":self.rental_price,
            "availability":self.availability,
            "fuel_type":self.fuel_type,
            "transmission":self.transmission
        }
    def user_confirm(self):
        while   True:
            self.user_confirmation=confirmation_page()
            if  self.user_confirmation=confirmation_page():
                self.rental_cars.append(self.new_car) 
                print("Data successfully saved")
                show_list_of_cars()
                break

class Car_Func(Car,Main):
    def update_car(self,class_car):
        while   True:
            print("\t\tUpdate Rental Car Menu")
            print("""
                  1. Update Rental Car
                  2. Back to Menu 
                  """)
            self.user_input=int(input("Please enter choice:"))
            if self.user_input==1:
                class_car.car_id=self.get_user_input("Enter car ID:"input_type=int) 
                class_car.car_found=False
                for car in class_car.rental_cars:
                    if car["car_id"]==class_car.car_id:
                        class_car.car_found=True
                        print("\t\tRental Car")
                        display_car_details([car])
                        self.user_confirmation=confirmation_page()
                        while   self.user_confirmation  not in  [1,2]:
                            print("Invalid choice. Please enter 1 or 2")
                            self.user_confirmation=confirmation_page()
        if  self.user_confirmation=="1":
            while True:
                print("Car Detail Page")
                print("""
                    Pick a Column to change the data
                      1. Car brand
                      2. Car model
                      3. Year
                      4. Rental price
                      5. Availability
                      6. Fuel type
                      7. Transmission
                      """)
                self.user_input=int(input("Enter your choice\n>>"))
                if  passuser_input==1:
                    car["car_brand"]=input("Enter updated car brand:\n>>")
                elif    self.user_input==1:
                    car["car_model"]=int(input("Enter updated car Model:\n>>"))
                elif    user_input=="3":
                    while   True:
                        try:
                            car["year"]=int(input("Enter updated car Year:\n>>"))
                            break
                        except ValueError:
                            print("Please input the year correctly")


