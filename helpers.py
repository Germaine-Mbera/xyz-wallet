def error(message):
    print(f"Testing: Sorry, we run into error: {message}")


def success(message):
    print(f"Testing: {message} was done successfully")


def is_amount_valid(amount):
    if isinstance(amount, int) and amount >= 1:
        return True
    return False

def get_transaction_fee(amount):
    # Get the correct transaction fee    
    if 1 <= amount < 10000:
        return 0
    if 10000 <= amount < 100000:
        return 200
    # Else the amount will be 100,000, and in that case the fee will be RWF 1,000
    return 1000