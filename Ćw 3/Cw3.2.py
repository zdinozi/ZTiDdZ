from random import randint, choice, shuffle
import string

def generate_safe_password():
    letterList = ([string.punctuation, choice(string.digits), choice(string.ascii_lowercase), choice(string.ascii_uppercase)])
    for i in range(randint(4,15)):
        letterList.append(choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits))
    shuffle(letterList)
    return ''.join(letterList)

print(generate_safe_password())