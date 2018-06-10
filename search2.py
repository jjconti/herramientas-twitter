from TwitterSearch import *
from data import api

try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['phyton'])
    #tso.set_language('es')
    tso.set_include_entities(False)



    ts = TwitterSearch(
        consumer_key = 'A7rnVb7Ad4YdLraaQWMRnKTeU',
        consumer_secret = 'fvnDJCeAPPO6CEG2RAXNRoNiN2qO4FqQxrJLNnb3cpAH1oi2EL',
        access_token = '1002626003846475776-L1vFAajHz4rTqpVhRroDBCDOCqIobj',
        access_token_secret = 'Dqmm7bjrsjgFEvU6EtyRpjUGDnjyF3uFwfAkWcHr2aQDE'

    )

    cuenta = 0

    for tweet in ts.search_tweets_iterable(tso):
        usuario = tweet["user"]["screen_name"]
        status_id = tweet["id"]
        if "phyton" in tweet["text"]:
            #import ipdb;ipdb.set_trace()
            api.PostUpdate("@{} It's Python!".format(usuario), in_reply_to_status_id=status_id, auto_populate_reply_metadata=True)
            cuenta += 1
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )


    print(cuenta)
    
            



except TwitterSearchException as e:
    print(e)

