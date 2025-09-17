# Account Points Manager

## 📌 Overview
Account Points Manager is a simple Python program that allows you to manage "accounts" stored in a text file.  
Each account has a **username** and an associated **point balance**.  

The program can:  
- Read existing accounts from a file (`accounts.txt`)  
- Add points to an existing account  
- Create a new account if the username does not already exist  

The program uses **lists, loops, decision structures, and file I/O** to manage account data.

---

## ✨ Features
- **File Access** → Reads from and writes to `accounts.txt`  
- **Account Management** → Create new accounts or update existing ones  
- **Input Validation** → User input is stripped of spaces before being processed  
- **Persistent Data** → Changes are always saved back to the text file  

---

## 📂 File Format
The program works with a text file called `accounts.txt`.  
Each line must follow this format:


### Example:
alice,50
bob,100

- When running the program, just enter the username (e.g., `alice`).  
- If the account exists, the program will look it up and allow you to update points.  
- If it doesn’t exist, the program will automatically create it for you.  

---

## ▶️ How to Run
1. Make sure `accounts.txt` is in the same folder as the program (optional).  
2. Run the Python program:  
   ```bash
   python account_manager.py
Follow the prompts:

Enter your username (no spaces allowed).

If the account exists, you can update its points.

If it doesn’t exist, the program will create it for you.

Points are updated and saved to accounts.txt.
