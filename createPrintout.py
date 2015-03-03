'''
Created on Mar 3, 2015

@author: amagoon
'''
import time
from prettytable import PrettyTable
from fullMetaJacket import work as w

def createPrintout(filename, title, altSet, metaSet):
    ''' Writes structured meta data to a designated file. '''

    date = time.strftime("%m/%d/%Y")


    with open(filename, 'w+') as p:
        p.write(date+'\n')
        p.write('Page Title: '+title+'\n'+'\n')

        for alt in altSet:
            p.write("Image meta data: " + alt + '\n')
                        
        #    Creates PrettyTable
        for item in metaSet:
            try:
                mType, metaList = w.meta(item)
            except TypeError:
                pass
            else:
                table = PrettyTable([mType])
                for i in metaList.split(','):
                    table.add_row([i])
                p.write(table.get_string() + '\n')
