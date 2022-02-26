
# made by quantium-rock for the Solana community
# MIT license

# SOLUCKY TOKEN MASSIVE-AIRDROPS #

#### v.0.2. ####

import os
import subprocess
import csv

DBpath = './db/wallets.csv'

i = 0
ws = []
with open(DBpath, newline='') as DB:
    print('\ngo\n')
    db = csv.reader(DB)
    for w in db:
        w = ', '.join(w)
        if len(w) > 22:
            print(w)
            ws.append(w)
            i += 1
    print('\n> Your db contains more than',i,'solana addresses')

def sol( address = 0 ):
    out = ''
    err = ''
    try:
        if len(address) > 22:
            proc = subprocess.Popen(['solana','balance',address], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            print('\n> Wallet:',address)
        else:
            proc = subprocess.Popen(['solana','balance'], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
    except:
        print(err)
    out = str(out)
    #out = out.split("'")[1]
    #out = out.split(" ")[0]
    sol = out
    print('> SOL:',sol,' ◎')
    return sol

def balances(): 
    total_sol = 0
    for w in ws:
        total_sol = sol(w)
        #print(total_sol,' ◎')

def airdrops(): 
    for w in ws:
        if sol >= min_sol:
            n +=1
            total_sol += sol
            print(w)
            print("balance:", round(sol,2))
            if send:
                os.system("spl-token transfer --fund-recipient 9bML8p4vbo9LvVnT6ZDgfC2dYoiJyh3RKycnobE4KrEV "+str(token_amount)+" "+w+" --allow-unfunded-recipient")
                sol()
            print('\nTotal SOL: ', total_sol)
            print('\nTotal wallets: ', n)
            print('\n')

def q1(): return input('\n> Do you wanna check wallets balances? > y(yes) or exit -> ')
def q2(): return input('\n> Do you wanna make massive airdrops? y(yes) or exit -> ')
def q3(): return input('\nhow many SOLUCKY TOKENS each airdrop? ')
def q4(): return input('\nactivate min S◎L balance wallet? y(yes) or n(no) ')
def confirm(): return input('\nARE YOU F*** SURE? \nenter to go -> ')
def bye(): return input('\n< ALGO EXECUTED CORRECTLY >\n')

def ans( que ):
    q = que
    if( q == "y" or q == "Y" or q == "yes" or q == "YES" ):
        return True

sol()

if ans( q1() ):
    print('...')
    balances( )

if ans( q2() ):
    print('...')
    tokens = int(q2())
    airdrops()


send = True
min_sol = 0
token_amount = 10




""" 
#### v.0.1. ####

import os
import subprocess

send = True
min_sol = 0
token_amount = 10

n = 0
total_sol = 0

for w in whitelist:
    try:
        proc = subprocess.Popen(["solana", "balance", w], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
    except:
        print(err)
    out = str(out)
    out = out.split("'")[1]
    out = out.split(" ")[0]
    sol = round(float(out),2) 
    if sol >= min_sol:
        n +=1
        total_sol += sol
        print(w)
        print("balance:", round(sol,2))
        if send:
            os.system("spl-token transfer --fund-recipient 9bML8p4vbo9LvVnT6ZDgfC2dYoiJyh3RKycnobE4KrEV "+str(token_amount)+" "+w+" --allow-unfunded-recipient")



for w in whitelist:
    
    sol = os.system("\nsolana balance "+w)
    print("sol = "+str(sol))
"""