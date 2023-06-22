"""Write a python script to enter any number, if it is integer number,then check
its palindrom or not.Print appropriate message if it is not palindrom."""
n=int(input('enter number :'))
dul=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==dul:
    print(f"\n{dul} is a palindrome number\n")
else:
    print(f"\n{dul} is not a palindrome number\n")
