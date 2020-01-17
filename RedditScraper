#!python3
import tkinter as tk
import urllib.request as urllib2
import re

subreddit = "kroger"
redditBase = "http://reddit.com/r/"
limit = 5

redditPost = {"URL": "-1",
              "topic": "-1",
              "body": "-1",
              "image": "-1",
              "user": "-1",
              "date": "-1",
              "upvotes": "-1",
              "commentsNum": "-1"}

def getPage(url):
    #Send headers so reddit doesn't think this is a bot even though it is
    req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    #Get the front page of reddit
    return urllib2.urlopen(req).read().decode('utf-8')    

def findCommentURLs(data):
    #Regex for /comment/ URLs
    m = re.compile('/comments/\w+/[A-za-z0-9_]+/')
    return m.findall(html)

def getPost(url):
    #Use Regex Strings to find then extract the data from the post
    reTopic = re.compile('\"_eYtD2XCVieq6emjKBH3m\">[A-Za-z0-9_].+<\/h1>')
    reTopicSub = re.compile('\"_.+">|<\/.+>')
    reBody = re.compile('class=\"_292iotee39Lmt0MkQZ2hPV.+?>.+?<\/div>')
    reBodySub = re.compile('class=\"_292iotee39Lmt0MkQZ2hPV.+?>|<\/div>')
    #reImage = re.compile('<img.+src=\".+\".+>')
    #reImageURL = re.compile('https*:\/\/.+?(?=\")')
    #reUser = re.compile('templateId\":\"2b52fb9e-652a-11e8-8a95-0ed6f365a1f0\",\"textColor\":\"\w+\",\"type\":\"\w+\"},\".+?\":{')
    #reUserSub = re.compile('templateId\":\"2b52fb9e-652a-11e8-8a95-0ed6f365a1f0\",\"textColor\":\"\w+\",\"type\":\"\w+\"},\"|\":{')
    reDate = '<a class=\"_3jOxDPIQ0KaOWpzvSQo-1s.+\">.+<\/a>' #This only pulls the "Posted x ys ago" data, not the timestamp.
    reDateSub = '<a class=\"_3jOxDPIQ0KaOWpzvSQo-1s.+\">|<\/a>'
    #reUpvotes = '<div class=\"_1rZYMD_4xY3gRcSS3p8ODO\".+>.+<\/div>'
    #reUpvotesSub = '<div class=\"_1rZYMD_4xY3gRcSS3p8ODO\".+\">|<\/div>'
    #reCommentsNum = '<span c\w+=\"FHCV02u6Cp2zYL0fhQPsO\">.+<\/span>'
    #reCommentsNumSub = '<span c\w+=\"FHCV02u6Cp2zYL0fhQPsO\">| comments*<\/span>'
    #Commented data fields display differently becase they're loaded from a script.


    #Use lookaround assertions to make runtime more efficient
    reUser = re.compile('(?<=author\":\").+(?=\",\"post)')
    reUpvotes = re.compile('(?<=score\":)\d+?(?=,\"is)')
    reCommentsNum = re.compile('(?<=numComments\":)\d+?(?=,\")')

    #Grab the data so we can begin sorting it
    data = getPage(url)
    #print(data)

    #Scrape info from AJAX Post Structure.
    reBitePostData = re.compile('domainOverride\".+?eventsOnRender\":.+?isScoreHidden\".+?\"saved\":.+?\"numComments\":.+?,\"upvoteRatio\".+?,\"author\":\".+?isSpoiler')
    bitePostData = re.search(reBitePostData, data).group()
    
    #Make a copy of what a reddit post "is"
    postInfo = redditPost.copy()

    #Populate it
    postInfo = {"topic": re.sub(reTopicSub, '', re.search(reTopic, data).group()),
                "body": re.sub(reBodySub, '', re.search(reBody, data).group()),
                "user": re.search(reUser, bitePostData).group(),
                "date": re.sub(reDateSub, '', re.search(reDate, data).group()),
                "upvotes": re.search(reUpvotes, bitePostData).group(),
                "commentsNum": re.search(reCommentsNum, bitePostData).group()}

    
    return postInfo.copy()

html = getPage(f'{redditBase}{subreddit}')

commentURLs = findCommentURLs(html)

#Make a list of i<=limit URLs because nobody wants to see all those posts 
toPrint = []
ran = 2 #We're going to increment, skip the current URL then try the next if we have duplicates
i = 0
while i <= ran:
    if (i>0):
        if (commentURLs[i] == commentURLs[i-1]):
            ran+=1
        else:
            toPrint.append(getPost(f'{redditBase}{subreddit}{commentURLs[i]}'))
    else:
        toPrint.append(getPost(f'{redditBase}{subreddit}{commentURLs[i]}'))
    i+=1
    
print(toPrint)
