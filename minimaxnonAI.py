import random
totalstick = input('Determine stick numbers:')
print('Stick number is determined as:', totalstick)

# First player move
#ss
def robot(stick):
    y = stick % 4
    if y==0:
        y= random.randint(1,3)

    mov=int(y)
    while stick < int(y):
        print('you cannot choose more than sticks')
        y = random.randint(1, 3)
    mov = int(y)
    print('machine chose:', mov)
    total = stick-mov
    return total

def human(stick2):
    mov2= int(input('your turn:'))
    while stick2 < mov2:
        print('you cannot choose more than sticks')
        mov2 = int(input('your turn:'))
    while (1>mov2 or 3<mov2):
        print('you are only able to choose between 1-3')
        mov2 = int(input('your turn:'))
    print('human chose:', mov2)
    total = stick2-mov2
    return total

#will be arranged
players= [robot, human]

number1= input('Determine first player machine(0) or human(1):')
number2= input('Determine second player (0) or (1):')
playerarray=[]
playerarray.append(players[int(number1)])
playerarray.append(players[int(number2)])


print(*playerarray)

print('the game begins')
print(players[0])
print(players[1])
x=0
while True:

   totalstick = playerarray[x](int(totalstick))
   print('remained sticks:', totalstick)
   if totalstick == 0:
       print ('Player'+ str(x+1)+ ' Win')
       break
   x = x + 1
   x = x % 2



