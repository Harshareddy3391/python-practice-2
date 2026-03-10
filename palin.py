"""val="halah"

if (val == val[::-1]):
    print("palin drom")
else:
    print("not palindrom") """  

val = input("Enter a word: ")

rev = ""

for i in val:
    rev = i + rev
"""
if val == rev:
    print("Palindrome")
else:
    print("Not Palindrome")"""


print(rev)