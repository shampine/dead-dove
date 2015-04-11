#!/usr/bin/python

import csv
import sys
import getopt
import tweepy
import pprint
import config

class DeadDove:

  def __init__(self, options):
    self.checkConfig()
    self.parseOpts(options)
    self.testTweepy()

  def checkConfig(self):
    self.twitter = config.twitter
    self.options = config.options

  def parseOpts(self, options):
    if('--help' or '-h') in options:
      self.displayHelp();

  def displayHelp(self):
    print("This will display our help menu.")
    pprint.pprint(self.options)
    sys.exit

  def testTweepy(self):
    auth = tweepy.OAuthHandler(self.twitter['consumer_key'], self.twitter['consumer_secret'])
    auth.set_access_token(self.twitter['access_token'], self.twitter['access_token_secret'])

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

if __name__ == "__main__":
  DeadDove(sys.argv[1:])