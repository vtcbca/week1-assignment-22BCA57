"""
Write a python script to enter any string, replace vowel with its position number.
For Example:
             input: Amit
             output:0m2t
"""
name=input("Enter string :").lower()
new_name=""
for i in range(len(name)):
    if name[i] in ['a','e','i','o','u']:
        new_name+=str(i)
    else:
        new_name+=name[i]
print(new_name)
