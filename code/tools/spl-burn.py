
# made by quantium-rock for the Solana community
# MIT license

# solana cli command -> solana transfer --from <KEYPAIR> <RECIPIENT_ACCOUNT_ADDRESS> <AMOUNT> --fee-payer <KEYPAIR>

import os
import subprocess

key = "./key/solucky.json"
print("\nBURN SOLUCKY COIN:")

def check_balance():
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

sol = check_balance()
x = input("\nHow many SOLUCKY COIN do you wanna burn? ")

confirm = input("\nARE YOU F*** SURE?\n\nPRESS ENTER TO MAKE TRANSFER -> ")
os.system("spl-token burn 53Ck2VYgiCyj25uXFqD7KzCHokZFFp5gUHaXmY8pHUk7 "+x)

final = check_balance()
print("\nNetwork fee:")
print(str(round(sol-final,11)))

input("\nEXIT -> ")
print('\n\n')
