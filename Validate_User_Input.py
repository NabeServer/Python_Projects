#1. username is no more than 12 chars
#2. username must not contain space
#3. username must not contain digits

username = input("Enter a username:")

result = username.find(" ")

if len(username) > 12:
    print("Username should not be more than 12 characters")
elif not result == -1:
    print("Your username should not have a space.")
elif not username.isalpha():
    print("Username can't conatin numbers.")

else:
    print(f"Welcome {username}")
