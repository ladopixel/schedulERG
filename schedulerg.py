"""
schedulERG
============

Create a token in the Ergo blockchain by encrypting the description with a password.

AUTHOR
    @ladopixel 

CREATED AT
    Friday 10 June 2022 08:00
"""

from platform import node
from ergpy import helper_functions, appkit 
import colorsPython
import cryptocode
import getpass
import requests

node_url: str = 'http://159.65.11.55:9053/'
ergo = appkit.ErgoAppKit(node_url=node_url)

wallet_mnemonic = ''
password = ''

# Convert the description UTF-8 to String
def to_utf8_string(hex):
    valor_utf8 = '' 
    aux = ''
    contador = 0
    for i in hex:
        contador = contador + 1
        if contador < 3:
            aux = aux + i
        if contador == 2:
            valor_utf8 = valor_utf8 + str(chr(int(aux, 16)))
            contador = 0
            aux = ''
    return valor_utf8

# add_info() → Mint token ciphed
def add_info():
    input_name = input(colorsPython.escribirVerdeOpacidad('Enter contact name: '))
    input_phone = input(colorsPython.escribirVerdeOpacidad('Enter description (will be encrypted): '))
    
    global password
    password = getpass.getpass(prompt=colorsPython.escribirVerdeOpacidad('Enter password: '))
    print(colorsPython.escribirVerde('Password ok!'))
    cipher_phone = cryptocode.encrypt(input_phone, password)
    print(colorsPython.escribirVerde('Ciphered correctly!'))

    print(' ')
    global wallet_mnemonic
    wallet_mnemonic = getpass.getpass(prompt=colorsPython.escribirVerdeOpacidad('Enter seed phrase: '))
    print(colorsPython.escribirVerde('Seed phrase ok!'))

    try:
        # purple color
        print('\033[1;35m')
        print(helper_functions.create_token(ergo=ergo, token_name=input_name, description=cipher_phone, token_amount=1, token_decimals=0, wallet_mnemonic=wallet_mnemonic))
        # end purple color
        print(colorsPython.escribirVerde('Minted correctly!'))
        print(' ')
        print(colorsPython.escribirVerde('Contact added correctly ') + colorsPython.escribirVerdeOpacidad(' → Name: ' + str(input_name) + ' → Description ciphered: ' + str(cipher_phone)))
    except:
        print(colorsPython.escribirRojo('ERROR minting!'))

# contact_info() → Read y deciphed description token
def contact_info():
    input_wallet_mail = input(colorsPython.escribirVerdeOpacidad('Enter your wallet to see your contacts: '))
    if requests.get('https://api.ergoplatform.com/api/v1/addresses/' + input_wallet_mail + '/balance/confirmed').status_code == 200:
        data_wallet = requests.get('https://api.ergoplatform.com/api/v1/addresses/' + input_wallet_mail + '/balance/confirmed')
        data_wallet = data_wallet.json()
        total_tokens = str(len(data_wallet['tokens']))
        id_tokens = []
        print('')
        print(colorsPython.escribirAmarillo('You have ' + str(total_tokens) + ' contacts'))

        for i, token in enumerate(data_wallet['tokens']):
            print(colorsPython.escribirVerde(str(i)) + ' → ' + colorsPython.escribirVerdeOpacidad(str(token['name'])))

        print('')
        token_deciph = int(input(colorsPython.escribirVerde('Select contact number to decipher: ')))
        
        id_token_deciph = data_wallet['tokens'][token_deciph]['tokenId']
        data_token = requests.get('https://api.ergoplatform.com/api/v0/assets/' + id_token_deciph + '/issuingBox')
        data_token = data_token.json()
        name_token = str(data_token[0]['assets'][0]['name'])
        description_token = to_utf8_string(data_token[0]['additionalRegisters']['R5'])[2:]
        
        print('')
        print(colorsPython.escribirVerdeOpacidad('This is you description → ') + colorsPython.escribirVerde(description_token))
        # password = input(colorsPython.escribirVerde('Enter the key to deciph: → '))
        password = getpass.getpass(prompt=colorsPython.escribirAmarillo('Enter the key to deciph: → '))
        
        if cryptocode.decrypt(description_token, password):
            str_decoded = cryptocode.decrypt(description_token, password)
            print('')
            print(colorsPython.escribirMorado('Decrypted ↓'))
            print(colorsPython.escribirVerde(str(name_token) + ' - ' + str(str_decoded)))
        else:
            print('')
            print(colorsPython.escribirRojo('Decrypted ↓'))
            print(colorsPython.escribirRojoOpacidad('Error, not is posible!'))
    else:
        print('')
        print(colorsPython.escribirRojo('Wallet incorrect!'))

# Menu
def menu(opcion):
    if opcion == 1:
        add_info()
    elif opcion == 2:
        contact_info()
    elif opcion == 0:
        exit()

while True:
    print('')
    print('┌───────────────────────┐')
    print('│ 1 - Add contact       │')
    print('│ 2 - Info contact      │')
    print('│ 0 - Exit              │')
    print('└───────────────────────┘')
    opcion = int(input('Select option: '))
    print('')
    menu(opcion)
