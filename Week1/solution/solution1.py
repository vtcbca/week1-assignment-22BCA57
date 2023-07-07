#Write a python script to enter any number and check its prime or not.
n=int(input('enter number : '))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(f'\n{n} is a prime number\n')
else:
    print(f'\n{n} is not a prime number\n')
