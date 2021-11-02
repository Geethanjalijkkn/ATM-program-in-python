#29/10/21
#Geethanjali
#Bank Account creating,credit and debit amount

#def deposit_final(dep_amt):
 #   balance += dep_amnt
 
    
def start():
    print("Welcome to State Bank Services")

    while True:
        print("\n please select the option!")
        user_type=['1.admin','2.user', '3.Exit']
        print(user_type[0])
        print(user_type[1])
        print(user_type[2])
        user_type=input("Enter the user type : ")
        if user_type=="1":
            admin()
        if user_type=="2":
            client()
        if user_type=="3":
            break
        
def admin():
       # x=admin_list[x]
        
        admin_name=input("Enter the admin Name : ")
        password=input("Enter the password : ")
        A=admin_list.index(admin_name)
        B=passwords.index(password)

        if A==B:
            admin_choice()

        else:
            print("\ninvalid user name or password, please try again.\n")
            start()

def admin_choice():
    print("\n 1.Blance Amount Checking\n 2.Exit")
    choice=input("Enter the choice :")
    if choice == "1":
        #balance_amount=100000
        print("Available ATM balance is : ",balance_amount)
    if choice =="2":
        start()

def pin_change():
    accnt_nbr = input('Please Enter your Account number\n')
    pin = input('Please enter a four digit Pin\n')
    C=accnt_nbrs.index(accnt_nbr)
    D=pins.index(pin)
    if C==D:
        pin_ch=input("Enter the new pin : ")

        pins[D]=pin_ch
        client()
    else:
        print("Invalid details")

    
    
def client():
    print("\n 1.Withdraw  2.Deposit  3.Blance Enquiry  4.change pin Number \n 5.Exit ")
    client_choice=input("Enter the choice : ")
    if client_choice=="1":
        withdraw()

    if client_choice == "2":
        deposit()
    if client_choice == "3":
        balance_enquiry()
    if client_choice == "4":
        pin_change()
    if client_choice =="5":
        start()

def withdraw():
    while True:
        accnt_nbr = input('Please Enter your Account number\n')
        pin = input('Please enter a four digit Pin\n')
        C=accnt_nbrs.index(accnt_nbr)
        D=pins.index(pin)
        #print(C)
        #print(D)
        acc_type = input('Please enter the type of account:\nChecking: "C", Saving: "S", Business: "B"\n')
        withdraw_amnt = int(input('Enter the amount you want to withdraw\n'))
        E=acc_types.index(acc_type)
        if C == D:
            print("")
            if withdraw_amnt <= balances[C]:
                client_withdraw =balances[C] - int(withdraw_amnt)
                balances[C]=client_withdraw
                print("your Account number :",accnt_nbr)
                print("Pin Number is ****")
                #print( "account balance is ",balances[D])

                print("Remaining Balance is :",client_withdraw)
                print("Amount is Successfully withdrawed")
                balance_amount[0]=int(balance_amount[0])-int(withdraw_amnt)

                client()
            else:
                print("insufficient balance.")
                client()
                #balance_amount=100000
                #balance_amount=balance_amount - client_withdraw
                #return balance_amount
                #client()
        else:
            print("\ninvalid Account number or pin, please try again.\n")
            withdraw()

def deposit():
    accnt_nbr = input('Please Enter your Account number\n')
    pin = input('Please enter a four digit Pin\n')
    C=accnt_nbrs.index(accnt_nbr)
    D=pins.index(pin)

    acc_type = input('Please enter the type of account you want to open:\nChecking: "C", Saving: "S", Business: "B"\n')
    deposit_amnt = int(input('Enter the amount you want to deposite\n'))
    if C == D:
        print("your Account number :",accnt_nbr)
        print("Pin Number is ****")
        #print( "account balance is ",balances[D])

        balances[C]=balances[C]+deposit_amnt
        print("Now your account balance is ", str(balances[C])+" INR.")
        print("Amount Successfully Deposited.")
        balance_amount[0]=int(balance_amount[0])+int(deposit_amnt)
        client()
            
    else:
        print('Information you entered is not in valid! Please try again')
        deposit()
        
    
def balance_enquiry():
    accnt_nbr = input('Please Enter your Account number\n')
    pin = input('Please enter a four digit Pin\n')
    C=accnt_nbrs.index(accnt_nbr)
    D=pins.index(pin)

    acc_type = input('Please enter the type of account you want to open:\nChecking: "C", Saving: "S", Business: "B"\n')

    if C == D:
        print("your Account number :",accnt_nbr)
        print("Pin Number is ****")
        balance_enquiry=balances[C]
        print("Now your account balance is ", str(balance_enquiry)+" INR.")
            
    else:
        print('Information you entered is not in valid! Please try again')
        client()


    
admin_list=['geetha','anjali','pavi']
passwords=['g123','a123','p123']
balance_amount=['50000']
accnt_nbrs=['102030','102031','102032']
pins=['7070','8080','9090']
acc_types=['s','s','b']
balances=[50000,15000,20000]


start()
