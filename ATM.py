balance=10000
print("WELCOME TO ATM")
card=input("insert your card: ")
if card=="ATM":
    print("your card is processing: ")
    language=input("enter the language: ")
    if language=="english" or language=="telugu":
        print("click ok")
        userpin=input("enter the pincode: ")
        if userpin=="3452":
            print("plase wait")
            account=input("enter your account type: ")
            if account=="current account" or account=="savings account":
                print("your account is processing: ")
                service=input("enter the service: ")
                if service=="withdraw" or service=="deposit":
                    print("your request is processing")
                    amount=int(input("enter the amount: "))
                    if amount<=1000:
                        print("wait a moment")
                        print("your request is processing")
                        print("DONE")
                        print("collect your cash")
                        request=input("enter your request")
                        if request=="reciept":
                            print("your balance is",balance-amount)
                            print("collect your cash")
                            print("THANKS")
                        else:
                            print("no balance")
                    else:
                        print("select valid amount")
                else:
                    print("select valid account")
            else:
                print("invalid pincode")
        else:
            print("select correct language")
    else:
        print("invalid card")        
else:
    print("nothing")                                                          
