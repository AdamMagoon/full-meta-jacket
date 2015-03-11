'''
Created on Feb 16, 2015

@author: amagoon
'''

    #    Returns only what is between the alt tag
def returnAlt(line):
    key = 'alt="'
    end = '\"'
    start = line.find(key) + 5
    line = line[start::]
    endit = line.find(end)
    return line[:endit]

def alt(item):
    my_alt = ''
    if item.find("alt=") > -1:
        my_alt = returnAlt(item)
        if len(my_alt) > 0:
            return my_alt
    return ''

def meta(line):
    #    Keys
    line = str(line)
    description = 'name="description"'
    keywords = 'name="keywords"'
    content = 'content='
    lineSearch = line.lower()
    getDescription = lineSearch.find(description)
    getKeywords = lineSearch.find(keywords)
    getContent = lineSearch.find(content)
    new_line = line[getContent+9::]
    end = new_line.find('\"')
    my_line = new_line[:end]
    
    if getDescription > 0:
        return "Description: ", my_line
    if getKeywords > 0:
        return "Keywords: ", my_line

import os
import wget
from urllib.error import URLError
import urllib.request as u

def extract_name(string, dir):
    key = string.replace("https://",'')
    key = key.replace("http://",'')
    key = key.replace("www.", '')
    key = key.replace(dir,'')
    key = key.replace('.','-')
    key = key.replace('/', '-')
    if key[0] == '-':
        key = key[1::]
    return key


def define_page(url):
    """ 
    Sends a GET request to the specified URL. Saves the response to a file for later access.

        - Checks if archived file exists; creates file if neccessary
        - Makes URL Request if not
        - If 403 Error, creates spoof to bypass
        - Saves response to .txt file
    """

    # Imports
    from tld import get_tld
    from genericpath import getmtime
    import time

    # Local variables
    domain = get_tld(url)
    file_name = extract_name(url, domain) + '.txt'
    html_dir = domain + '\\html'
    file_path = html_dir + '\\' + file_name
    now = time.time()
    ageLimit = 604800

    if not os.path.exists(domain):
        os.makedirs(html_dir)
        print("New directory created: ", domain)

    if not os.path.isfile(file_path) or now - getmtime(file_path) > ageLimit:
        print("File does not exist or is past a week old...attempting to create a new reference file.")
        try:
            wget.download(url, file_path)
        except (URLError, ValueError) as e:
            print("Not a valid URL - ", e)
            try:
                print("Assembling spoof request")
                spoof = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'
                agentRequest = {'User-Agent': spoof}
                urlObject = u.Request(url, headers=agentRequest)
                page = u.urlopen(urlObject)
                try:
                    with open(file_path, 'w+') as f:
                        for line in page:
                            line = line.decode('utf-8')
                            f.write(line)
                except:
                    import sys
                    print("spoof failed\nTerminating program.")
                    sys.exit(0)
            except (URLError, ValueError) as er:
                print("Again, Not a valid URL - ", er)
                print("No further options available.\nTerminating program.")
                sys.exit(0)
        else:
            print("New reference file created.")
            print("Reference Filename: ", file_name)
    return file_name, domain, html_dir

def define_printout(url):
    name = extract_name(url)
    if name[-1] == '/' or name[-1] == '-':
        file_name = name + 'printout' + '.txt'
    else:
        file_name = name + '-printout' + '.txt'
    return file_name
