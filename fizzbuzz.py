'''
Created on Aug 15, 2017

@author: Bernd Hollerit
'''

if __name__ == '__main__':
    pass

for j in range(1,101):
    if j % 3 == 0 and j % 5 == 0:
        print ("fizzbuzz")
    elif j % 3 == 0:
        print ("fizz")
    elif j % 5 == 0:
        print ("buzz")
    else:    
        print (j)