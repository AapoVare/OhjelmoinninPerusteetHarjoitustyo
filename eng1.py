"""
Made by: Aapo Väre
Description:
    This program lets the user create a username and a password, then use them to log in.
    The program then writes the usernames and passwords into separate txt files.
    Originally this program was supposed to also be able to read the logins and passwords files so successful logins could be made with the info in them,
    but I failed to implement it correctly.
"""
from getpass import getpass
users = {}
status = ""
new_users = []
try:
    logins_file = open ("logins.txt", "x") 
    passwords_file = open ("passwords.txt", "x") # create the files if they don't exist
except:
    logins_file = open ("logins.txt", "a") 
    passwords_file = open ("passwords.txt", "a") # if the files do exist, open them in appending mode so they won't be overwritten

def StartMenu(): # Start menu that asks the user if they're registered or not
    status = str(input("Are you a registered user? y/n? Press q to quit: "))

    if status == "y":
        return OldUser() 
    elif status == "n":
        NewUser()
    elif status == "q":
        return status
    elif status != "q" or "y" or "n":
        print("Incorrect input!")

def NewUser(): # Here the user creates a new username and a password
    error_log = ""
    error_pass = ""
    while error_log != "ok": # Loops the program until the user gives a username that isn't taken
        CreateLogin = input("Create username: ")
        if CreateLogin in users:
            print("Username taken!")
        else:
            error_log = "ok"
            new_users.append(CreateLogin) # adds the created user to the list of new users
            while error_pass != "ok": # Loops until the passwords match
                logins_file.write(str(CreateLogin) + "\n") # writes the username into the username file
                CreatePassword = getpass("Create password: ") # this hides the password but still keeps the value of the variable
                confirm = getpass("Confirm password: ")
                if confirm == CreatePassword:
                    passwords_file.write(str(CreatePassword) + "\n") # writes the password into the passwords file
                    users[CreateLogin] = CreatePassword
                    print ("User created!")
                    print("Username: ", CreateLogin)
                    print ("Password: ", len(CreatePassword)*"*") # prints out stars according to how many characters are in the password
                    error_pass = "ok"
                else:
                    print("Passwords don't match!")

def OldUser(): # Here the user logs in with already existing credentials
    for i in range (1,4):
        login = input("Type username: ")
        password = input("Type password: ")
        if login in users and users[login] == password:
            print("Welcome ", login,"!")
            status_end = ""
            while status_end != "q": # This part is here if I want to add a menu function later on
                # print new menu
                status_end = input("Do you want to restart the program? Press q to quit: ")
                # depending on status/ input, do function
            return status_end
            break
        else:
            print("Incorrect username or password!")
    print("Too many failed attempts!")
    status = "q"
    return status
          
while True: # loops the program until the user presses q when the program asks 
    print (status)
    status = StartMenu()
    if (status == "q"):
        break

logins_file.close()
passwords_file.close()
if new_users != []: # if the list is not empty, prints out the new users made
    print("Following users made: ", new_users)
print ("Have a good day!")
# program ends.