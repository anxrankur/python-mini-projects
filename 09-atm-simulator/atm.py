balance = 5000
correct_pin = "1234"

print("===== ATM SIMULATOR =====")

pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("Incorrect PIN!")
else:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance is: ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance += amount
                print(f"₹{amount:.2f} deposited successfully!")
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully!")

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid option.")
