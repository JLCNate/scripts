#! /usr/bin/python

from mpd import MPDClient
client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("localhost", 6600) 

artist = client.currentsong()["artist"]
title =  client.currentsong()["title"]
print


import tweepy, time, facebook
from credentials import *

""" Credentials should be included into a separate file in the following format
# Twitter Auth Vars
CONSUMER_KEY = 'foobar'
CONSUMER_SECRET = 'foobar'
ACCESS_KEY = 'foobar'
ACCESS_SECRET = 'foobar'
#Facebook Auth
FACEBOOK_AUTH = "foobar"
"""


#Twitter Auth Method
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#Facebook Auth Method
graph = facebook.GraphAPI(FACEBOOK_AUTH)

# Append any text to your post or leave as it is
nowplaying = "#NowPlaying: %s - %s " % (artist,title)
sharing = nowplaying + raw_input("Message: %s \nAppend message to post?\n" % nowplaying)

# Send api call to both facebook and Twitter
api.update_status(nowplaying)
graph.put_object("me", "feed", message=nowplaying)
#Print the posted message for feedback
print("Posted " + sharing)
