import random

names = []
with open('names.txt') as r:
    n = r.readlines()
    # noinspection PyRedeclaration
    names = [x.strip() for x in n]
for i in range(100):
    t = random.choice(names)
    a = f" model(**{{'name':'{t}', 'email':'{t}@zorro.com'}}).save()"
    print(a)
