"""Write a python script to enter any string and print only part of string.
Take input of start character and end character from user."""
name=input('Enter string :')
sc=input('Enter start character :')
ec=input('Enter end character :')
sc_index=name.index(sc)
ec_index=name.index(ec)
print(name[sc_index:ec_index+1])
