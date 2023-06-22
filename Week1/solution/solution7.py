"""
Write a python script to enter any string, replace vowel with its position number.
For Example:
             input: Amit
             output:0m2t
"""
name=input("Enter string :")
new_name=""
for i in range(len(name)):
    if i%2!=0:
        new_name+=name[i]
    else:
        new_name+=str(i)
print(new_name)
