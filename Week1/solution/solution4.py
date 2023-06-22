"""Write a python script to enter any number, if it is integer number, then check
its armstrong or not. Print appropriate message if it is not armstrong."""
n=int(input('enter number :'))
dul=n
rev=0
while n!=0:
    rem=n%10
    rev=rev+(rem*rem*rem)
    n=n//10
if rev==dul:
    print(f"\n{dul} is an armstrong number\n")
else:
    print(f"\n{dul} is not an armstrong number\n")
