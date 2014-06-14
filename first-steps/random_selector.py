import random
import time

teams = [
	"Brazil",
  "Croatia",
  "Mexico",
  "Cameroon",
  "Spain",
  "Netherlands",
  "Chile",
  "Australia",
  "Colombia",
  "Greece",
  "Ivory Coast",
  "Japan",
  "Uruguay",
  "Costa Rica",
  "England",
  "Italy",
  "Switzerland",
  "Ecuador",
  "France",
  "Honduras",
  "Argentina",
  "Bosnia and Herzegovina",
  "Iran",
  "Nigeria",
  "Germany",
  "Portugal",
  "Ghana",
  "USA",
  "Belgium",
  "Algeria",
  "Russia",
  "Korea"
]

names = [
	  "Gwe",
  "Nick",
  "Nadia",
  "James",
  "Reuben",
  "Haifeng",
  "Lloyd",
  "Victor",
  "Luke",
  "Ian",
  "Charlie",
  "Ala",
  "Lou",
  "Louis",
  "Tony",
  "Andrey",
  "Gwe",
  "Nick",
  "Nadia",
  "James",
  "Reuben",
  "Haifeng",
  "Lloyd",
  "Victor",
  "Luke",
  "Ian",
  "Charlie",
  "Ala",
  "Lou",
  "Louis",
  "Tony",
  "Andrey"
]

random.shuffle(teams)

results = []

for team in teams:
	name = random.choice(names)
	names.remove(name)
	results.append((team, name))

print()
print("Welcome to the Artirix World Cup 2014 Sweepstakes Draw")
time.sleep(1)
print()
print("And we begin......")

time.sleep(2)
print()
print("First team out of the hat is....")

for team, name in results:
	time.sleep(3)
	print(team)
	time.sleep(1)
	print("The person who has drawn %s is..." % team)
	time.sleep(3)
	print("....%s!!!!" % name.upper())
	print()
	time.sleep(2)
	print("Next team out of the hat is....")

print()
print("And that concludes the Artirix 2014 World Cup Sweepstakes draw")
print("Thankyou for your attendance")
print()
print(results)
