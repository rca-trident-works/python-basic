from class_person3 import Person

class Customer(Person):
    def __init__(self, company_id=None, company_name=None, first_name=None, last_name=None):
        super().__init__(first_name, last_name)
        self.company_id = company_id
        self.company_name = company_name

    def show(self):
        # return f"{super().show()}\n\tid:{self.company_id} 会社名:{self.company_name}"
        print(f"氏名: {self.full_name}\n\tid:{self.company_id} 会社名:{self.company_name}")
