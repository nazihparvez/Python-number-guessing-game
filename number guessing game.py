import random
#getting the limit and the number that is to be guessed
limit=int(input('enter the limit bro: '))
number = random.randint(1, limit)
print(f'guess the number between 1 and {limit}')
attempts=0
#no. of chances
chance=int(input('\nnumber of chances: '))
if chance<=0:
    print('alr bro thats enough, you cant play anymore')
#main game logic
while chance>0:
    guess=int(input('\nenter your guess : '))
    chance-=1
    attempts += 1
    percentage=(abs(number-guess)/limit)*100
    guesses=''
    if guess==number:
        print(f'YAYY you guessed it right! with {attempts} tries :D')
        break
#checking if the guess is already guessed
    elif str(guess) in guesses:
        print('You already guess this number before, Try Again')
        attempts-=1
        chance+=1
        guesses+=str(guess)
    elif guess>limit or guess<1:
        print('That is out of bounds, Try Again')
        chance+=1
        attempts-=1
    elif percentage<=5:
        print('you are veryy close')
    elif percentage<=15:
        print('you are close')
    elif percentage<=35:
        print('you are a lil far')
    else:
        print('you are quite far vro :C')
else:
    print(f'\nHAHA, you LOST, the number was {number}')

#i learned the while else loop and the string function f() thingy, and the random module and how to generate random integer.