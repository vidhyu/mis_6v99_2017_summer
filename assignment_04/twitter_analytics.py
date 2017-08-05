# Fourth Assignment

from __future__ import print_function
import requests # for sending Http requests 
import json
from collections import Counter

# Step1 : Downloading and Extracting json file

url = "http://kevincrook.com/utd/tweets.json"

r = requests.get(url) # this will connect to the url

f = open("tweets.json", "wb") # The wb indicates that the file is opened for writing in binary mode. On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.

f.write(r.content) # writes the entire content in the url to the zip file

f.close() # closes the file

f1 = open('tweets.json','rt')

json_data = json.load(f1)

f1.close()

my_list = []

for tweet in json_data:
    if 'text' in tweet:
        my_string = str(tweet['text'].encode('utf-8'))
        #my_string.split("'")[1])
        my_string = my_string.strip("b'")
        my_list = my_list +[my_string]
        
lang_list = []
for tweet in json_data:
    if "lang" in tweet:
        tweet_lang = str(tweet["lang"])
        lang_list = lang_list +[tweet_lang]

c = Counter(lang_list)
c = c.items()
c = list(c)
c = sorted(c, key=lambda x: x[1], reverse=True)

        

# Step2 : Print in Analytics file

fn = 'twitter_analytics.txt' # file name

# Step 2: Read data in Data Structures
with open(fn,'w') as f:
    print(len(json_data), file=f)
    print(len(my_list), file=f)
    for row in c:
        print(row[0]+','+ str(row[1]), file=f)
 