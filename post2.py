import random

from login import api

FILE = 'darkweb2017-top10.txt'

with open(FILE, 'r') as f:
    lines = f.readlines()
    line = random.choice(lines)
    print(line)
    api.PostUpdate("Password popular: {}".format(line))
