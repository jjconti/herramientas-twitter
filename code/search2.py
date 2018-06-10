#!/usr/bin/python

from TwitterSearch import *
from login import *

try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['phyton'])
    tso.set_include_entities(False)
    ts = TwitterSearch(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_key,
        access_token_secret=access_secret
    )

    cuenta = 0

    for tweet in ts.search_tweets_iterable(tso):
        usuario = tweet["user"]["screen_name"]
        status_id = tweet["id"]
        if "phyton" in tweet["text"]:
            api.PostUpdate("@{} It's Python!".format(usuario), in_reply_to_status_id=status_id,
                           auto_populate_reply_metadata=True)
            cuenta += 1
    print(cuenta)

except TwitterSearchException as e:
    print(e)

