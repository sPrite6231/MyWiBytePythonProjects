import time


print("Hello, I heard that you wanted to meet the best philosopher in the world, Socrates. But, first I will use the socratic method on you and see how long you last.")
print("This is my job as his assistant, and you will have to be extra careful today because I got up on the wrong side of the bed.")
time.sleep = 6
print();

#answer = input("Tell the definition of courage\n")
#print(answer, 'apple', sep='')
#print(answer.strip(), 'apple', sep='')


answer = input("What is the defintion of courage?")

if answer.lower() == "being brave to stand up for others and what is right even if that requires sacrifice":
    print("You may have somehow gotten this answer right by guessing, but there will be much harder questions soon.")
    time.sleep = 2
    print()

else:
    print("How could you get this one wrong? It was the easiest question on my list. Your chances of meeting Socrates are very low.")
    time.sleep = 2
    print()

answer = input("Give me an 8 letter English word that describes life with at leat 2 vowels\n")
if len(answer) == 8:
    print("Your word has 8 letters...")
    count_a = answer.count("a")
    count_e = answer.count("e")
    count_o = answer.count("o")
    count_u = answer.count("u")
    count_i = answer.count("i")

    count_vowels = count_a + count_e + count_i + count_o + count_u
    if count_vowels > 2:
        print("You gave me more than two vowels. Stop wasting my time.")
    elif count_vowels < 2:
        print("You don't even know what vowels are. You couldn't even think of a 8 letter word with 2 vowels.")
    else:
        print("You are very lazy. You gave me the least amount of vowels just to get the question correct and over with quickly.")
        print("I am dissapointed in you.")

else:
    print("The word is not even 8 letters... do you remember how to count?")

print()
sentence = input("Tell me a sentence ending in 'free will'")
if sentence.endswith('free will'):
    print("Have you forgotten that punctuation helps philsophers dive into better arguments.")
elif sentence.endswith('free will.'):
    len_first = sentence.find(' ')
    if len_first < 5:
        print ("The first word in the sentence isn't descriptive enough to help other philosopheres communicate with you.")
else:
    print("You will make Socrates grumpy!")

print()
print("I don't know why I'm giving you an option but...")
print("Pick your preferred appointment time for next Tuesday; (A/B/C/D)")
print("A. 8 mins past midnight", "B. 16 mins before sunrise", sep='\t'); 
print("C. 24 mins before noon", "D. 48 mins after sunset", sep='\t');
appointment = input("Select which time you prefer, A/B/C/D\n")

if appointment == 'A':
    print("Careful, Socrates might be sleepy.")
if appointment == 'B':
    print("Warning, Socrates might be meditating.")
if appointment == 'C':
    print("Caution, Socrates might be thinking about the meaning of food instead of listening to you.")
if appointment == 'D':
    print("Beware, Socrates might be thinking about the meaning of life in solitary.")

print()
print("Good luck for your appointment, though I know you'll make a mess out of it. Bye for now.")
