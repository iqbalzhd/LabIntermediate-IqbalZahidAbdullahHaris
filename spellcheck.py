storyAlice = "./file-io/alice.txt"
words = "./file-io/words.txt"
uniqueWords = []

def readfile(file):
  file = open(file, 'r')
  fileJadi = file.read()
  hasilSplit = fileJadi.split()
  file.close()
  return hasilSplit

def wordCount(file):
  hasilSplit = readfile(file)
  jumlahKata = len(hasilSplit)
  return jumlahKata

def uniqueWord(file):
  hasilSplit = readfile(file)
  jadiSet = set(hasilSplit)
  jumlahUnique = len(jadiSet)
  return jumlahUnique

def spellcheck(pembanding, target):
  pembandingJadi = readfile(pembanding)
  targetJadi = readfile(target)
  listTypo = []
  for i in range(len(targetJadi)):
    if targetJadi[i] not in pembandingJadi:
      listTypo.append(targetJadi[i])
  jumlahTypo = len(listTypo)
  return jumlahTypo
      


print('Jumlah kata dalam alice.txt: ', wordCount(storyAlice))
print('Jumlah kata unik dalam alice.txt: ', uniqueWord(storyAlice))
print("Jumlah kesalahan penulisan/typo pada cerita alice adalah sebanyak : ", spellcheck(words, storyAlice), " kata")
