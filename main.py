blocks = {"A": 2, "B": 7, "C": 12, 'D': 11}
klasters = ['', '', 3, 4, 5, 'eof', 'eof', 16, 'eof', 8, 'bad', 13, 13, 20, "", 'bad', 9, "", "", "", 6, '', '', '', 25,
            26, 'eof', '']
normalizedBlocks = {}

for i in blocks:
    normalizedBlocks[i] = []
    normalizedBlocks[i].append(blocks[i])
    currentClaster = blocks[i]
    while 1:
        if type(currentClaster) == int:
            if klasters[currentClaster]!="eof":
                normalizedBlocks[i].append(klasters[currentClaster])
            currentClaster = klasters[currentClaster]
        else:
            break
print(normalizedBlocks)
