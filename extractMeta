'''
Created on Mar 3, 2015

@author: amagoon
'''

from bs4 import BeautifulSoup

def extractMeta(file_location):
    '''
        Returns structured alt text and meta
        data table from html to be used in printout.
    '''
    altSet = set()
    try:
        with open(file_location) as html:
            soup = BeautifulSoup(html)
            title = soup.title.contents
            title = title[0]
            rawImageSet = set(soup.find_all('img'))
            metaSet = set(soup.find_all('meta'))
    except (TypeError, FileNotFoundError):
        print("Could not open file. Program has been terminated.")

    else:
        ''' Attempts to use get() function to get only the alt text '''
        for image in rawImageSet:
            alt = image.get('alt','')
            if len(alt):
                altSet.add(alt)

    return title, altSet, metaSet
