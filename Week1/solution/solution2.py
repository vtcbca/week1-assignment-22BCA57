#Write a python script to enter any number and print the sum of its digit.
num=input("enter number :")
s=0
for i in num.split():
    s+=int(i)
print(f"\nsum of given number : {s}\n")
