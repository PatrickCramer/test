# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pickle

def scrape_vk():
    url = 'http://www.volkskrant.nl'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    g_data = soup.find_all("article", {"class":"ankeiler ankeiler-teaser ankeiler-teaser--medior"})
    linklist = []
    for item in g_data:
        title = item.h2.text

        for link in item.find_all('a'):
            url = link.get('href')
        print title
        link = '<a href="'+url+'">'+title+'</a>'
        linklist.append(link)

    file = open('vk.txt', 'wb')
    pickle.dump(linklist, file)
    file.close()
    print 'scraping volkskrant done'
    return

def scrape_parool():
    url = 'http://www.parool.nl'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    p_data = soup.find_all("article", {"class": "ankeiler ankeiler-teaser ankeiler-teaser--hot"})
    linklist = []
    for item in p_data:
        title = item.p.text

        for link in item.find_all('a'):
            url = link.get('href')

        link = '<a href="' + url + '">' + title + '</a>'
        print title
        linklist.append(link)

    file = open('parool.txt', 'wb')
    pickle.dump(linklist, file)
    file.close()
    print 'scraping parool done'
    return

#scrape_vk()
#scrape_parool()




