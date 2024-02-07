import random
print("Welcome to the guessing game.")
Name = input("Enter your name: ")
print(f"Good Luck! {Name}")
words = ["ludo","avaitor","cards","bet"]
word = random.choice(words)
guess = input("Guess a character: ")
guesses = ''
attempts = 5
while attempts > 0:
    failed = 0
    for word in words:
        if guess in words:
            print(word, end=" ")
    else:
        print("_")
        failed += 1
    if failed == 0:
        print("You Win")
    print("Congratulation!! The word is: ",word)
    break
print() 
guesses += guess
if guess not in word:
    attempts -= 1
    print("Wrong input")

print("You have", + attempts, "more guesses")

if attempts == 0:
    print("You Loose")

