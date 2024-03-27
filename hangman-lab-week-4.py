#################################
# Hangman template for Lab 3 #
# March 27, 2022 #
# Author: Iqbal Zahid Abdullah Haris #
# NIM 23502310013 #
#################################

import random
import sys

urutan = 6
listTebak = []
word_list = ['g']
kata_ditebak = []
benar = 0
salah = 0


def random_word(word_list, kata_ditebak):

  a = random.randint(0, len(word_list) - 1)
  b = word_list[a]
  # print(b)
  word_list.remove(b)
  # print(word_list)
  kata_ditebak.append(b)
  return b


def stop():
  while True:
    break


def reset_list():
  listTebak.clear()
  return listTebak


def opening():
  print('Welcome to Hangman')
  print('Created by The Most Handsome Boy in the World')
  print('Dezertz x Woeztjin')
  print('-' * 50)
  opsi()


def habis_kata(kata_ditebak):
    print('Selamat kamu sudah menebak semua kata yang ada')
    print(f'Kata yang sudah ditebak: {kata_ditebak}')
    print('Sampai jumpa lagi di Hangman Dezertz 2.0')
    sys.exit()

def benar_kata(benar):
  benar+=1
  print(f'Kamu sudah menebak {benar} kata')

def salah_kata(salah):
  salah+=1
  print(f'Kamu sudah menebak {salah} kata')


def mainLagi():

  while True:
    if len(word_list) > 0:
      reset_list()
      print('Kata yang sudah ditebak: ', listTebak)
    else:
      habis_kata(kata_ditebak)



def opsi():
  reset_list()
  while True:
    print('1. Play')
    print('2. Exit')
    pilih = input('Choose: ')
    if pilih == '1':
      print('Let\'s play')
      main()
    elif pilih == '2':
      print('Thank you for playing')
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
  kata = random_word(word_list, kata_ditebak)
  print('Guess the word')
  print('You have 6 lives')
  print('_' * len(kata))
  print('Panjang kata adalah ', len(kata), 'huruf')
  global urutan
  while urutan > 0:

    # Variabel untuk menebak
    tebak = input('Tebak huruf :')
    tebak = tebak.lower()

    # Pengurangan nyawa untuk tebakan salah
    if tebak not in kata:
      urutan -= 1

    # Memanggil fungsu updateText
    updateText(kata, listTebak, tebak)

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
    print(' ' * 50)
    # Info mengenai nyawa

    if kosong == kata and urutan > 0:
      print('Selamat, kamu menang')
      benar_kata(benar)
      mainLagi()
      break

    elif urutan <= 0:
      print('Kamu kalah karena kehabisan waktu, kata yang benar adalah',
            kata.upper())
      salah_kata(salah)
      mainLagi()
      break

    else:
      print('Kamu masih ada', urutan, 'nyawa lagi')
      continue


opening()
