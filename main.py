from datetime import datetime

class Car:
    def __init__(self, plate, model, year, status="disponivel", day_price=0):
        self.plate = plate
        self.model = model
        self.year = year
        self.status = status
        self.day_price = day_price

    def att_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Placa: {self.plate}, Modelo: {self.model}, Ano: {self.year}, Status: {self.status}, Preço por dia: {self.day_price}"


class Client:
    def __init__(self, name, cpf, number, email, cnh):
        self.name = name
        self.cpf = cpf
        self.number = number
        self.email = email
        self.cnh = cnh
        self.rent_history = []

    def add_history(self, rent):
        self.rent_history.append(rent)

    def __str__(self):
        return f"Cliente: {self.name}, CPF: {self.cpf}, CNH: {self.cnh}, Histórico de Locações: {len(self.rent_history)} locações"


class Rent:
    def __init__(self, car, client, rent_date, devo_date, km_init, total_price=0, payment_status="pendente", devo_status="pendente", multas=0):
        self.car = car
        self.client = client
        self.rent_date = rent_date
        self.devo_date = devo_date
        self.km_init = km_init
        self.total_price = total_price
        self.payment_status = payment_status
        self.devo_status = devo_status
        self.multas = multas
        self.km_final = None

    def devo_car(self, km_final):
        self.km_final = km_final
        self.car.att_status("disponivel")
        self.devo_status = "devolvido"

    def calc_val_total(self):
        rent_days = (self.devo_date - self.rent_date).days
        self.total_price = rent_days * self.car.day_price + self.multas
        return self.total_price

    def __str__(self):
        return f"Aluguel do {self.car.model} para {self.client.name}, Data de Retirada: {self.rent_date}, Data de Devolução: {self.devo_date}, Valor Total: {self.total_price}"


class RentSystem:
    def __init__(self):
        self.cars = []
        self.clients = []
        self.rents = []

    def sign_car(self, car):
        self.cars.append(car)

    def sign_client(self, client):
        self.clients.append(client)

    def sign_rent(self, rent):
        self.rents.append(rent)

    def show_cars(self):
        for car in self.cars:
            print(car)

    def show_clients(self):
        for client in self.clients:
            print(client)

    def show_rents(self):
        for rent in self.rents:
            print(rent)
