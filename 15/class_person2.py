from class_person1 import Person

class Customer(Person):
    def __init__(self, company_id=None, company_name=None, first_name=None, last_name=None):
        super().__init__(first_name, last_name)
        self.company_id = company_id
        self.company_name = company_name

