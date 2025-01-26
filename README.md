# E-Voting System 🗳️

A simple and secure **E-Voting System** implemented in Python to manage voting processes for small-scale elections. The system features distinct roles for admins and voters, ensures voting integrity, and provides results in real-time.

## 🌟 Features
- **Admin Panel:**
  - Start or stop the voting process.
  - View real-time voting results, including total votes, voters who participated, and absentees.
- **Voter Functionality:**
  - Secure login with username and password.
  - Cast votes for candidates A, B, or C.
  - Prevents duplicate voting by tracking completed voters.
- **Real-Time Results:**
  - Total votes per candidate.
  - Number of voters and absentees.

## 🛠️ Tech Stack
- **Language:** Python

## 🚀 How It Works
1. **Admin Role:**
   - Admin logs in using predefined credentials.
   - Admin can start/stop voting and view results.
2. **Voter Role:**
   - Voters log in with their credentials.
   - Eligible voters can cast their vote when voting is active.
   - Each voter can vote only once.
3. **Voting Results:**
   - Votes for candidates are counted and displayed.
   - Participation and absentee details are provided.

## 🧩 Code Overview
The system includes the following key components:
- **Admin Credentials:** Stored in a dictionary.
- **Voter Credentials:** Stored in a separate dictionary for secure access.
- **Voting Process:** Controlled by an admin-initiated status.
- **Vote Count:** Tracks votes for candidates A, B, and C.
- **Completed Voters:** Prevents duplicate voting using a list.

## 📝 Sample Code
```python
# Function to display voting results
def results():
    print("Results are given below")
    print("A :", a)
    print("B :", b)
    print("C :", c)
    print("Total no.of voters: 6")
    print("No.of persons voted:", len(completed))
    print("No.of persons absent:", (6 - len(completed)))
```

## 🛠️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/DheerajKonakalla4/E-voting-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd E-voting-system
   ```
3. Run the program:
   ```bash
   python voting.py
   ```
4. Follow the prompts to log in as an admin or voter and interact with the system.

## 📸 Example Usage
1. **Admin Login:**
   - Username: `dheeraj`
   - Password: `1234`
2. **Voter Login:**
   - Sample voter usernames: `syam`, `tasleem`, `varun`
   - Passwords are predefined in the code.
3. **Voting Results:**
   - View results with total votes, participants, and absentees.

## 🚧 Limitations
- Designed for small-scale usage (e.g., limited number of voters).
- Credentials are stored directly in the code (could be improved with a database).

## 🤝 Contribution
Contributions are welcome! To contribute:
- Fork the repository.
- Create a new branch.
- Make your changes and submit a pull request.

## 📜 License
This project is licensed under the [MIT License](LICENSE).
