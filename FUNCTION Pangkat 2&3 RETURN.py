import seaborn as seaborn


def pangkatin(angka):
    int(angka)
    hasil = angka ** 2
    print(f"Pangkat dua dari {angka} adalah {hasil}")
pangkatin(60)

def pangkatin(number):
    int(number)
    hasil = number ** 3
    terpangkat = f"Hasil pangkat tiga dari {number} adalah {hasil}"
    return terpangkat
print(pangkatin(5))

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person
musician = build_person('jimi', 'hendrix', 76)
print(musician)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print('(press q if you wanna quit)')
    f_name = input("First name: ")
    l_name = input("Last name: ")
    if f_name == 'q':
        break
    listname = {'first': f_name, "last": l_name}
    print(listname)
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left. Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

alien_0 = {'color': 'green'}
alien_color = alien_0.get('color')
alien_points = alien_0.get('points',0)
print(alien_color)
print(alien_points)
