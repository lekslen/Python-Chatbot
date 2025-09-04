def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    # reading a name
    your_name = input()
    print(f"What a great name you have, {your_name}!")

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    # reading all remainders
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())

    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print(f"Your age is {your_age}; that's a good time to start programming!")

def count():
    print('Now I will prove to you that I can count to any number you want.')

    # read a number and count to it here
    num_to_count = int(input())

    for num in range(num_to_count + 1):
        print(f"{num} !")

def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while True:
        user_answer = int(input())
        if user_answer == 2:
            break
        else:
            print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')

# Now we can use these functions
greet("Axel", 2025)
remind_name()
guess_age()
count()
test()
end()



