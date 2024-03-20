#################################
# Hangman template for Lab 3 #
# March 22, 2022 #
# Author: Iqbal Zahid Abdullah Haris #
# NIM 23502310013 #
#################################

urutan = 6
listTebak=[]
kata = 'gagak'
kata = kata.lower()

def opening():
  print('Welcome to Hangman')
  opsi()

def opsi():
  while True:
    print('1. Play')
    print('2. Exit')
    pilih = int(input('Choose: '))
    if pilih == 1:
      print('Let\'s play')
      main()
    elif pilih == 2:
      break
    else:
      print('Input tidak valid')
    continue
  
def updateText(kata, listTebak, tebak):
  if tebak in listTebak:
    print('huruf', tebak, 'sudah ditebak')

  elif tebak in kata:
    print('huruf', tebak, 'ada pada kata')

  else:
    print('huruf', tebak, 'tidak ada pada kata')
  
def main():
  print('Guess the word')
  print('You have 6 lives')
  print('_'*len(kata))
  print('Panjang kata adalah ', len(kata), 'huruf')
  global urutan
  while urutan > 0:
  # Variabel untuk menebak
    tebak = input('Tebak huruf :')
    tebak = tebak.lower()

  # Pengurangan nyawa untuk tebakan salah
    if tebak not in listTebak:
      urutan -= 1
      

  # Menambahkan tebakan kedalam tebakan
    listTebak.append(tebak)

  # List untuk menyimpan tebakan
    kosong = ''
    for i in kata:
      if i in listTebak:
        kosong += i
      else:
        kosong += '_'
    print(kosong)

  # Memanggil fungsu updateText
    updateText(kata, listTebak, tebak)
    
  # Info mengenai nyawa
    print('Kamu masih ada', urutan, 'kali lagi')
    if kosong == kata and urutan > 0:
      print('Selamat, kamu menang')
      break
    elif urutan <= 0:
      print('Kamu kalah karena kehabisan waktu, kata yang benar adalah',
            kata.upper())
      break


opening()