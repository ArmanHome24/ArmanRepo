class Emplyee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@arman.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Emplyee('Arman', 'Nas', 130000)
emp_2 = Emplyee('Farnia', 'Emami', 130000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_1.email)
print(emp_1.fullname())
print(emp_2.fullname())
