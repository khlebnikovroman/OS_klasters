blocks={"A":2,"B":7,"C":12}

klasters=['','',3,4,5,'eof','eof',16,'eof',8,'bad','',13,20,"",'bad',9,"","","",6]
def getNextKlaster(i):
    try:
        print(klasters[i], end=' ')
        if type(klasters[i])==int:
            getNextKlaster(klasters[i])
        else:
            print("\n")
    except:
        pass
for i in blocks:
    print(str(i) +": " +str(blocks[i])+ " ",end="")
    getNextKlaster(blocks[i])