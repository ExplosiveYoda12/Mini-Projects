class Database:
  def __init__(self, country, capital, language, borders):
    self.country = country
    self.capital = capital
    self.language = language
    self.borders = borders

  def Information(self):
    return 'Country: {}, Capital: {}, Language: {}, Borders: {}'.format(self.country, self.capital, self.language, self.borders)

  @classmethod
  def from_string(cls, emp_str):
    country, capital, language, borders = emp_str.split('-') #spliting at the hyphon
    return cls(country, capital, language, borders) #returning values into class

class Borders(Database):
  def __init__(self, borders=None):
    super().__init__(borders)
    if borders is None:
      self.borders = []
    else:
      self.borders = borders

  def add_border(self, border):
    if border not in self.borders:
      self.borders.append(border)

  def remove_border(self, border):
    if border in self.employees:
      self.borders.remove(border)

  def print_border(self):
    for border in self.borders:
      print('-->', border)

spain_str_1 = 'Spain-Madrid-Spanish-France, Andorra, UK, Portugal, Morocco'
Spain = Database.from_string(spain_str_1)

'''
print(Spain.language)
print(Database.Information(Spain))'''

Database.Information(Spain)
