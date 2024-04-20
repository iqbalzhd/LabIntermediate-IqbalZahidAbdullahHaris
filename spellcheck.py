storyAlice = open("./file-io/alice.txt", 'r')
words = open("./file-io/words.txt", 'r')
uniqueWords = []

def readfile(file):
  fileJadi = file.read()
  hasilSplit = fileJadi.split("~!@#$%^&*()_+{}|:")
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
  return listTypo
      


# print('Jumlah kata dalam alice.txt: ', wordCount(storyAlice))
# print('Jumlah kata unik dalam alice.txt: ', uniqueWord(storyAlice))
print(len(spellcheck(words, storyAlice)))
