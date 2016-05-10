import random
import time

def main():
    verbs_file = "translations.tsv"
    verbs = parse_verbs(verbs_file)
    while True:
        verb = random.choice(verbs) 
        quiz_user(verb)
        print("Question suivante....")
        print("\n\n")
        time.sleep(3)

def quiz_user(verb):
    print("Quel est le sens de " + verb[0] + "?")
    answer = input()
    print("Tu as dit: " + answer + ".")
    time.sleep(2)
    print("La bonne réponse est " + verb[1])
    time.sleep(1)
    if answer.strip() == verb[1].strip():
        print("Vous avez raison!")
    else:
        print("Désolé. Votre response est incorrecte. Vous devez pratiquer " + verb[0])
    time.sleep(2)
    print("")

def parse_verbs(file):
    verbs = []
    for line in open(file):
        parts = line.split("\t")
        verbs.append((parts[0], parts[1]))
    return verbs

main()
