import sys
import urllib3 as urllib
import io
import csv
import pandas as panda
from TwitterAPI import TwitterAPI

# Writes CSV file with bitcoin price data
def getBtcData():
    http = urllib.PoolManager()
    btc_url = 'https://api.bitcoinaverage.com/history/USD/per_minute_24h_sliding_window.csv'
    res = http.urlopen('GET', btc_url)
    f = open('newBtcData.csv', 'w')
    f.write(res.data)
    f.close()
    with open('newBtcData.csv', 'rb') as csvfile:
        myInfo = csv.reader(csvfile)
        myInfo = list(myInfo)
        start =  myInfo[1][1]
        end = myInfo[-1][1]
        print float(end) - float(start) 
        

def twitterData():
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # for each word in all the tweets
    # check if it is in the score dictionary
    # if it is add this score to the over all sentiment for the day
    #print scores.items() # Print every (term, score) pair in the dictionary
    search_term = 'bitcoin since:2015-3-3'
    consumer_key = 'r77hwOwZ29Vsquiy2Yzch2nlC'
    consumer_secret = '8b5CksWSTrewx0TMoKWc9OMr7QSAPLw18MDInAsp2Fy1zEIIY3'
    api = TwitterAPI(consumer_key,
                    consumer_secret,
                    auth_type='oAuth2')

    r = api.request('search/tweets', {'q': search_term})

    # define punctuation 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    tweetWords = []
    value = 0
    for item in r:
        if 'text' in item:
            words = item['text'].split(" ")
            no_punct = ""
            for thing in words:
                no_punct = ""
                for char in thing:
                    if char not in punctuations:
                        no_punct = no_punct + char
                # lets get the average for the sentiment
                for sentiment in scores:
                    if no_punct.lower() == sentiment:
                        value = value + scores[sentiment]
                        print sentiment + ' corresponds to: ' + str(scores[sentiment])
                        print 'here is the sentiment'
                        print value

                tweetWords.append(no_punct)

        else:
            print 'we have no text'
        f = open('newTwitterData.csv', 'w')
    f.close() 

def main():
    getBtcData()
    twitterData()

if __name__ == '__main__':
    main()