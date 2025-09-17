# Intro Programming Using Python Project
# Beauty Rewards Program
# Beauty Store Rewards Program
# This program allows a user to check and modify their rewards account balance.
# It reads and writes user account details to a file.

# Inputs: User inputs their account name and the action they want to perform (add points, subtract points, or check balance).
# Outputs: The program will display the updated account balance.

# To run:
# 1. Ensure there's an 'accounts.txt' file with account details in the format: 'username,points'.
# 2. Run the program and follow the prompts.

def read_account(file_name):
    # Reads the account details from the file and returns a list of accounts.
    accounts = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, points = line.strip().split(',')
                accounts.append([name, int(points)])  # Store as a list of [username, points]
    except FileNotFoundError:
        print("Account file not found. Creating a new one.")
        # Automatically create an empty file
        with open(file_name, 'w') as file:
            pass  # Just create the empty file
    return accounts

def write_account(file_name, accounts):
    # Writes the updated account details to the file.
    with open(file_name, 'w') as file:
        for account in accounts:
            file.write(account[0] + ',' + str(account[1]) + '\n')

def main():
    # Main function to interact with the user and manage their rewards account.
    file_name = "accounts.txt"
    accounts = read_account(file_name)

    # Ask for the user's account name
    user_name = input("Enter your account name: ").strip()  # Remove spaces before and after the input

    # If the user is new, create an account with 0 points
    user_found = False
    for account in accounts:
        if account[0] == user_name:
            user_found = True
            break

    if not user_found:
        print("Account not found. Creating a new account for " + user_name + " with 0 points.")
        accounts.append([user_name, 0])  # Add a new account with 0 points

    # Display the current balance
    for account in accounts:
        if account[0] == user_name:
            print("Current balance for " + user_name + ": " + str(account[1]) + " points")
            break

    while True:
        # Menu for user actions
        print()  # Creates a blank line for better readability
        print("What would you like to do?")
        print("1. Add points")
        print("2. Subtract points")
        print("3. Check balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()  # Remove spaces around choice input

        if choice == '1':  # Add points
            points = input("Enter points to add: ").strip()  # Remove spaces around points input
            try:
                points = int(points)  # Ensure the points are an integer
                for account in accounts:
                    if account[0] == user_name:
                        account[1] += points
                        print(str(points) + " points added! New balance: " + str(account[1]))
                        break
            except ValueError:
                print("Please enter a valid number for points.")
        elif choice == '2':  # Subtract points
            points = input("Enter points to subtract: ").strip()  # Remove spaces around points input
            try:
                points = int(points)  # Ensure the points are an integer
                for account in accounts:
                    if account[0] == user_name:
                        if points <= account[1]:
                            account[1] -= points
                            print(str(points) + " points subtracted! New balance: " + str(account[1]))
                        else:
                            print("Not enough points to subtract.")
                        break
            except ValueError:
                print("Please enter a valid number for points.")
        elif choice == '3':  # Check balance
            for account in accounts:
                if account[0] == user_name:
                    print("Your current balance is: " + str(account[1]) + " points")
                    break
        elif choice == '4':  # Exit the program
            print("Thank you for using the Beauty Store Rewards Program!")
            write_account(file_name, accounts)  # Save the updated data to the file
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
main()
