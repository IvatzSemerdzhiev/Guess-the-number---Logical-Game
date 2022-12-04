import random


attempts = 0
def generate_secret_number():
    secret_number = random.randint(1, 101)
    return secret_number
def choose_level():
    level = input("Choose level- easy(e)/hard(h)->")
    if level == 'e':
        attempts = 10
        return attempts
    elif level == 'h':
        attempts = 5
        return attempts


print("% % % Guess the number! % % %")
attempts = int(choose_level())

secret_n = int(generate_secret_number())

called_numbers = []

while attempts > 0:
    print(f"Attempts left {attempts}")
    numbers = int(input("Your guess between 1 and 100 -> "))

    if numbers in called_numbers:
        print("You already gave this number!")
        continue
    else:
        if numbers != secret_n:

            attempts -= 1

            called_numbers.append(numbers)
            if numbers > secret_n:

                if numbers > secret_n and numbers > secret_n + 10:
                    print("No, far too high!")
                else:
                    print("No, far too high!")

            if numbers < secret_n:
                print("No, too low! ")
                if numbers < secret_n and numbers < secret_n - 10:
                    print("No, far too low!")




        else:
            print(f"*!*!*!* BINGO *!*!*!*")
            break

print("GAME OVER")
print(f"The secret number was {secret_n}")
print(f"Attempts left {attempts}")