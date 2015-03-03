'''
Created on Mar 3, 2015

@author: amagoon
'''
import time
from fullMetaJacket import work as w
from fullMetaJacket import extractMeta as e
from fullMetaJacket import createPrintout as c
import sys

start = time.clock()

def main():
    url = "https://dsadetection.com/dev/ied-threat-training-aids/ied-training-kits/complete-kits/tsk7100-explosives-sample-kit.html"
    file_name, domainFolder, html_dir = w.define_page(url)
    file_location = sys.path[0] + '\\' + html_dir + '\\' + file_name
    title, altSet, metaSet = e.extractMeta(file_location)
    printLocation = domainFolder + '\\' + title + '.txt'
    c.createPrintout(printLocation, title, altSet, metaSet)
    print("""Filename: %s
File Location: %s""" % (title, printLocation))

main()

print(time.clock() - start)
print("Operation complete.")
