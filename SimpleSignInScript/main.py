letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

username = input("Create a username: ")
if len(username) < 4:
    print("Username must be atleast 4 characters long!")
    exit()

password = input("Create a strong password: ")
if len(password) < 8:
    print("Password must be atleast 8 characters long")
    exit()

pin = input("Create a pin: ")
if len(pin) != 6:
    print("Pin must be 6 digits long!")
    exit()
if any(char in letters for char in pin):
    print("pin cannot contain letters!")
    exit()

print("************************Please Sign in**************************")

entered_username = input("enter username: ")
entered_password = input("enter password: ")
entered_pin = input("enter pin: ")

if entered_username == username and entered_password == password and entered_pin == pin:
    print("Access aquired.  Welcome back!")
elif entered_username != username and entered_password == password and entered_pin == pin:
    print("Access Denied. Username incorrect!")
elif entered_username == username and entered_password != password and entered_pin == pin:
    print("Access Denied. Password incorrect!")
elif entered_username == username and entered_password == password and entered_pin != pin:
    print("Access Denied. Pin incorrect!")
elif entered_username != username and entered_password != password and entered_pin == pin:
    print("Access Denied. Username & password incorrect!")
elif entered_username != username and entered_password == password and entered_pin != pin:
    print("Access Denied. Username & pin incorrect!")
elif entered_username == username and entered_password != password and entered_pin != pin:
    print("Access Denied. Password & pin incorrect!")
else:
    print("Login information incorrect! Please try again")