import random

from login import api

api.PostUpdate("Tweet automatico: {}".format(random.randint(1, 100)))
