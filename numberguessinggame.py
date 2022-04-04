import random
number=random.randint(1,9)
chances=0
while chances<5:
    guess=int(input('enter your guess'))
    if guess==number:
        print('congratulations you won')
        break
    elif guess<number:
         print("YOUR GUESS IS TO LOW")   
    else:
        print('your guess is to high')
    chances+=1

if chances>=5:
    print("you lost the game")
    
