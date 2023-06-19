#write a python script to enter any number and check its it prime or not
choice=1
while(choice!=6):
    print("1. CHECK NUMBER IS PRIME OR NOT")
    print("2. SUM OF GIVEN DIGIT")
    print("3. CHECK NUMBER IS PALINDROME OR NOT")
    print("4. CHECK NUMBER IS AN ARMSTRONG OR NOT")
    print("5. COUNT VOWEL IN A STRING")
    print("6. EXIT")
    choice=int(input('enter your chocie :'))
    if choice==1:
        n=int(input('enter number : '))
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c+=1
        if c==2:
            print(f'\n{n} is a prime number\n')
        else:
            print(f'\n{n} is not a prime number\n')
    elif choice==2:
        num=input("enter number :")
        s=0
        for i in num.split():
            s+=int(i)
        print(f"\nsum of given number : {s}\n")
    elif choice==3:
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
    elif choice==4:
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
    elif choice==5:
        n=input("enter string :")
        vowels=0
        for i in range(len(n.lower())):
            if n[i] in ['a','e','i','o','u']:
                vowels+=1
        print(f'{n} contain {vowels} vowels')
