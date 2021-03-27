from tabulate import tabulate

def findNextGoodKlaster(currentKlaster, klasters):
    for i in range(currentKlaster,len(klasters)):
        if klasters[currentKlaster+1]=='bad':
            currentKlaster+=1
        else:
            return currentKlaster+1

files = {"A": 2, "B": 7, "C": 12, 'D': 11}
klasters = ['', '', 3, 4, 5, 'eof', 'eof', 16, 'eof', 8, 'bad', 13, 13, 20, "", 'bad', 9, "", "", "", 6, '', '', '', 25,
            26, 'eof', '']
normalizedFiles = {}

for i in files:
    normalizedFiles[i] = []
    normalizedFiles[i].append(files[i])
    currentClaster = files[i]
    while 1:
        if type(currentClaster) == int:
            if klasters[currentClaster]!="eof":
                normalizedFiles[i].append(klasters[currentClaster])
            currentClaster = klasters[currentClaster]
        else:
            break
badKlasters=[]
normalKlasters=[]
for i in range(2,len(klasters)):
    if klasters[i]!='bad':
        normalKlasters.append(i)
    if klasters[i]=='bad':
        badKlasters.append(i)
goodClasters=['' for i in range(len(klasters))]
for i in badKlasters:
    goodClasters[i]='bad'
fileSizes= {}
for i in normalizedFiles:
    fileSizes[i]=len(normalizedFiles[i])

currentClaster=2
for i in fileSizes:
    if currentClaster==len(goodClasters):
        break
    j=0
    while j<fileSizes[i]:
        if goodClasters[currentClaster] != 'bad': # если текущий кластер не бэд
            if j==fileSizes[i]-1:
                goodClasters[currentClaster] = 'eof' # если это последнй кластер файла
                currentClaster += 1
            else:
                goodClasters[currentClaster]=findNextGoodKlaster(currentClaster,goodClasters)
                currentClaster=findNextGoodKlaster(currentClaster,goodClasters)
            j+=1
        else:
            currentClaster+=1

normalFiles = {}
currentClaster=2
for i in normalizedFiles:
    normalFiles[i]=[]
    while 1:
        if goodClasters[currentClaster]!='eof':
            if goodClasters[currentClaster]!="bad":
                normalFiles[i].append(currentClaster)
            currentClaster += 1
        else:
            normalFiles[i].append(currentClaster)
            currentClaster+=1
            break

indexes = list(range(len(goodClasters)))

print("Начальные данные:")
print(files)
print(normalizedFiles)
print(tabulate([indexes,klasters]))

print("Переработанные данные")
print(normalFiles)
print()
print(tabulate([indexes,goodClasters]))



