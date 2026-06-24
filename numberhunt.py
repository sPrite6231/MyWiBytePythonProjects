import random
import time
n = random.randint(1, 100)

print('I have chosen a number between 1 and 100. Can you guess what that number is? You have upto 10 attempts.')


attempts = 0
max_attempts = 10
# To ensure that the loop starts, set the done flag to False

done = False

hint = 1
hints_tobe_given = False

while not done:
    try:
        hint_wanted = input("Would you like a hint?")
        
        if hint_wanted == 'yes' and hint < 5:
            hints_tobe_given = True
        else:
            hints_tobe_given = False
        
        if hints_tobe_given:
            print('Let me give you a hint.')

            if hint == 1:
                if n % 2 == 0:
                    print("The number is even.")
                else:
                    print("The number is odd.")
            
            if hint == 2:
                if n % 3 == 0:
                    print("The number is divisible by 3.")
                else:
                    print("The number is not divisible by 3.")
            
            if hint == 3:
                if n == 1:
                    print("The number is not prime.")
                elif n % 2 == 0:
                    if n !=2:
                        print("The number is not prime.")
                    else:
                        print("The number is prime.")
                else:
                    for kk in range(2, int(n/2)+1):
                        if n % kk == 0:
                            print("The number is not prime.")
                            break
                    if kk == int(n/2):
                        print("The number is prime.")
            
            if hint == 4:
                n_str = str(n)
                sum = 0
                for kk in n_str:
                    sum = sum + int(kk)
                print("The sum of the digits of the number is", sum)

            hint = hint + 1 

        guess = int(input('Guess the number\n'))
        attempts = attempts + 1

        if guess > n:
            print('My number is smaller than that\n')

        if guess < n:
            print('My number is larger than that\n')
    
        if guess == n:
            print("That is correct! You're good at this game.")
            print("You took", attempts, "attempts to guess it.")
            done = True

        if attempts > max_attempts:
            print("You no longer have any attempts remaining. You have failed this game.")
            done = True
    except:
        print("This is an invalid guess. I will be nice and not count this as an attempt, but please try a valid guess next time.")

print()
print()
done = False
time.sleep = 5
print("Now you pick a number from 1 to 100 and I will try to guess it.")
print("When you are ready, please press enter so that I can start guessing.")

input()

# Simple but correct algorithm

guess = 0
attempts = 0
guess_step = 10;
prev_answer = '1'

while not done:
    # guess = round((low + high)/2)
    answer = input("Is it "+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1

    if attempts > 1:
        if answer != prev_answer:
            # guess_step = round(guess_step/2)
            guess_step = guess_step - 1


    prev_answer = answer
    
    if answer.lower() == 's':
        guess = guess - guess_step
    if answer.lower() == 'l':
        guess = guess + guess_step
    if answer.lower() == 'y':
        print("I did it! I guessed the number!")
        print("I took", attempts, "attempts to guess it.")
        done = True


print()
print()

print("I think I can do better.")
print("Let me try binary search!")

# binary search

done = False
low = 0
high = 100
guess_step = 0
attempts = 0

while not done:
    guess = round((low + high)/2)
    answer = input("Is it "+ str(guess) + '? (y = Yes, s = smaller than that, l = larger than that) \n')
    attempts = attempts + 1

    if answer.lower() == 's':
        high = guess
    
    if answer.lower() == 'l':
        low = guess
    
    if answer.lower() == 'y':
        print("I did it! I guessed the number!")
        print("I took", attempts, "attempts to guess it.")
        done = True

print()
print()
print("THE END")
print("THE END")
print("THE END")
print("THE END")
print("THE END")
print()
