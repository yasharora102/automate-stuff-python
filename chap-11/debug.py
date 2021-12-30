import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
guess_int=0
if guess =='heads':
    guess_int = 1
else:
    guess_int = 0


toss = random.randint(0, 1) # 0 is tails, 1 is heads
print(toss)
if toss == guess_int:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess_int:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
