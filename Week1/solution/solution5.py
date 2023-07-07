#Write a python script to enter any string and count vowel.
n=input("enter string :")
vowels=0
for i in range(len(n.lower())):
    if n[i] in ['a','e','i','o','u']:
        vowels+=1
print(f'{n} contain {vowels} vowels')
