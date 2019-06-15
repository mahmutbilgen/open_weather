import datetime

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
        self.pay = int (self.pay * Employee.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

my_date = datetime.date(2019, 6, 14)
print(Employee.is_workday(my_date))


emp_1 = Employee('Mahoni','Kemble' , 50000 )
emp_2 = Employee ('Test','User' ,60000)




# new_emp_1 =  Employee.from_string(emp_str_1)


# print (new_emp_1.email)
# print (new_emp_1.pay)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'


# first, last, pay = emp _str_1.split('-')
# print(Employee.num_of_emps)
# Employee.set_raise_amt(1.05)
#
#
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)



# print(emp_1.fullname(),emp_1.pay)
#
# emp_1.apply_raise()
# emp_1.apply_raise()
#
# print(emp_1.fullname(),emp_1.num_of_emps)




# emp_1.raise_amt = 1.05
#
#
# print('emp_1 name space',emp_1.__dict__)
#
# print('Employee Raise Amount: ', Employee.raise_amt)
# print('Emp_1 Raise Amount: ', emp_1.raise_amt)
# print('Emp_2 Raise Amount: ', emp_2.raise_amt)
#




# print(emp_1.pay)
# print(emp_1.pay)

#
# print ( emp_1.fullname())
# print ( Employee.fullname(emp_2))




