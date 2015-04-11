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

  def checkConfig(self):
    self.twitter = config.twitter
    self.options = config.options

  def parseOpts(self, options):
    if('--help' or '-h') in options:
      self.displayHelp();

  def displayHelp(self):
    print("This will display our help menu.")
    pprint.pprint(self.twitter)
    pprint.pprint(self.options)
    sys.exit

if __name__ == "__main__":
  DeadDove(sys.argv[1:])