import random
import time

def main():
    verbs_file = "translations.tsv"
    number_of_questions = 5
    verbs = parse_verbs(verbs_file)
    results = []
    for x in range(1, number_of_questions + 1):
        print("Question " + str(x) + " of " + str(number_of_questions) + "....")
        print()
        verb = random.choice(verbs) 
        result = quiz_user(verb)
        results.append(result)
        print("")
        time.sleep(2)
    print_results(results)

def quiz_user(verb):
    print("Quel est le sens de " + verb[0] + "?")
    answer = input()
    print("Tu as dit: '" + answer + "'")
    time.sleep(1)
    print("La bonne réponse est '" + verb[1] + "'")
    time.sleep(1)
    if answer.strip() == verb[1].strip():
        print("Vous avez raison!")
        return("correct", verb[0], answer, verb[1])
    else:
        print("Désolé. Votre response est incorrecte.")
        return("incorrect", verb[0], answer, verb[1])

def parse_verbs(file):
    verbs = []
    for line in open(file):
        parts = line.split("\t")
        verbs.append((parts[0].strip(), parts[1].strip()))
    return verbs

def print_results(results):
    print("Incorrect answers.....")
    print("")
    for r in results:
        if r[0] == "incorrect":
            print(r[1] + " - you said: " + r[2] + ". Correct answer: " + r[3])
    print("")
    print("Corect answers.....")
    print("")
    for r in results:
        if r[0] == "correct":
            print(r[1])


main()
