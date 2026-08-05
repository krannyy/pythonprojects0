password = input("Please enter your password: ")

def check_password_strength(password):
    uppercase = False
    numbers = False
    length = len(password)
    for letter in password:
        if letter.isdigit():
            numbers = True
        if letter.isupper():
            uppercase = True
    if length >= 8 and uppercase and numbers:
        print("Your password is strong.")
        return True 
    else:
        print("Your password is weak.")
        return False 



print(check_password_strength(password)) # we test the values after evaluating conditions for each letter in the password / boolean becomes (both) true and true, as each of these criteria is being met in the password string.

