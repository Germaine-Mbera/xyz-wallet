from helpers import error, success, is_amount_valid, get_transaction_fee

class User:
    def __init__(self, f_name, l_name, contact):
        # Trim any leading white spaces
        f_name, l_name = f_name.strip(), l_name.strip()
        
        # Ensure username is not blank
        if not f_name or not l_name:
            return error("First name and Last name are required")

        # Ensure username is not blank
        if not contact:
            return error("Please input your phone number") 
        
        # Ensure contact has number type
        if not isinstance(contact, int) :
            return error("Check contact format: No parenthesis or dashes")
        
        self.first_name = f_name
        self.last_name = l_name
        self.contact = contact
        self.balance = 1000

        return
    

    def receive(self, amount):
        if is_amount_valid(amount):
            self.balance += amount
        return


    def send(self, receiver, amount):
        # If amount is not valid, we will do nothing. Just return
        if not is_amount_valid(amount):
            return error(f"Amount RWF {amount} is not valid")

        # Like wise if the user is not valid, we should not do anything
        if not isinstance(receiver, User):
            return error("The user does not exist.")

        fee = get_transaction_fee(amount) 
           
        if self.balance <= amount + fee:
            print(f"Insufficient balance of RWF {self.balance} to perform"
                    "this transaction")
            return

        # Now if all of the above conditions passes well, we are good to send
        self.balance -= amount + fee
        receiver.receive(amount)

        return success(f"Sending RWF {amount} to {receiver.last_name} "
                      f"{receiver.first_name} with a fee of RWF {fee} ")