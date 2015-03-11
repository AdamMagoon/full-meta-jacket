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
    url = input("Enter URL")
    file_name, domainFolder, html_dir = w.define_page(url)
    html_location = sys.path[0] + '\\' + html_dir + '\\' + file_name
    title, altSet, metaSet = e.extractMeta(html_location)
    printout_name = file_name
    printLocation = sys.path[0] + '\\' + domainFolder + '\\' + printout_name
    c.createPrintout(printLocation, title, altSet, metaSet)
    print("""Filename: %s
File Location: %s""" % (printout_name, printLocation))

main()
