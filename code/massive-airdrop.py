
# made by quantium-rock for the Solana community
# MIT license

# SOLUCKY TOKEN MASSIVE-AIRDROPS #

#### v.0.2. ####

import os
import subprocess
import csv

wallets = ''; ws = []
with open('./db/wallets.csv', newline='') as csvfile:
    wallets = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in wallets:
        ws = ws.append(row)
        print(', '.join(row))

def sol():
    try:
        proc = subprocess.Popen(["solana", "balance"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
    except:
        print(err)
    out = str(out)
    out = out.split("'")[1]
    out = out.split(" ")[0]
    sol = round(float(out),6)
    print("\nYour balance:")
    print(sol)
    return sol

def balances(): 
    for w in ws:
        try:
            proc = subprocess.Popen(["solana", "balance", w], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
        except:
            print(err)
        out = str(out)
        out = out.split("'")[1]
        out = out.split(" ")[0]
        sol = round(float(out),2) 

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

def q1(): return input('\ndo you wanna check balance? > y(yes) or ENTER -> ')
def q2(): return input('\ndo you wanna make massive airdrops? y(yes) or ENTER -> ')
def q3(): return input('\nhow many SOLUCKY TOKENS each airdrop? ')
def q4(): return input('\nactivate min S◎L balance wallet? ')
def confirm(): input('\nARE YOU F*** SURE? \nLFGO -> ')
def bye(): return input('\n< ALGO EXECUTED CORRECTLY >\n')

def ans( que ):
    q = que
    if( q == "y" or q == "Y" or q == "yes" or q == "YES" ):
        return True
        
balances()
q2 = q2()


send = True
min_sol = 0
token_amount = 10
n = 0
total_sol = 0



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