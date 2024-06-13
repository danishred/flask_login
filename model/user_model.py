"""A model file contains an application's data
logic and the core information that the user can access
and manipulate:"""
import sqlite3
import re  # Import the regular expression module

# Connect to the SQLite database

class user_model():
    # this method is called from user_controller file
    def user_addone_model(self,data):    
        username = data['username']
        password = data['password']

        # Username validation
        if len(username) < 3:
            return "Username must be at least 3 characters long"
        if not username.isalnum():
            return "Username can only contain alphanumeric characters"

        # Password validation
        if len(password) < 8:
            return "Password must be at least 6 characters long"
        if not re.search(r'\d', password):
            return "Password must contain at least one number"

        user_data = (username, password)
        con = sqlite3.connect('users_cred.db')
        cur = con.cursor()

        # Check for duplicate username
        cur.execute("SELECT COUNT(*) FROM users WHERE username = ?", (data['username'],))
        count = cur.fetchone()[0]

        if count > 0:
           con.close()
           return "Username already taken"


        cur.execute("INSERT INTO users (username, password) VALUES(?, ?)",user_data)
        con.commit()
        con.close()
        return "User Created Succesfully"
    
    # to verify user credentials
    def user_Verification(self, username, password):
        conn = sqlite3.connect('users_cred.db')
        cur = conn.cursor()
        
        # Check if username and password combination exists
        cur.execute("SELECT COUNT(*) FROM users WHERE username = ? AND password = ?", (username, password))
        count = cur.fetchone()[0]

        conn.close()

        if count > 0:
            return "User verified successfully"
        else:
            return "Invalid username or password"
        