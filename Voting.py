# Define a function to display voting results
def results():
    print("Results are given below")
    print("A :", a)
    print("B :", b)
    print("C :", c)
    print("Total no.of voters: 6")
    print("No.of persons voted:",len(completed))
    print("no.of persons absent:",(6-len(completed)))

# Define an 'admin' dictionary to store admin credentials
admin = {"dheeraj": "1234"}

# Define a 'voter' dictionary to store voter credentials
voter = {
    "syam": "1901",
    "tasleem": "2003",
    "varun": "1426",
    "lokesh": "2005",
    "teja": "2000",
    "sai":"3000"

}

# Define a 'user' dictionary to associate usernames with roles (admin or voter)
user = {
    "syam": "voter",
    "dheeraj": "admin",
    "tasleem": "voter",
    "varun": "voter",
    "lokesh": "voter",
    "teja":"voter",
    "sai":"voter"
    }

# Initialize a list to keep track of completed votes
completed = []

# Initialize a variable to manage the voting process (0 for inactive, 1 for active)
status = 0

# Initialize variables to count votes for candidates A, B, and C
a = b = c = 0

# Initialize a boolean variable to control the main program loop
program = True

# Start the main program loop
while program:
    print("Welcome to online voting")
    
    # Prompt the user to enter their name (username)
    username = input("Please enter your name: ")
    
    # Check if the entered username is not in either the 'voter' or 'admin' dictionaries
    if username not in voter and username not in admin:
        print("You are not eligible to vote")
        continue  # Continue to the next iteration of the loop

    # Prompt the user to enter their password
    password = input("Please enter your password: ")
    
    # Determine the user's role (admin or voter)
    temp = user[username]

    # Check if the user is an admin
    if temp == "admin":
        # Verify the admin's password
        if admin[username] == password:
            print("Admin successfully logged in")
            print("Admin Features: 1) Start voting, 2) Stop voting, 3) View results")
            choice = input("Pick your choice: ")

            if choice == "1":
                status = 1  # Start the voting process
            elif choice == "2":
                continue  # Skip setting status to 0 to avoid stopping voting unintentionally
            elif choice == "3":
                results()  # Display voting results

    # Check if the user is a voter
    elif temp == "voter":
        # Verify the voter's password
        if voter[username] == password:
            print("Voter successfully logged in")

            # Check if the voter has already voted
            if username in completed:
                print("User has already voted; repetition is not allowed")
            else:
                # Check if the voting process is active
                if status == 1:
                    print("Voting has started; you can vote now")
                    print("Candidates: 1) A, 2) B, 3) C")
                    vote = input("Enter your vote (A, B, or C): ")

                    # Update vote counts for candidates A, B, and C
                    if vote == "A":
                        a += 1
                    elif vote == "B":
                        b += 1
                    elif vote == "C":
                        c += 1

                    # Add the username to the list of completed votes to prevent further voting
                    completed.append(username)
                else:
                    print("Voting is not started")
        else:
            print("Invalid user")

    # Handle the case where the user's role is neither admin nor voter
    else:
        print("Invalid user")
