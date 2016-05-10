import random
import time

def main():
    verbs_file = "translations.tsv"
    verbs = parse_verbs(verbs_file)
    while True:
        verb = random.choice(verbs) 
        quiz_user(verb)
        print("Moving on......")
        print("\n\n")
        time.sleep(3)

def quiz_user(verb):
    print("What does " + verb[0] + " mean?")
    answer = raw_input()
    print("You said: " + answer + ". The correct answer is " + verb[1])
    if answer.strip() == verb[1].strip():
        print("You are correct!")
    else:
        print("Sorry. You were wrong. You need to practice " + verb[0])
    time.sleep(2)
    print("")

def parse_verbs(file):
    verbs = []
    for line in open(file):
        parts = line.split("\t")
        verbs.append((parts[0], parts[1]))
    return verbs

main()
