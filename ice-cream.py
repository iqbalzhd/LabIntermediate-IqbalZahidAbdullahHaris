iceCream = open("./file-io/icecream.txt")
file = iceCream.readline()
salesData = {}
nama = []
toko_1 = []
toko_2 = []
toko_3 = []

# Membuat data dictionary
while file != "":
  hasilSplit = file.split(":")

  # Menambahkan data ke list untuk tiap toko
  nama.append(hasilSplit[0])
  toko_1.append(float(hasilSplit[1]))
  toko_2.append(float(hasilSplit[2]))
  toko_3.append(float(hasilSplit[3]))
  
  # buat dictionary
  salesData[hasilSplit[0]] = [float(hasilSplit[1]), float(hasilSplit[2]), float(hasilSplit[3])]
  file = iceCream.readline()

# Menampilkan header table
print("%-12s %10s %10s %10s %10s" % ('Nama', 'Toko 1', 'Toko 2', 'Toko 3', 'Total'))

# Menampilkan data
for i in salesData:
  print("%-12s %10.2f %10.2f %10.2f %10.2f" % (i, salesData[i][0], salesData[i][1],salesData[i][2], sum(salesData[i])))



# Menampilkan total harga tiap toko
print("%-12s %10.2f %10.2f %10.2f" % ('Total Toko', sum(toko_1), sum(toko_2), sum(toko_3)))

  



