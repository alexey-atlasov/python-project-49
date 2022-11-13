#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()


print('Answer "yes" if the number is even, otherwise answer "no".')
count = 0
while count != 3:
    q = input('Question: ')
    answer = input('Your answer: ')
    if int(q) % 2 == 0 and answer == 'yes' :
        print ('Correct!')
        count += 1
    elif int(q) % 2 != 0 and answer == 'no':
        print ('Correct!')
        count += 1
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'")
        print("'Let's try again, Bill!")
        break
