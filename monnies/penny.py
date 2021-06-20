######################################################################
# _______      _                        ______
#(_______)    (_)_   _                 (_____ \
# _      _ _ _ _| |_| |_  ____  ____    _____) )___ ____  ____  _   _
#| |    | | | | |  _)  _)/ _  )/ ___)  |  ____/ _  )  _ \|  _ \| | | |
#| |____| | | | | |_| |_( (/ /| |      | |   ( (/ /| | | | | | | |_| |
# \______)____|_|\___)___)____)_|      |_|    \____)_| |_|_| |_|\__  |
#                                                              (____/
#
######################### Monnie for SwearJar ########################

import requests, json, getopt, sys
import tweepy
from pyfiglet import Figlet

this = sys.modules[__name__]
this.tweetTagOpen = "<tweet>"
this.tweetTagClose = "</tweet>"
this.config = {}
this.api = {}

def authorize():
    config = {}

    with open("penny.apikey") as configFile:
        config = json.load(configFile)

    auth = tweepy.AppAuthHandler(config["twitter-appid"], config["twitter-appsecret"])
    this.api = tweepy.API(auth)

def printBanner():
    custom_fig = Figlet(font='stop')
    print("#####################################################################")
    print(custom_fig.renderText('Twitter Penny'))
    print("######################## Monnie for SwearJar ########################")

def loadConfig():
    global config
    with open("penny.cfg") as configFile:
        this.config = json.load(configFile)

def setOptions(argv):
    this.lang = ""
    this.query = ""
    this.collect = False
    this.censor = False
    this.analyze = ""

    usage = "penny.py -L <ISO 639-1 language> [-c,--collect|-s,--search <query>] [-x, --censor-mode] [-a, --analyze FILE]"

    try:
        opts, args = getopt.getopt(argv, "L:cs:xa:", ["lang=", "collect", "search=", "analyze=", "censor-mode"])
        print(opts)
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-L", "--lang"):
            this.lang = arg
        elif opt in ("-c", "--collect"):
            this.collect = True
        elif opt in ("-s", "--search"):
            this.query = arg
        elif opt in ("-a", "--analyze"):
            this.analyze = arg
        elif opt in ("-x", "--censor-mode"):
            this.censor = True

    if this.collect and this.query:
        print("--search and --collect are mutually exclusive")
        sys.exit(2)

    if this.collect and not this.lang:
        print("--lang is required when doing --collect")
        sys.exit(2)

    if this.analyze and not this.lang:
        print("--lang is required when doing --analyze")
        sys.exit(2)

def search(api, query, lang):
    tweets = []
    count = 1

    if this.censor:
        queryDisp = f"{query[:1]}******{query[-1]}"
    else:
        queryDisp = query

    for tweet in tweepy.Cursor(api.search, q=f"{query} -filter:retweets", lang=lang, result_type="recent", include_entities ="false").items(this.config["tweets_per_phrase"]):
        print(f"Getting tweets ('{queryDisp}''): {count}                   ",end="\r")
        tweets.append(f"{this.tweetTagOpen}{tweet.text}{this.tweetTagClose}")
        count+=1
    print(f"Tweets gathered ('{queryDisp}'): {count-1}                   ")
    return tweets

def analyzeTweets(filename, lang):
    with open(filename, "r", encoding="utf-8") as file:
        tweet = file.readline()
        while tweet:
            postData = {"s":tweet}
            requests.post(f"{this.config['swearjar-api']}/{lang}/analyze", data=postData)
            tweet = file.readline()

def collectTweets(api, lang):
    with open(f"{lang}_{this.config['output']}", "a", encoding="utf-8") as output:
        output.write("<tweets>")
        for q in this.config["phrases"][lang]:
            tweets = search(api, q, lang)
            output.writelines(tweets)
        output.write("</tweets>")

def main(argv):
    printBanner()
    setOptions(argv)
    loadConfig()
    authorize()

    if this.query:
        print(search(this.api, this.query, this.lang))
    elif this.collect:
        collectTweets(this.api, this.lang)

    if this.analyze:
        analyzeTweets(this.analyze, this.lang)

if __name__ == "__main__":
    main(sys.argv[1:])
