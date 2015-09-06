#!/usr/bin/python

import csv
import sys
import tweepy
import config
import time
from dateutil.parser import parse

class DeadDove:

  # Inits the class with base calls/logic
  # :param options|array
  def __init__(self, options):
    print('Starting dead dove...')
    self.deleted = 0
    self.missing = 0
    self.checkConfig()
    self.parseOpts(options)
    print('Deleted a total of ' + str(self.deleted) + ' tweets. ' + str(self.missing) + ' did not exist. Rest easy.')

  # Sets our config to class vars
  def checkConfig(self):
    self.twitter = config.twitter
    self.options = config.options

  # Parses the options passed on the CLI, override the config
  def parseOpts(self, options):
    if set(['--help', '-h']) & set(options):
      self.displayHelp()
    else:
      self.setAPI()
      self.parseCSV()

  # Displays our help menu
  def displayHelp(self):
    print("This will display our help menu. Probably will be super janky.")
    sys.exit()

  # Parses the CSV with only the tweets older than the date specified
  def parseCSV(self):
    archive  = open(self.options['archive'])
    tweets   = csv.DictReader(archive)
    time     = self.getEpoch(self.options['date'])

    for row in tweets:
      tweetTime  = self.getEpoch(row['timestamp'])
      if(tweetTime < time):
        print('Deleting (' + row['timestamp'] + '): ' + row['text'])
        self.deleteTweet(row['tweet_id'])

    archive.close()

  # Returns the unix timestamp for maths
  def getEpoch(self, timestamp):
    dt = parse(timestamp)
    return time.mktime(dt.timetuple())

  # Sets the API using the auth keys from the config
  def setAPI(self):
    auth = tweepy.OAuthHandler(self.twitter['consumer_key'], self.twitter['consumer_secret'])
    auth.set_access_token(self.twitter['access_token'], self.twitter['access_token_secret'])

    self.api = tweepy.API(auth)

  # Passes the call to the twitter api to drop it like it's hot
  # I am using a 5 second sleep call to slow the hits to the API (rate limiting)
  def deleteTweet(self, id):
    try:
      self.api.destroy_status(id)
      self.deleted = self.deleted + 1
      time.sleep(5)
    except tweepy.error.TweepError:
      self.missing = self.missing + 1

if __name__ == "__main__":
  DeadDove(sys.argv[1:])
