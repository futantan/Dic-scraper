#!/usr/bin/env python
import requests
import bs4
import sys


def printDic(words):
    try:
        response = requests.get("http://dict.youdao.com/search?", params=words)
        content = bs4.BeautifulSoup(response.text).find("div", class_="trans-container").ul.find_all('li')
    except requests.exceptions.ConnectionError:
        print "Network error"
    except AttributeError:
        print "No result"
    else:
        for line in content:
            print line.string


def getParams():
    if len(sys.argv) == 1:
        return
    else:
        words = ""
        for word in sys.argv[1:]:
            words += word + " "
        return words


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "No input"
    else:
        payload = {'q': getParams()}
        printDic(payload)