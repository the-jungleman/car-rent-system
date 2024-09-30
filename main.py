from datetime import    datetime

class Car:
    def car_info(self,plate,model,year,status,day_price):
        self.plate=plate,
        self.model=model,
        self.year=year,
        self.status="disponivel",
        self.day_price=day_price

    def att_status(self,new_status):
        self.status=novo_status


class Client():
    def client_info(self,name,cpf,number,email,cnh,rent_history):
        self.name=name
        self.cpf=cpf
        self.number=cpf
        self.email=email
        self.cnh=cnh
        self.rent_history=[]

    def client_register(self):
        name=str(input("Nome do cliente:\n>>"))
        cpf=input("CPF do cliente:\n>>")
        number=input("Numero de telefone do cliente:\n>>")
        cnh=input("CNH do cliente:\n>>")

    def add_history(self,rent):
        self.rent_history.append(rent)


class Rent(Car):
    def rent(self,rent_date,devo_date,km_init,total_price,payment_status,devo_status,multaas,km_final):
        self.rent_date=rent_date
        self.devo_date=devo_date
        self.km_init=km_init
        self.total_price=total_price
        self.payment_status=payment_status
        self.devo_status=devo_status
        self.multas=multas

    def devo_car(self,km_final,car_info):
        self.km_final=km_final
        self.car_info.atualizar_status("disponivel")

    def calc_val_total(self,car_info):
        rent_days=(self.devo_date_self-rent_date).days
        return  dias_aluguel*self.car_info.day_price

class RentSystem():
    def rent_system(self):
        self.cars=[]
        self.clients=[]
        self.rents=[]

    def sign_cars(self, car):
        self.cars.append(car)

    def sign_client(self,client):
        self.clients.append(client)

    def sign_rents(self,rents):
        pass
