import random
import sys


def main():
    comp_num = random.randint(100, 999)
    user_guess = check_range()
    runner(comp_num, user_guess)


def runner(comp_num, user_guess):
    while user_guess != comp_num:
        if user_guess < comp_num:
            d_match = matches(comp_num, user_guess)
            print(str(d_match) + " digits are correct.")

            print("The number is too low")
            user_guess = check_range()


        elif user_guess > comp_num:
            print("The number is too high")
            d_match = matches(comp_num, user_guess)
            print(str(d_match) + " digits are correct.")

            user_guess = check_range()

    print("Congrats! You did it")


def check_range():
    user_guess = input("Your Guess: ")
    if check_integer(user_guess):
        user_guess = int(user_guess)
    else:
        user_guess = check_numeric(user_guess)
        user_guess = int(user_guess)
    if user_guess < 100:
        print("Input shouldn't be less than 100")
        sys.exit(1)


    elif (user_guess > 999):
        print("Input shouldn't be greater than 999")
        sys.exit(1)

    return user_guess


def split(word):
    return [char for char in word]


def check_integer(num):
    if num.isnumeric():
        return True
    else:
        return False


def check_numeric(num):
    new_num = num
    while not check_integer(num):
        new_num = input("Enter a valid number between 100 and 999: ")
        new_num = check_numeric(new_num)
        num = new_num
    return new_num


def matches(comp_num, user_guess):
    digit_match = 0
    comp_num_arr = str(comp_num)
    comp_num_arr = split(comp_num_arr)
    user_guess_arr = str(user_guess)
    user_guess_arr = split(user_guess_arr)

    for d in user_guess_arr:
        if d in comp_num_arr:
            digit_match += 1
    return digit_match


if __name__ == '__main__':
    main()
