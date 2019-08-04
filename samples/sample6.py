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

    def __repr__(self):
        return " Employee ( {} ,  {} , {} ) ".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} ==== {}'.format(self.fullname(),self.email)

    def __len__(self):
        return len(self.fullname())



emp_1 = Employee ('Mahoni','Kemble', 50000 )
emp_2 = Employee ('Test','User',60000)


print("Employee Name lenght : {}".format(emp_1.__len__()))
print(emp_1.__repr__())