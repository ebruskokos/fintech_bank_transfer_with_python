def withdraw():
    receiver_account = "87654321"
    sender_account = "12345678"
    pin = "1234"
    account_balance = 300

    entered_receiver_account = input("Enter the receiver's account number: ")
    entered_sender_account = input("Enter the sender's account number: ")
    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    entered_pin = input("Enter the PIN: ")

    if entered_pin == pin:
        if entered_sender_account == sender_account:
            if account_balance >= withdrawal_amount:
                print("Withdrawal successful.")
                account_balance -= withdrawal_amount
            else:
                print("Insufficient balance.")
        else:
            print("Sender's account number is incorrect.")
    else:
        print("Incorrect PIN.")

    print("Current account balance:", account_balance)


withdraw()
