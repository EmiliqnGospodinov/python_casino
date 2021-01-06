credits_balance = 1000

def show_wallet_balance():
    """Show wallet balance"""
    print(f'Balance is {credits_balance} $.')

def deposit_wallet(i):
    """Withdrawing from wallet"""
    global credits_balance
    credits_balance += i
    print(f'Balance is {credits_balance} $ after depositing.') 

def withdraw_wallet(i):
    """Withdrawing from wallet"""
    global credits_balance
    credits_balance -= i
    print(f'Balance is {credits_balance} $ after withdrawing.') 