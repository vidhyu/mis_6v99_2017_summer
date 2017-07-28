# Third Assignment

from __future__ import print_function
import requests # for sending Http requests
import os       # for getting functions to set OS paths
import zipfile  # module for Zip and Unzip file functions
import openpyxl # create/delete xl files. openpyxl is a pure python reader and writer of Excel OpenXML files (`.xlsx`, `.xlsm`).
import sqlite3  # for sqlite DB
import glob     # glob patterns specify sets of filenames with wildcard characters
import itertools as it  
import csv      # To work with CSV files
import numpy as np


# Step1 : Downloading and Extracting txt  training file

url = "http://kevincrook.com/utd/market_basket_training.txt"

r = requests.get(url) # this will connect to the url

f = open("market_basket_training.txt", "wb") # The wb indicates that the file is opened for writing in binary mode. On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.

f.write(r.content) # writes the entire content in the url to the zip file

f.close() # closes the file