from random import randint


def guess_num():
    print("I'm thinking of a number b/w 1 and 20.\nGuess the number!")
    secret_num = randint(1, 20)
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
        if count >= 5:
            print("You have exceeded the limit of {} guesses! Good Bye!".format(count))
            break


if __name__ == '__main__':
    guess_num()

