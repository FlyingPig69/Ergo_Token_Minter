from ergpy import helper_functions, appkit

node_url: str = "http://127.0.0.1:9053"
ergo = appkit.ErgoAppKit(node_url=node_url)

wallet_mnemonic = ''

token_name = input('Enter Name:')
token_description = input('Enter Description:')
token_amount = int(input('Enter Amount: '))
token_decimals = int(input('Enter Decimals: '))

print(helper_functions.create_token(ergo=ergo, token_name=token_name, description=token_description, token_amount=token_amount, token_decimals=token_decimals, wallet_mnemonic=wallet_mnemonic))
