#!/usr/bin/python

from login import consumer_key, consumer_secret, access_key, access_secret

from TwitterSearch import *


try:
    tso = TwitterSearchOrder()  # crear un objeto para definir la búsqueda
    tso.set_keywords(['Python'])    # agregar las palabras claves a buscar
    tso.set_language('es')
    tso.set_include_entities(False) # no incluir entidades
    ts = TwitterSearch(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_key,
        access_token_secret=access_secret
    )

    for tweet in ts.search_tweets_iterable(tso):
        print( '@{} dijo: {}'.format(tweet['user']['screen_name'], tweet['text']))
except TwitterSearchException as e:
    print(e)

