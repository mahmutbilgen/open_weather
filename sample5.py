##
##  It is demostrate Class usage and subclass usage
##
class Employee:
    raise_amt  = 1.04

    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt  = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)           #  Setting params in subclass - option 1
        #Employee.__init__(self, first, last, pay)    #  Setting params in subclass - option 2
        self.prog_lang  = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employeees=None):
        super().__init__(first, last, pay)           #  Setting params in subclass - option 1
        if employeees is None:
            self.employees = []
        else:
            self.employees = employeees

    def add_emp(self, emp):
         if emp not in self.employees:
             self.employees.append(emp)

    def remove_emp(self, emp):
         if emp in self.employees:
             self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Develo per ('Mahoni','Kemble' , 50000, 'Python' )
dev_2 = Developer ('Test','User' ,60000, 'Java' )

mgr_1 = Manager('Sue', 'Smith', 90000,[dev_1])

print(isinstance(mgr_1, Developer))


# print(mgr_1.email)
# mgr_1.remove_emp(dev_1)
# mgr_1.add_emp(dev_2)
#
# mgr_1.print_emps()


# print (dev_1.email)
# print (dev_1.prog_lang)

## Below code shows all Classes and sub classes structure.

# print (dev_1.email)
# print (dev_2.email)
#
# print(help(Developer))
