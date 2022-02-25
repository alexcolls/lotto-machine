
# made by quantium-rock for the Solana community
# MIT license

import os
import json
import shutil
from PIL import Image

net = "devnet" # mainnet-beta or devnet

# metadata
name = "SOLUCKY"
symbol = "LUCKCAT"
edition = "GENESIS"
generation = 0
description = "SOLucky NFTicket ◎ The Solana onchain-lotto every f*** Friday! A Solana community-based project built-in the Solana blockchain. Visit our website to claim your LuckyCat reward. We wish you best of luck!"
date ="March 4th 2022"
catpot = "12.50 S◎L"
website = "https://soluckylotto.com"
discord = "https://discord.gg/AA4sJBEX"
twitter = "https://twitter.com/SOLuckyLotto"

LUCKYCATS = [ 'GOLDEN CAT', 'BLACK CAT', 'WHITE CAT' ]
RARITY = [ 10, 30, 60 ]
PROBABILITY = [ 50, 0, 25 ]

PIXELS = 777

TOTALCOLLECTION = 10

LAST_NFTICKET = 10

def LuckyCat():

    src = 'assets/'
    try:
        shutil.rmtree(src)
        shutil.rmtree('.cache')
        os.mkdir(src)
    except OSError:
        os.mkdir(src)
    else:
        print ("Preparing collection... %s " % src)
    
    nft = LAST_NFTICKET
    for j in range(0,len(LUCKYCATS)):
        luckycat = LUCKYCATS[j]
        rarity = RARITY[j]
        image = Image.open('art/'+luckycat+'.png')
        new_image = image.resize((PIXELS, PIXELS))
        new_image.save('art/'+luckycat+'.png')
        n = int( (rarity/100)* TOTALCOLLECTION )
        for i in range(1,n+1):
            nft += 1
            print(nft)
            metadata = {
                "name": name+" #"+str(nft),
                "symbol": symbol,
                "description": description,
                "external_url": website,
                "edition": nft,
                "image": str(nft-1-LAST_NFTICKET)+".png",
                "website": website,
                "discord": discord,
                "twitter": twitter,
                "attributes": [
                    {
                    "trait_type": "NFTICKET",
                    "value": nft
                    },
                    {
                    "trait_type": "LUCKYCAT",
                    "value": luckycat
                    },
                    {
                    "trait_type": "RARITY",
                    "value": str(rarity)+"%"
                    },
                    {
                    "trait_type": "PRIZE DATE",
                    "value": date
                    },
                    {
                    "trait_type": "TOTAL CATPOT",
                    "value": catpot
                    },
                    {
                    "trait_type": "EDITION",
                    "value": edition
                    },
                    {
                    "trait_type": "GENERATION",
                    "value": generation
                    },
                    {
                    "trait_type": "SUPPLY",
                    "value": TOTALCOLLECTION
                    }
                ],
                "properties": {
                    "files": {
                    "uri": str(nft-1-LAST_NFTICKET)+".png",
                    "type": "image/png"
                    },
                    "category": "image",
                    "creators": [
                    {
                        "address": "4vL2Fg5rb5DmXdJd2LpWvZxhJz3W6ZeKyzx4rtLypagw",
                        "share": 100
                        
                    }
                    ]
                },
                "seller_fee_basis_points": 3000
            }
            print(nft, luckycat, i)
            print(metadata)
            json_string = json.dumps(metadata)
            print(image.size)
            
            dst = str(nft-1-LAST_NFTICKET)+'.json'
            with open(src+dst, 'w') as outfile:
                outfile.write(json_string)
            
            art = './art/'+luckycat+'.png'
            png = str(nft-1-LAST_NFTICKET)+'.png'
            shutil.copyfile(art, src+png)
    
    print('\n')
    cmnd = input('do you want to upload your assets to arweave? press y (yes) + enter to continue... > ')
    if( cmnd == 'y' or cmnd == 'yes' ):
        print('\nUploading files to arweave...')
        print('\n')
        
        os.system("ts-node ./lib/metaplex/js/packages/cli/src/candy-machine-v2-cli.ts upload -e "+net+" -k ./key/solucky.json -cp ./config.json -c cache ./assets")
        
        print('\ndone! check for errors..')
        input("\nenter to leave program >")

    else:
        print('\n')
        print('we are done here!')

LuckyCat()