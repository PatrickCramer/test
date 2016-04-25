# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen
import json
import pickle

# Create your views here.

def index():
    # Deze apirequest moet met celery afgehandeld worden.

    apirequest = Request('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    apiresponse = urlopen(apirequest)
    keys = apiresponse.read()
    keys = json.loads(keys)
    keys = keys[0:50]

    # Haal voor iedere key een title en een url op
    hn = {}
    k = 1
    # Set up dict with keys from HN API
    for i in keys:
        url = 'https://hacker-news.firebaseio.com/v0/item/'+str(i)+'.json?print=pretty'
        story_response = urlopen(Request(url))
        story_response = story_response.read()
        story = json.loads(story_response)
        title = story.get('title')
        url = story.get('url')
        score = story.get('score')
        # Put data in hn dict
        hn[k] = [title,url,score]
        k += 1
    print 'Got '+ str(k) + ' keys from hackernews'


    # save string in file using pickle
    hn_file = hn
    file = open('file_hn.txt', 'wb')
    pickle.dump(hn_file, file)
    file.close()
    print 'Saved info to file_hn.txt'


