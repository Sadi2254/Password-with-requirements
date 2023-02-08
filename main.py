# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random
import string


def randomPassword(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(size - 4):
        password += random.choice(all_chars)
    return password


pass_len = int(input("What would be the password length? "))
print("First Random Password is:", randomPassword(pass_len))
print("Second Random Password is:", randomPassword(pass_len))
print("Third Random Password is:", randomPassword(pass_len))