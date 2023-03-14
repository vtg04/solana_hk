

def do_payment_in_crypto(crypto_wallet_address,amount):
            '''
            This function does payment in crypto using a given crypto wallet address and an amount.

            Parameters:
            crypto_wallet_address (str): the address of the crypto wallet
            amount (float): the amount to be paid

            Returns:
            str: a message describing the success/failure of the payment
            '''

            # Check if amount is a valid number
            if type(amount) != float:
                return 'Invalid amount - not a valid number'

            # Check if amount is larger than 0
            if amount <= 0:
                return 'Invalid amount - must be larger than 0'

            # Check if wallet address looks valid
            if len(crypto_wallet_address) != 34 or not crypto_wallet_address.startswith('0x'):
                return 'Invalid wallet address'

            # All conditions checked - do payment
            payment_success = True  # Pseudo-code for payment functionality

            if payment_success:
                return 'Payment successful - ' + str(amount) + ' sent to ' + crypto_wallet_address
            else:
                return 'Payment failed'


