import random
import os; os.system("cls")

number_of_trials = 100
number_of_people = 50
matching_birthdays = 0

for trial in range(number_of_trials):
    birthdays=set()
    
    for person in range(number_of_people):
        rnd_birthday=random.randint(1,365)
        birthdays.add(rnd_birthday)
        
    if len(birthdays) != number_of_people:
        matching_birthdays = +1
        
    print(matching_birthdays)
        

        