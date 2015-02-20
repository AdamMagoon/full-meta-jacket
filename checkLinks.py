'''
Created on Feb 19, 2015

@author: amagoon
'''

import time
start = time.clock()
from urllib.error import URLError
from bs4 import BeautifulSoup
from urllib.request import urlopen

def log_traceback(e):
    import traceback
    tb_lines = traceback.format_exception(e.__class__, e, e.__traceback__)
    tb_text = ''.join(tb_lines)
    print(tb_text)
#     exception_logger.log(tb_text)


class Page(object):
    '''
    Scrapes all <a href= ></a> tags off of a HTML5 webpage.
    
    
    '''

    def __init__(self, file, url):
        self.file = file
        self.url = url
        try:
            self.soup = BeautifulSoup(open(file))
        except URLError as e:
            log_traceback(e)
        self.childLinks = set()
    
    def checkLink(self):
        """  Boolean : Checks validation of URL  """
        try:
            urlopen(file)
        except URLError as e:
            log_traceback(e)
            return False
        return True
        
    def getAllAnchors(self):
        """ Returns a set of all anchors on the page """
        anchorList = self.soup('a', href=True)
        return anchorList
    
    def getUniqueAnchors(self):
        """ Returns a set of all unique anchors on the page """
        anchorSet = set(self.getAllAnchors())
        return anchorSet
    
    def getUniqueAnchorCount(self):
        return len(set(self.soup('a', href=True)))
    
    def cleanAnchors(self, anchorList):
        pass
    
    def getAnchorCount(self):
        return len(self.soup.find_all('a', href=True))
    
    def getAnchorDuplicates(self):
        aList = self.getAllAnchors()
        aSet = set()
        for i,x in enumerate(aList):
            if x in aList[i+1::]:
                aSet.add(x)
        return aSet

    def getUniqueUrls(self):
        anchors = self.getUniqueAnchors()
        urls = set()
        for a in anchors:
            urls.add(a.get('href'))
        return urls
    
    def r_short(self):
        urlLen = len((self.url))
        childList = list(self.childLinks)
        for link in childList:
            if len(link) < urlLen:
                self.childLinks.remove(link)
                
    
url = 'https://www.dsadetection.com/'
file = 'dsadetection.txt'
home = Page(file, url)
links = home.getUniqueAnchors()
urls = home.getUniqueUrls()
print("Total Links: ", home.getAnchorCount())
for u in urls:
    home.childLinks.add(u)
print(len(home.childLinks), home.childLinks)
home.r_short()
print(len(home.childLinks), home.childLinks)  
print("Total time: ", time.clock() - start)
