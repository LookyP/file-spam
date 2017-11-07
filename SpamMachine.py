import random
import time
import string

def mainthingy():
    times = 0
    total = 0
    
    print('Starting:')
       
    print('...')
    
    print('...')
    
    print('...')
    
    for line in range(2):
        print()
    
    print('         Welcome to the SPAM-MACHINE!')
    
    print('            1. Spam and troll')
    
    print('            2. Exit the system')
    
    userFIRSTinput = input('            Please choose an option! ')
    if userFIRSTinput == '1':
        for line in range(2):
            print()
        userinput = int(input('            How many spams? '))
        for i in range(userinput):
            f = random.choice(string.ascii_letters)
            d = random.choice(string.ascii_letters)
            p = random.choice(string.ascii_letters)
            g = random.choice(string.ascii_letters)
            F = str(f)+ str(d)+'CLEANupTIME'
            G = str(g)+ str(p)+'HAVEfun.txt'
            file = open(F+G,'a')
            file = open(F+G,'w')
            file.write("hello")
            file.close()
            time.sleep(0.01)
        total += times + (userinput)
        print((total),'spams completed. Please check the folder for confirmation.')
        
        for line in range(5):
            print()
        mainthingy()
        
    elif userFIRSTinput == '2':
        print('Exiting the system')
        time.sleep(0.2)
        print('...')
        time.sleep(0.2)
        print('...')
        time.sleep(0.2)
        print('...')
    else:
        print('Sorry that is not a valid input')
        mainthingy()
    

mainthingy()
