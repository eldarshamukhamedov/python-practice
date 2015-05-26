class Employee:
    # static variables
    numberEmployed = 0
    employees = []

    # constructor
    def __init__(self, name, salary):
        # instance
        self.name = name
        self.salary = salary

        Employee.numberEmployed += 1
        Employee.employees.append(self)

    @staticmethod
    def getNumberEmployed():
        print 'There are {0} employees working at the company.'.format(
            Employee.numberEmployed
        )

    @staticmethod
    def listAllEmployees():
        for employee in Employee.employees:
            employee.printEmployeeInformation()

    def printEmployeeInformation(self):
        print '{0} makes {1}'.format(self.name, self.salary)


bob = Employee('Bob', 100000)
jay = Employee('Jay', 115000)

print bob.printEmployeeInformation()

Employee.getNumberEmployed()
Employee.listAllEmployees()
