
import os

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