from user import User

sam = User("Sam", "Mucyo", 7638238923893)
klein = User("Calvin", "Klein", 782379039)

if sam.balance == 1000 and klein.balance == 1000:
    print("✅Every new user starts with initial balance of RWF 1,000")
else:
    print("❌Every new user does not start with initial balance of RWF 1,000")

# Let's bump Sam's account so that we can test transactions
sam.receive(105000)
if sam.balance == 106000:
    print("✅Users can receive money")
else:
    print("❌Users cannot receive money")

# Testing sending 5,000 with no transaction fee
sam.send(klein, 5000)

if sam.balance == 101000:
    print("✅Users can send and receive money")
    print("✅Sending 5000 RWF has no transaction fee")
else:
    print("❌Users cannot send money: tested by sending 5,000RWF")

if klein.balance == 6000:
    print("✅Users can receive money")
else:
    print("❌Users cannot receive money")
    
# Testing sending 20,000 with a transaction fee of 200. Now, Sam has RWF 101,000
# After this transaction, he should be having RWF 80,800
sam.send(klein, 20000)

if sam.balance == 80800:
    print("✅Users can send and receive money")
    print("✅Sending RWF 10,000 - 100000 charges 200 RWF")
else:
    print("❌Users cannot send money or incorrect fee was charged")
    print("tested by sending 20,000RWF")

# Let's bump Klein's account so that we can test transactions of more than
# 100,000 RWF. He should be having 26,000 RWF for now. So he will be having
# 526,000 RWF after we bump up his account with 500,000 RWF
klein.receive(500000)

klein.send(sam, 200000)
if klein.balance == 325000:
    print("✅Users can send and receive money")
    print("✅Sending 100,000 - above charges 1000 RWF")
else:
    print("❌Users cannot send money or incorrect fee was charged")
    print("tested by sending 20,000RWF")