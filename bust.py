import urllib2
import requests
import sys
import os
import time

BASE_URL = "http://www.ejshs.emersonschools.org"
open_dir_list = open('dirlist.txt', 'r')
dirs = open_dir_list.read().split("\n")
open_dir_list.close()

for dir in dirs:
    uri = "{}/{}".format(BASE_URL, dir)
    response = requests.get(uri)
    if response.status_code == 200:
        print("[+] FOUND SOMETHING @ {}".format(uri))
        time.sleep(5)
    else:
        print("[!] NOT FOUND {}".format(uri))
