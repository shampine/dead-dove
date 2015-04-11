#!/usr/bin/python

import csv
import sys
import getopt
import tweepy
import pprint
import config
import time
import datetime
from dateutil.parser import parse


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
      self.parseCSV()
      self.setAPI()
      self.printTweets()

  # Displays our help menu
  def displayHelp(self):
    print("This will display our help menu. Probably will be super janky.")
    sys.exit

  # Parses the CSV with only the tweets older than the date specified
  def parseCSV(self):
    archive  = open(self.options['archive'])
    tweets   = csv.DictReader(archive)
    time     = self.getEnoch(self.options['date'])

    for row in tweets:
      tweetTime  = self.getEnoch(row['timestamp'])
      if(tweetTime < time):
        pprint.pprint(row['text'])

  # Returns the unix timestamp for maths
  def getEnoch(self, timestamp):
    dt = parse(timestamp)
    return time.mktime(dt.timetuple())

  # Sets the API using the auth keys from the config
  def setAPI(self):
    auth = tweepy.OAuthHandler(self.twitter['consumer_key'], self.twitter['consumer_secret'])
    auth.set_access_token(self.twitter['access_token'], self.twitter['access_token_secret'])

    self.api = tweepy.API(auth)

  def deleteTweet(self, id):
    # delete stuffs



if __name__ == "__main__":
  DeadDove(sys.argv[1:])