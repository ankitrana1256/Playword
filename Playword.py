import time
import random

print("WELCOME TO PLAYWORD\n")
time.sleep(1)
print("Rules:\nFor every right answer you will get 10 points extra.\nFor every wrong answer 5 points will be deducted.\nThere is no space between numbers.")
time.sleep(1)
print("\nGame will start in 5 seconds")
time.sleep(1)
print("GET READY")
timelimit = 5
for n in range(timelimit):
    print(str(timelimit - n) + " seconds left")
    time.sleep(1)

print("Game Begins!\n")
print("Convert it into numbers if A = 0 & Z = 25")
score = 0

for i in range(10):
    print("QUESTION " + str(i+1))
    Alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    first_word = random.choice(Alphabet)
    second_word = random.choice(Alphabet)
    third_word = random.choice(Alphabet)
    fourth_word = random.choice(Alphabet)
    final_word = first_word + second_word + third_word + fourth_word
    print("YOUR WORD IS: " + final_word)

    a = Alphabet.index(first_word)
    b = Alphabet.index(second_word)
    c = Alphabet.index(third_word)
    d = Alphabet.index(fourth_word)
    list1 = [a , b , c , d]
    result = int(''.join(map(str, list1)))
    
    while True:
        try:
            Answer = int(input("TYPE YOUR ANSWER HERE: "))
        except:
            print("PLEASE ENTER A NUMBER")
        else:
            print("ANSWER SUBMITTED")
            break
    
    if Answer == result:
        print("Right answer")
        newscore = score + 10
        print("YOUR SCORE IS: " + str(newscore) + " pts" + "\n")
    else:
        newscore = score - 5
        print("WRONG ANSWER...BETTER LUCK NEXT TIME")
        print("YOUR SCORE IS: " + str(newscore) + " pts")
        print("RIGHT ANSWER IS " + str(result) + "\n")
    time.sleep(1)
    score = newscore