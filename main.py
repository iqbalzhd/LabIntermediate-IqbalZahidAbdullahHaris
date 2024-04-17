iceCream = open("./file-io/icecream.txt")
file = iceCream.readline()
salesData = {}
nama = []
toko_1 = []
toko_2 = []
toko_3 = []


while file != "":
  hasilSplit = file.split(":")
  # print(hasilSplit)
  nama.append(hasilSplit[0])
  toko_1.append(hasilSplit[1])
  toko_2.append(hasilSplit[2])
  toko_3.append(hasilSplit[3])
  
  # buat dictionary untuk tiap rasa
  
  salesData[hasilSplit[0]] = [float(hasilSplit[1]), float(hasilSplit[2]), float(hasilSplit[2])]
  file = iceCream.readline()

  print

  



