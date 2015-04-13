# dead dove

I don't know what I expected.

![dead-dove](http://i.imgur.com/PLTZJRh.gif)

## environment

Requires a Python3 environment, OS X ships with 2.7 by default. I recommend setting up a virtualenv to use Python3 inside of.

```
sudo pip install virtualenv
virtualenv --python=/usr/local/bin/python3 python3_env
source python3_env/bin/activate
```

## usage

1) Request your [twitter archive](https://twitter.com/settings/account)  
2) [Create](https://apps.twitter.com) a twitter application with read & write access, generate a self-use token  
3) Copy & modify `config.sample.py` to `config.py`  
4) `python3 dd.py`

## flags

| flag          | value         | description            |
| :-----------: | :-----------: | :---------:            | 
| --help (-h)   | none          | Displays the help menu |

## requirements

- python3

## packages

- [tweepy](http://tweepy.readthedocs.org/en/v3.3.0/getting_started.html)

## license

MIT
