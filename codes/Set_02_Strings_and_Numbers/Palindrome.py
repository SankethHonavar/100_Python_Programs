def is_palindriome(s):
    return s==s[::-1]
string=input("Enter a string: ")
if is_palindriome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")