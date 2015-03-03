'''
Created on Feb 16, 2015

@author: amagoon
'''

def mainDataName(string):
    """ Function to extract domain name from URL """
    indexEnd = string.find("-")
    return string[:indexEnd]


def return_tags(line, key):
    end = '>'
    my_list = []
    
    #    Pass it a line, it'll return the tag
    def retrieve_tag(line):
        indx_end = line.find(end)
        return line[:indx_end+1], indx_end
    
    def if_find_key(line):
        lineS = line.lower()
        idx = lineS.find(key)
        if idx > -1:
            tag, idx_end = retrieve_tag(line[idx::])
            my_list.append(tag)
            line = line[idx_end+1::]
            if idx_end != -1:
                if_find_key(line)
    
    if_find_key(line)
    return my_list

def title(line):
    key = '<title>'
    findit = line.find(key)
    if findit != -1:
        endit = '</title>'
        stopit = line.find(endit)
        return line[findit+7:stopit]
    else:
        return ''
    
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
    findD = lineSearch.find(description)
    findK = lineSearch.find(keywords)
    c = lineSearch.find(content)
    new_line = line[c+9::]
    end = new_line.find('\"')
    my_line = new_line[:end]
    
    if findD > 0:
        return "Description: ", my_line
    if findK > 0:
        return "Keywords: ", my_line

import os
import wget
from urllib.error import URLError
import requests as r

def extract_name(string, dir):
    key = string.replace("https://",'')
    key = key.replace("http://",'')
    key = key.replace("www.", '')
    key = key.replace('ftp.','')
    key = key.replace(dir,'')
    return key.replace('/', '-')


def define_page(url):
    from tld import get_tld
    domain = get_tld(url)
    file_name = extract_name(url, domain) + '.txt'
    html_dir = domain + '\\html'

    if not os.path.exists(domain):
        os.makedirs(domain)
        os.makedirs(html_dir)
        print("New directory created: ", domain)

    if not os.path.isfile(html_dir + '\\' + file_name):
        print("File does not exist...attempting to create a new reference file.")
        try:
            wget.download(url, html_dir + '\\' + file_name)
        except (URLError, ValueError) as e:
            print("Not a valid URL - ", e)
            try:
                urlObject = r.get(url)
                print(urlObject)
            except (URLError, ValueError) as er:
                print("Again, Not a valid URL - ", er)
                return ''
        else:
            print("New reference file created.")
            print("Filename: ", file_name)
    return file_name, domain, html_dir

def define_printout(url):
    name = extract_name(url)
    if name[-1] == '/' or name[-1] == '-':
        file_name = name + 'printout' + '.txt'
    else:
        file_name = name + '-printout' + '.txt'
    return file_name
