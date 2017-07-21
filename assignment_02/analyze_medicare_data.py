#Assignment02 

from __future__ import print_function
import requests # for sending Http requests
import os       # for getting functions to set OS paths
import zipfile  # module for Zip and Unzip file functions
import openpyxl # create/delete xl files. openpyxl is a pure python reader and writer of Excel OpenXML files (`.xlsx`, `.xlsm`).
import sqlite3  # for sqlite DB
import glob     # glob patterns specify sets of filenames with wildcard characters
import getpass
import csv      # To work with CSV files



# Step1 : Downloading and Extracting CSV files from data.medicare.gov

url = "https://data.medicare.gov/views/bg9k-emty/files/0a9879e0-3312-4719-a1db-39fd114890f1?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip"

r = requests.get(url) # this will connect to the url

staging_dir_name = "staging"

os.mkdir(staging_dir_name)  # mkdir will make the directory if it doesn't exist in the path

zip_file_name = os.path.join(staging_dir_name, "Hospital_Data.zip") # Zip file will be created in the mentioned Staging path

zf = open(zip_file_name, "wb") # The wb indicates that the file is opened for writing in binary mode. On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.

zf.write(r.content) # writes the entire content in the url to the zip file

zf.close() # closes the file

z = zipfile.ZipFile(zip_file_name,'r') # Open a ZIP file, where file can be either a path to a file (a string) or a file-like object. The mode parameter should be 'r' to read an existing file, 'w' to truncate and write a new file, or 'a' to append to an existing file.

z.extractall(staging_dir_name) 

z.close()


# Step2 : Create a SQLite DB to fill the data

glob_dir = os.path.join(staging_dir_name,"*.csv")  # to get list of csv files
valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for file_name in glob.glob(glob_dir):
    #fn = os.path.join(staging_dir_name, file_name)
    in_fp = open(file_name, "rt", encoding = 'cp1252') #in_fp is input file , rt is read text
    input_data = in_fp.read()
    input_data = input_data.replace('"', '').replace(' ', '_').replace('-','_').replace('%','pct').replace('/','_').lower().replace('''""''', '_')
    in_fp.close()
    
    
    ofn = file_name + "modified"
    out_fp = open(ofn, "wt", encoding = 'utf-8') #in_fp is input file , rt is read text      
    for c in input_data:
        if c!= '\0':
            out_fp.write(c)
    out_fp.close()
    
glob_dir = os.path.join(staging_dir_name,"*.csvmodified")

conn = sqlite3.connect("medicare_hospital_compare.db") #connection to open db, if the db doesn't exist it creates a new one.
conn.text_factory = str
c1 = conn.cursor()  # Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands

for csvfile in glob.glob(glob_dir):
    # remove the path and extension and use what's left as a table name
    tablename = os.path.splitext(os.path.basename(csvfile))[0]
    tablename = tablename.replace(' ', '_').replace('-','_').replace('%','pct').replace('/','_').lower().replace('''""''', '_')
    if tablename[0] not in valid_characters:
        tablename = "t_"+ tablename
    print(csvfile)
    print(tablename)
 
    with open(csvfile, "r") as f:
        reader = csv.reader(f, delimiter=',', skipinitialspace=True)
 
        header = True
        for row in reader:
            if header:
                # gather column names from the first row of the csv
                header = False
 
                sql = "DROP TABLE IF EXISTS '" + tablename + "'"
                c1.execute(sql)
                sql = "CREATE TABLE " + tablename + "(" + ",".join(column+ " text" for column in row) + ")"
        
                c1.execute(sql)
 
               
 
                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename,
                            ", ".join([ "?" for column in row ]))
 
                rowlen = len(row)
            else:
                # skip lines that don't have the right number of columns
                if len(row) == rowlen:
                    c1.execute(insertsql, row)
 
        conn.commit()
 
c1.close()
conn.close()

