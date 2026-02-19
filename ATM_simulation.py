# Function to display ATM welcome screen
def show_welcome():
    print("=" * 40)
    print("           🏦 ATM SERVICE 🏦")
    print("=" * 40)
    print(f"\nPlease insert your card...")
    print(f"Card Detected.")

# Function to check daily withdrawal limit (₹10,000)
def daily_limit(withdrawal,withdraw_amount):
    total_amount_withdraws=withdraw_amount+withdrawal
    return total_amount_withdraws<=10000

# Main function that runs the ATM system
def main():
    show_welcome()   # Display welcome screen

    # Initial account setup
    total_balance=100000 
    current_pin="1234"
    attempts=0
    deposited=0
    withdrawal=0
    no_of_transactions=0
    remaining_attempts=3

    # 🔐 PIN Authentication (maximum 3 attempts)
    while attempts<3:
        pin=input("\nEnter your 4-digit PIN: ")
        print("Verify....")
        if pin == current_pin:
           print("\nLogin successful!")
           print("-"*30)
           break 
        else:
            print("❌ Incorrect PIN")
            attempts+=1
            remaining_attempts-=1 
            print(f"\nAttempts remaining: {remaining_attempts}")
            continue

    # Block card after 3 failed attempts    
    if attempts == 3:
        print("🔒 Too many incorrect attempts. Card blocked.")
        return
    
    print(f"Total Balance in Your Account:  ₹{total_balance:.2f}") 

    # 🔁 Main ATM Menu Loop   
    while True:
        print(f"\n =================== MAIN MENU =================== ")
        print("\n1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

        choice=int(input("\n🔏 Enter your choice (1-4) : "))

         # 💸 Withdrawal Section
        if choice==1:
            withdraw_amount=int(input("\n💸 Enter amount to withdraw: "))
            if withdraw_amount>0:
                if daily_limit(withdrawal,withdraw_amount):    
                    if withdraw_amount<=total_balance:
                        total_balance-=withdraw_amount 
                        withdrawal+=withdraw_amount
                        remaining_withdraw_amount=10000-withdrawal
                        print(f"\n⌛ Processing transaction...")
                        print(f"🏧 Please collect your cash.")
                        print(f"\n₹{withdraw_amount} debited successfully.")
                        print(f"\nRemaining Balance: ₹{total_balance:.2f}")
                        print(f"Daily Withdrawal Remaining: ₹{remaining_withdraw_amount:.2f}")
                        no_of_transactions+=1
                    else:
                        print("⚠️ Insufficient balance")   
                else:
                    print("\nTransaction declined.")
                    print("Reason: Daily withdrawal limit exceeded")
            elif withdraw_amount <= 0:
                    print("Invalid amount")        
            continue

         # 💰 Deposit Section
        elif choice == 2:
            deposit_amount=int(input("\n💰 Enter amount to deposit: "))
            if deposit_amount>0:
                total_balance+=deposit_amount 
                print(f"\n✔️ ₹{deposit_amount} deposited successfully.")
                print(f"Updated Balance:{total_balance:.2f}") 
                deposited+=deposit_amount
                no_of_transactions+=1
            elif deposit_amount<=0:
                print("Invalid amount")    
            continue

        # 📊 Balance Inquiry / Mini Statement
        elif choice == 3:
            if no_of_transactions>0:
                print("================= MINI STATEMENT ===================")
                print(f"\nDeposited ₹{deposited}")
                print(f"Withdrew ₹{withdrawal}")
                print("\n"+"-"*30)
                print(f"💵 Current Balance: ₹{total_balance:.2f}")
                print("-"*30)
            else:
                print("\nNo Transactions Happened")    
            continue

         # 🚪 Exit ATM
        elif choice==4:
            print(f"\n🙏 Thank you for using Python ATM")
            print(f"👋 Please collect your card")
            print(f"💖 Have a great day!")
            break

        # ❌ Invalid Menu Option
        else:
            print("Entered Invalid Choice") 
            continue       
main()