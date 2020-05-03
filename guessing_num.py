from random import randint


def guess_num():
    print("I'm thinking of a number b/w 1 and 20.")
    secret_num = randint(1, 20)

    print('Guess number: ')
    count = 0
    while True:
        guess = int(input())
        while guess != secret_num:
            if guess < secret_num:
                print('Your guess is too low,\tTake a guess!')
            elif guess > secret_num:
                print('Your guess is too high,\tTake a guess!')
            break
        if guess == secret_num:
            print("You guessed it in {} guesses".format(count))
        count = count + 1
        if count >= 6:
            print("You guesses {} has exceeded the limit".format(count))


if __name__ == '__main__':
    guess_num()

