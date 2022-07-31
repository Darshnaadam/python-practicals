import string
def fun(str):
    a="abcdefghijklmnopqrstuvwxyz"
    for char in a:
        if char not in str.lower():
            return False
        else:
            return True
str = input('Enter the string:\n')
if (fun(str)==True):
    print("string is pangram")
else:
    print("string is not a pangram")
