print(ord("."))
print(chr(65))

x=input("Enter a capital letter: ")
if ord(x)>=65 and ord(x)<=90:
    print("You have entered an upper case letter.")
if ord(x) >=97 and ord(x) <=122:
    print("You have entered an lower case letter.")
if ord(x) >=48 and ord(x) <=57:
    print("You have entered a didgit.")
