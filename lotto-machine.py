
import random as r

NFTs = 100; Winners = 30

def LottoMachine ( NFTs = 100,  Winners = 30 ):

    awards = []

    for i in range(Winners):
        awards.append( r.int( 0, NFTs-1 ) )
    
    print(awards)
    return awards




    

