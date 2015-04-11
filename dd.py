#!/usr/bin/python

import csv
import sys
import getopt
import tweepy
import pprint
import config

class DeadDove:

  # Inits the class with base calls/logic
  # :param options|array
  def __init__(self, options):
    self.checkConfig()
    self.parseOpts(options)

  # Sets our config to class vars
  def checkConfig(self):
    self.twitter = config.twitter
    self.options = config.options

  # Parses the options passed on the CLI, override the config
  def parseOpts(self, options):
    if('--help' or '-h') in options:
      self.displayHelp();
    else:
      self.setAPI()
      self.printTweets()

  # Displays our help menu
  def displayHelp(self):
    print("This will display our help menu. Probably will be super janky.")
    sys.exit

  # Sets the API using the auth keys from the config
  def setAPI(self):
    auth = tweepy.OAuthHandler(self.twitter['consumer_key'], self.twitter['consumer_secret'])
    auth.set_access_token(self.twitter['access_token'], self.twitter['access_token_secret'])

    self.api = tweepy.API(auth)

  # Retrieves our timeline, iterates over the tweets
  # This is going away, just put it in to test if the connection to tweeters worked
  def printTweets(self):
    public_tweets = self.api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)



if __name__ == "__main__":
  DeadDove(sys.argv[1:])