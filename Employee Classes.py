import datetime

class Employee: #parent class
  num_of_emps = 0
  raise_amount = 1.04 #Class Variable

  def __init__(self,fname,lname,pay): #Runs for each employee, self taken by defalt
     self.fname = fname
     self.lname = lname
     self.pay = pay
     self.email = fname + "." + lname + '@company.com'
     Employee.num_of_emps += 1

  def fullname(self):
    return '{} {}'.format(self.fname, self.lname)

  def apply_raise(self):
    self.pay = int(self.pay * Employee.raise_amount)

  @classmethod
  def set_raise_amount(cls, amount): #changes class Variable raise_amount, cls taken by defalt
    cls.raise_amount = amount

  @classmethod
  def from_string(cls, emp_str):
    fname, lname, pay = emp_str.split('-') #spliting at the hyphon
    return cls(fname, lname, pay) #returning values into class

  @staticmethod #Used if class is not referenced, nothing taken by defalt
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False 
    return True

class Developer(Employee): #inheriting code, subclass
  raise_amount = 1.10 #uses this amt instead as this is first ref in order for Developer

  def __init__(self,fname,lname,pay, programming_lang): #Runs for each employee, self taken by defalt
    super().__init__(fname, lname, pay) #OR Employee.__init__(self, fname, lname , pay) #runs code from Employee Class and adds below
    self.programming_lang = programming_lang

  @classmethod
  def from_string(cls, dev_str):
    fname, lname, pay, programming_lang = dev_str.split('-') #spliting at the hyphon
    return cls(fname, lname, pay, programming_lang) #returning values into class

class Manager(Employee):
  def __init__(self,fname,lname,pay, employees=None):
    super().__init__(fname, lname, pay)
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

# Employee.set_raise_amount(1.06)
emp_1 = Employee('Bob', 'Anderson', 50000)
emp_2 = Employee('Test','User', 30000)

dev_str_1 = 'Raymond-Holt-70000-Python'
dev_1 = Developer.from_string(dev_str_1)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(dev_1.email)
# print(dev_1.programming_lang)

'''
my_date = datetime.date(2020, 8, 5) 
print(Employee.is_workday(my_date))'''

print(mgr_1.email)
mgr_1.add_emp(emp_2)
mgr_1.print_emps()
print(emp_1.fullname)
print(Employee.fullname(emp_1))
Manager.print_emps(mgr_1)
