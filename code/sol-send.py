
# made by quantium-rock for the Solana community
# MIT license

import os

key = "./key/solucky.json"

# command -> solana transfer --from <KEYPAIR> <RECIPIENT_ACCOUNT_ADDRESS> <AMOUNT> --fee-payer <KEYPAIR>

print('\n')
balance = os.system("solana balance")
sol = input("\nHow many SOL do you wanna send? ")
w = input("\nPaste address and press enter to transfer -> ")
confirm = input("\nARE YOU F*** SURE? PRESS ENTER TO MAKE TRANSFER -> ")
os.system("solana transfer --from "+key+" "+w+" "+sol+" "+"--fee-payer "+key+" --allow-unfunded-recipient")
input("\nEXIT -> ")
