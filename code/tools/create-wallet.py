# made by quantium-rock for the Solana community
# MIT license

import os

name = input("\n> Insert wallet name... ")

if name != 0:
    os.system("solana-keygen new -o tools/token/keys/"+name+'.json')
    rewrite = input("\n> Do you want to rewrite the wallet? enter y(yes) to proceed: ")
    if rewrite == 'y' or main == 'Y':
        input("\n> ARE YOU F*** SURE? YOU WILL LOSE ACCESS TO THIS WALLET! press enter if you don't care -> ")
    os.system("solana-keygen new -o tools/token/keys/"+name+'.json --force')
    print('\nDONE')
    main = input("\n> Do you want to set '+name+'.json as main Solana wallet? press y(yes) or enter for no: ")
    if main == 'y' or main == 'Y':
        os.system("solana config set -k tools/token/keys/"+name+'.json')