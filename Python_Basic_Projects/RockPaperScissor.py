# RockPaperScissors.py
# Purpose: Use random module, and loop
# Program: RockPaperScissor Game
#Pseudocode
""" Get initial Wins, Losses Ties
 Assign the value of Rock,Paper and Scissor 
 Give option to quit
 Let user give the input 
 Generate Rock Paper Scissor for opponent 
 Compare the input with the given variable and let user know if he won, lost or it tied
 Keep the counter for win,loss or ties
 End the program if player choses to quit"""


import random,sys

print('ROCK, PAPER, SCISSORS')
print('0 Wins, 0 Losses, 0 Ties')
win=0
loss=0
tie=0

while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    userinput=input()
    if userinput=='r' or userinput=='s' or userinput=='p' or userinput=='q':
        if userinput=='q':
            print('Do you really want to quit? y/n')
            quitinput=input()
            if quitinput=='n':
                print('Good Choice! The game will continue')
            elif quitinput=='y':
                print('See you later!')
                sys.exit()

        if userinput=='r':
            print('ROCK VERSUS')
        elif userinput=='p':
            print('PAPER VERSUS')
        elif userinput=='s':
            print('SCISSOR VERSUS')
    else: 
        print('Please only provide the follwing values: r,p,c,q ')
        break

    pcinputnum=random.randint(1,3)
    pcinputvalue=''
    if pcinputnum==1:
        pcinputvalue='r'
        print('ROCK')
    elif pcinputnum==2:
        pcinputvalue='p'
        print('PAPER')    
    elif pcinputnum==3:
        pcinputvalue='s'
        print('SCISSOR')
    if userinput== pcinputvalue:
        print('It is a Tie')
        tie+=1
    elif userinput=='r' and pcinputvalue=='s':
        print('You win')
        win+=1
    elif userinput=='r' and pcinputvalue=='p':
        print('You lose')
        loss+=1
    elif userinput=='p'and pcinputvalue=='s':
        print('You lose')
        loss+=1
    elif userinput=='p' and pcinputvalue=='r':
        print('You win')
        win+=1    
    elif userinput=='s'and pcinputvalue=='p':
        print('You win')
        win+=1
    elif userinput=='s' and pcinputvalue=='r':
        print('You lose')
        loss+=1
    print(str(win)+' Wins, '+str(loss)+ ' Losses, '+str(tie)+' Ties')


            
        


            
        
