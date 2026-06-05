class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} - {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company1 = Company("Lockheed Martin")
company2 = Company("Chum Bucket")

company1.add_employee("Joe", "Pilot")
company1.add_employee("Harry", "Security Operations Officer")
company1.add_employee("Jazy", "Ground Staff")

company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")

print(company1.company_name)
for employee in company1.list_employees():
    print(employee)

print()

print(company2.company_name)
for employee in company2.list_employees():
    print(employee)
