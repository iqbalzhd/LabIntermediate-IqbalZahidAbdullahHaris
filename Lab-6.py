# Name : Iqbal Zahid Abdullah Haris
# NIM : 23502310013

class Pecahan:

  def __init__(self, pembilang, penyebut):
    self.pembilang = pembilang
    self.penyebut = penyebut

  def __str__(self):
    return f"{self.pembilang}/{self.penyebut}"

  def desimal(self):
    return round(self.pembilang / self.penyebut, 2)


a = Pecahan(1, 3)
print('Pecahan',a.__str__())
print('Desimalnya',a.desimal())

