# Python Object_Oriented Programing:
class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    """now the raise amount can be accessed from the class itself by: print(Employee.raise_amount)"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
        """pay attention here, since every time that we pass an employee information 'init' runs, we need to place 
        the code inside the init. and also make sure not to use 'SELF' if the variable needs to be general """

    """print('{} {}'.format(emp_1,first, emp_1.last) can print you the full name of Employee, but we have to write it 
    every single time. instead we write a method to create this action for us: every method in a class get an 
    instance as SELF! so don't forget it. """

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    """the problem with this method is that the amount of raise is not defined or no one can access to it, 
    also it's hard coded here and if anyone wants to change it, they have to go through the code and manually change 
    it. let's upscale it to the class level """

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    """using self.raise_amount here helps us to be able to override the raise amount with such a code: 
    emp_1.raise_amount = 1.05. if we have used Employee.raise_amount, it would be impossible to update an employee's 
    raise amount manually """

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    """ new_emp_1 = Employee.from_string(emp_str_1)
        print(new_emp_1.__dict__)"""

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    """This is an example of Static method. static methods don't get any arguments from a class directly
    Import datetime
       my_date = datetime.date(2016, 7, 10)
       print(Employee.is_workday(my_date))"""


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        # Employee.__init__(self, first, last, pay): also works. super is more maintainable, but when it comes to
        # multi-inheritance it's better to use the class name.

    """print(dev_1.pay)
       dev_1.apply_raise()
       print(dev_1.prog_lang)"""


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    """mgr_1.print_emps()
       mgr_1.add_emp(dev_2)
       mgr_1.print_emps()
       mgr_1.remove_emp(dev_1)
       mgr_1.print_emps()"""


emp_1 = Employee('Martin', 'Shirazi', 50000)
emp_2 = Employee('Sahba', 'Esfandabadi', 60000)

emp_str_1 = 'John-doe-70000'
emp_str_2 = 'Steve-Smith-90000'
emp_str_3 = 'Jane-Doe-30000'

dev_1 = Developer('Corey', 'Schafer', 75000, 'Python')
dev_2 = Developer('Breanna', 'Coley', 80000, 'Java')

mgr_1 = Manager('sue', 'Smith', 90000, [dev_1])

# two built-in function of Python:

print(isinstance(mgr_1, Manager))  # True
print(isinstance(mgr_1, Employee))  # True
print(isinstance(mgr_1, Developer))  # False

print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer))  # False
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
"""when we run it with the class itself, the instance has to be passed to it as an argument. pay attention to these 
two: """

# print(Employee.fullname(emp_1))
# print(emp_1.fullname())

"""Using __dict__ is a very helpful command to show the values for an instance. raise amount also is not shown under 
emp_1 but Employee. it's because raise_amount is a class level argument not method """

# print(emp_1.__dict__)
# print(Employee.__dict__)
#
# Employee.set_raise_amt(1.05)
"""it's same as Employee.raise_amount = 1.05"""
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
"""for these three print statements, if we say: Employee.raise_amount = 1.05, it changes the amount for everyone. but 
if we use emp_1.raise_amount = 1.05, it only updates emp_1 raise amount. """
# print(Employee.num_of_emps)
