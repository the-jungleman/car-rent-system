from datetime import datetime, timedelta
import os

class Car:
    def __init__(self, plate, model, year, status="disponivel", day_price=0, km_total=0):
        self.plate = plate
        self.model = model
        self.year = year
        self.status = status
        self.day_price = day_price
        self.km_total = km_total

    def att_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Placa: {self.plate}, Modelo: {self.model}, Ano: {self.year}, Status: {self.status}, Preco por dia: {self.day_price}, Quilometragem Total: {self.km_total}"

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
        return f"Cliente: {self.name}, CPF: {self.cpf}, CNH: {self.cnh}, Histórico de Locacoes: {len(self.rent_history)} locacoes"

class Rent:
    def __init__(self, car, client, rent_date, devo_date, total_price=0, payment_status="pendente", devo_status="pendente", multas=0):
        self.car = car
        self.client = client
        self.rent_date = rent_date
        self.devo_date = devo_date
        self.total_price = total_price
        self.payment_status = payment_status
        self.devo_status = devo_status
        self.multas = 0  
        self.km_final = None

    def devo_car(self, km_final):
        self.km_final = km_final
        self.car.km_total += km_final  
        self.car.att_status("disponivel")
        self.devo_status = "devolvido"

    def calc_val_total(self):
        rent_days = (self.devo_date - self.rent_date).days
        if self.devo_date > datetime.now():  
            self.multas = 0
        else:
            overdue_days = (datetime.now() - self.devo_date).days
            self.multas = overdue_days * 50 
        self.total_price = (rent_days * self.car.day_price) + self.multas
        return self.total_price

    def __str__(self):
        return f"Aluguel do {self.car.model} para {self.client.name}, Data de Retirada: {self.rent_date}, Data de Devolucao: {self.devo_date}, Valor Total: {self.total_price}, Multa: {self.multas}"

class RentSystem:
    def __init__(self):
        self.cars = []
        self.clients = []
        self.rents = []
        self.history_output = []

    def clear(self):
        os.system("clear")
        if self.history_output:
            for msg in self.history_output:
                print(msg)
        self.history_output.clear()

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
        self.clear()
        print("Clientes cadastrados:")
        for client in self.clients:
            print(client)

    def show_rents(self):
        for rent in self.rents:
            print(rent)

    def find_car_by_plate(self, plate):
        for car in self.cars:
            if car.plate == plate:
                return car
        return None

    def find_client_by_cpf(self, cpf):
        for client in self.clients:
            if client.cpf == cpf:
                return client
        return None

    def list_available_cars(self):
        return [car for car in self.cars if car.status == "disponivel"]

    def list_rented_cars(self):
        return [car for car in self.cars if car.status == "alugado"]

    def cli_menu(self):
        while True:
            self.clear()
            print("\n=== Sistema de Aluguel de Veiculos ===")
            print("1. Cadastrar veiculo")
            print("2. Cadastrar cliente")
            print("3. Alugar veiculo")
            print("4. Devolver veiculo")
            print("5. Listar veiculos disponiveis")
            print("6. Listar clientes")
            print("7. Sair")
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                self.cli_register_car()
            elif opcao == "2":
                self.cli_register_client()
            elif opcao == "3":
                self.cli_rent_car()
            elif opcao == "4":
                self.cli_return_car()
            elif opcao == "5":
                self.show_available_cars()
                input("Pressione Enter para continuar...")
            elif opcao == "6":
                self.show_clients()
                input("Pressione Enter para continuar...")
            elif opcao == "7":
                self.clear()
                print("Saindo do sistema.")
                break
            else:
                self.history_output.append("Opcao invalida. Tente novamente.")

    def cli_register_car(self):
        self.clear()
        try:
            plate = input("Digite a placa do veiculo: ")
            model = input("Digite o modelo do veiculo: ")
            year = int(input("Digite o ano de fabricacao: "))
            day_price = float(input("Digite o preco da diaria: "))
            car = Car(plate, model, year, day_price=day_price)
            self.sign_car(car)
            self.history_output.append("Veiculo cadastrado com sucesso!")
        except ValueError:
            self.history_output.append("Erro ao cadastrar veiculo. Verifique as entradas.")

    def cli_register_client(self):
        self.clear()
        try:
            name = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            number = input("Digite o telefone do cliente: ")
            email = input("Digite o email do cliente: ")
            cnh = input("Digite o numero da CNH do cliente: ")
            client = Client(name, cpf, number, email, cnh)
            self.sign_client(client)
            self.history_output.append("Cliente cadastrado com sucesso!")
        except Exception as e:
            self.history_output.append(f"Erro ao cadastrar cliente: {str(e)}")

    def get_valid_date(self, prompt):
        while True:
            date_str = input(prompt)
            try:
                return datetime.strptime(date_str, "%d/%m/%Y")
            except ValueError:
                print(f"Data invalida! Por favor, insira a data no formato correto (dd/mm/yyyy).")

    def cli_rent_car(self):
        self.clear()
        cpf = input("Digite o CPF do cliente: ")
        client = self.find_client_by_cpf(cpf)
        if client:
            available_cars = self.list_available_cars()
            if available_cars:
                print("Veiculos disponiveis:")
                for i, car in enumerate(available_cars):
                    print(f"{i + 1}. {car}")
                try:
                    car_choice = int(input("Escolha o numero do veiculo: ")) - 1
                    if car_choice < 0 or car_choice >= len(available_cars):
                        raise IndexError("Escolha invalida.")
                    car = available_cars[car_choice]
                    rent_date = self.get_valid_date("Digite a data de retirada (dd/mm/yyyy): ")
                    devo_date = self.get_valid_date("Digite a data de devolucao (dd/mm/yyyy): ")
                    rent = Rent(car, client, rent_date, devo_date)
                    self.sign_rent(rent)
                    car.att_status("alugado")
                    client.add_history(rent)
                    self.history_output.append(f"Veiculo {car.model} alugado para {client.name} com sucesso!")
                except (ValueError, IndexError) as e:
                    self.history_output.append(f"Erro ao alugar veiculo: {str(e)}")
            else:
                self.history_output.append("Nao ha veiculos disponiveis.")
        else:
            self.history_output.append("Cliente nao encontrado.")

    def cli_return_car(self):
        self.clear()
        plate = input("Digite a placa do veiculo a ser devolvido: ")
        car = self.find_car_by_plate(plate)
        if car and car.status == "alugado":
            rent = None
            for r in self.rents:
                if r.car.plate == plate and r.devo_status == "pendente":
                    rent = r
                    break
            if rent:
                km_final = float(input("Digite a quilometragem final: "))
                rent.devo_car(km_final)
                rent.calc_val_total() 
                self.history_output.append(f"Veiculo {car.model} devolvido com sucesso! Valor total: {rent.total_price}, Multa: {rent.multas}")
            else:
                self.history_output.append("Aluguel nao encontrado.")
        else:
            self.history_output.append("Veiculo nao encontrado ou nao esta alugado.")

    def show_available_cars(self):
        self.clear()
        available_cars = self.list_available_cars()
        if available_cars:
            print("Veiculos disponiveis:")
            for car in available_cars:
                print(car)
        else:
            self.history_output.append("Nao ha veiculos disponiveis.")

if __name__ == "__main__":
    sistema = RentSystem()
    sistema.cli_menu()
