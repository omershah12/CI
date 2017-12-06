from random import randint
import re


cont  = True

while cont == True:
    
    g = input("Guess a number between 1 and 10: ")
    
    while g == "":
        g = input("Enter a number between 1 and 10: ")
        
    
   # regex = re.search('[a-zA-Z]+',g)
   # amt = regex.group()
    #use = len(amt)
  
    
        
   # while use > 0 :
    #    g = input("Please enter a number between 1 and 10: ")
    
    guessedNum = int(g)
    
    rnd = randint(1,10)
    
    while guessedNum > 10:
        guessedNum = int(input("Enter a number between 1 and 10: "))
    
    while guessedNum < 0:
        guessedNum = int(input("Enter a number between 1 and 10: "))
                            
    if guessedNum == rnd:
        print("Congratulations you guessed the number")
    else:
        print("Better luck next time")
        print("The number was %d" % rnd)
    
    cond = input("Do you wish to try again? Y/N: ")
    
    again = False
    
    while not again :
        if cond.upper() == "N":
            cont = False
            again = True
        elif cond.upper() == "Y":
            cont = True
            again = True
        else:
            cond = input("Please input Y/N: ")
    



