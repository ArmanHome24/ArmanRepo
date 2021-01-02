class Emplyee:

    num_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@arman.com'

        Emplyee.num_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Emplyee('Arman', 'Nas', 130000)
emp_2 = Emplyee('Farnia', 'Emami', 130000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_1.email)
print(emp_1.fullname())
print(emp_2.fullname())
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.__dict__)

print(Emplyee.num_emps)
print(emp_1.num_emps)
