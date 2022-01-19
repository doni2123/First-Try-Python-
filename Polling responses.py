from pip._vendor.progress import counter

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    name = name.title()
    response = input("Which mountain would you like to climb someday? ")
    response= response.title()
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

from collections import Counter
res = Counter(responses.keys())
print('\nMountains that would like to climb:', res)






