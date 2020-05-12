import string
import random

s1 = string.ascii_lowercase
#print(s1)
s2 = string.ascii_uppercase
#print(s2)
s3 = string.digits
#print(s3)
s4 = string.punctuation

#print(s4)
# Random Password Generator
while True:
    try:
        plen = int(input("Enter the length of password: "))
        break
    except:
        print("Onlu Integer is accepted")


s = []
# s.extend(list(s1))
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
print(len(s))
random.shuffle(s)
print("Your Password is:")
print("".join(s[0:plen]))
# print("Your Password is:")
# print("".join(random.sample(s,plen)))
