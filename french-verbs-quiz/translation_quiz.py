import random
import time

def main():
    verbs_file = "translations.tsv"
    verbs = parse_verbs(verbs_file)
    incorrect_answers = []
    for x in range(0, 20):
        verb = random.choice(verbs) 
        failure = quiz_user(verb)
        if (failure):
            incorrect_answers.append(failure)
        time.sleep(1)    
        print("")
        print("Question suivante....")
        print("")
        time.sleep(3)
    print_failures(incorrect_answers)

def quiz_user(verb):
    print("Quel est le sens de " + verb[0] + "?")
    answer = input()
    print("Tu as dit: '" + answer + "'")
    time.sleep(1)
    print("La bonne réponse est '" + verb[1] + "'")
    time.sleep(1)
    if answer.strip() == verb[1].strip():
        print("Vous avez raison!")
    else:
        print("Désolé. Votre response est incorrecte.")
        return (verb[0], answer)

def parse_verbs(file):
    verbs = []
    for line in open(file):
        parts = line.split("\t")
        verbs.append((parts[0].strip(), parts[1].strip()))
    return verbs

def print_failures(failures):
    print()
    print("You answered incorrectly to...")
    print()
    for f in failures:
        print(f[0] + " - you said: " + f[1])

main()
