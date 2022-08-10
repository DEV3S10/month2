class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):
    def __init__(self, company_name, company_bank, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.salary <= self.company_bank:
            self.company_bank -= self.salary
            print("salary was get!")
        else:
            print("У компании не достаточно средств!")

    def info(self):
        print(f"{self.first_name} {self.last_name} {self.salary}")


Oomat = Person("Keyboard", 1000, "Oomat", "K", 500)

Oomat.get_salary()
Oomat.get_salary()
Oomat.get_salary()
Oomat.info()

