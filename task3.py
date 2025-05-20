import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        return "Username already exists"
    users[username] = hash_password(password)
    return "Created new user"

def login(username, password):
    if username in users and users[username] == hash_password(password):
        return "Login Successful"
    return "Login Failed"

print(register("john", "mypassword")) 
print(login("john", "mypassword"))     
