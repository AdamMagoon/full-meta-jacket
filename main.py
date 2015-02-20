'''
Created on Feb 16, 2015

@author: amagoon
'''

import time
from fullMetaJacket import work as w
from prettytable import PrettyTable

webpage = input("Paste URL: ")
start = time.clock()
file_name = w.define_page(webpage)
dir = w.mainDataName(file_name)
date = time.strftime("%m/%d/%Y")

def startIndividualURL():
    my_img_set = set()
    my_meta_set = set()
    if file_name != '':
        try:
            with open(dir+'/'+file_name) as content:
                title = ''  #    Set to an empty string to detect a change
                try:
                    for line in content:
                        if title != '': #    No longer attempts to look for the title if it has changed
                            pass
                        else:
                            try:
                                title = w.title(line)
                            except:
                                pass
                        try:
                            #    Only difference between the two bellow variables are the keys passed
                            #    and what happens to the data after they get returned
                            images = w.return_tags(line, '<img')
                            meta = w.return_tags(line, '<meta')
                            for item in images:
                                my_img_set.add(str(item))
                            for item in meta:
                                my_meta_set.add(str(item))
                        except TypeError:
                            print('TypeError', line)
                except UnicodeDecodeError:
                    print("Unicode Error dudee")
                    
                printout = w.define_printout(webpage)
                try:
                    with open(dir+printout, 'w+') as p:
                        p.write(date+"\n")
                        if title != '':
                            try:
                                p.write('Page Title: '+title+'\n'+'\n')
                            except:
                                print("could not write title to file")
                                raise Exception
                        #    Pulls alt text from img tags
                        for item in my_img_set:
                            alt = w.alt(item)
                            try:
                                if len(alt) > 0:
                                    p.write("Image meta data: " + alt + '\n')
                            except Exception as exc:
                                raise RuntimeError("write alt text fail") from exc
                            
                        #    Organizes and cleans up meta data
                        for item in my_meta_set:
                            try:
                                mType, metaList = w.meta(item)
                            except TypeError:
                                pass
                            else:
                                table = PrettyTable([mType])
                                for i in metaList.split(','):
                                    table.add_row([i])
                                p.write(table.get_string() + '\n')
                except TypeError:
                    print("Create printout failed.")
                    
                print("""
Filename: %s
File Location: %s"""
    % (printout,"C:\Anaconda\Workspaces\Project Setup\src\scrapper\" + dir))
                
        except (TypeError, FileNotFoundError):
            print("Could not open file. Program has been terminated.")

startIndividualURL()
print(time.clock() - start)
print("Operation complete.")
