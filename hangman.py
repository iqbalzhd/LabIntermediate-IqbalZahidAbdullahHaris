urutan = 6
listTebak = []
kata = 'Software'
kata = kata.lower()

while urutan > 0:

  tebak = input('Tebak huruf :')
  tebak = tebak.lower()


  if tebak in listTebak:
    print('huruf', tebak, 'sudah ditebak')

  elif tebak in kata:

    print('huruf', tebak, 'ada pada kata')

  else:
    urutan -= 1
    print('huruf', tebak, 'tidak ada pada kata')

  listTebak.append(tebak)

  kosong = ''
  for i in kata:
    if i in listTebak:
      kosong += i
    else:
      kosong += '_'

  print(kosong)

  print('Kamu masih ada', urutan, 'kali lagi')
  if kosong == kata and urutan > 0:
    print('Selamat, kamu menang')
    break
  elif urutan <= 0:
    print('Kamu kalah karena kehabisan waktu, kata yang benar adalah',
          kata.upper())
    break
