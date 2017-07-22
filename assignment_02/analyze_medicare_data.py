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

staging_dir_name = "staging" #directory name

os.mkdir(staging_dir_name)  # mkdir will make the directory if it doesn't exist in the path

zip_file_name = os.path.join(staging_dir_name, "Hospital_Data.zip") # Zip file will be created in the mentioned Staging path

zf = open(zip_file_name, "wb") # The wb indicates that the file is opened for writing in binary mode. On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.

zf.write(r.content) # writes the entire content in the url to the zip file

zf.close() # closes the file

z = zipfile.ZipFile(zip_file_name,'r') # Open a ZIP file, where file can be either a path to a file (a string) or a file-like object. The mode parameter should be 'r' to read an existing file, 'w' to truncate and write a new file, or 'a' to append to an existing file.

z.extractall(staging_dir_name) #extracts all the files in staging

z.close()

# Step2 : Create a SQLite DB to fill the data

glob_dir = os.path.join(staging_dir_name,"*.csv")  # to get list of csv files
valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
conn = sqlite3.connect("medicare_hospital_compare.db") #connection to open db, if the db doesn't exist it creates a new one.
conn.text_factory = str
c1 = conn.cursor()  # Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands

for file_name in glob.glob(glob_dir):
    tablename = os.path.splitext(os.path.basename(file_name))[0] # remove the path and extension and use what's left as a table name
    if not(tablename == "FY2015_Percent_Change_in_Medicare_Payments"):  #removing the corrupt file from iterations
    
        tablename = tablename.replace(' ', '_').replace('-','_').replace('%','pct').replace('/','_').lower().replace('''""''', '_')
        if tablename[0] not in valid_characters:   #cross-checking the first letter of tablename to be in valid_characters
            tablename = "t_"+ tablename
    
        with open(file_name, "rt", encoding = 'cp1252') as f:
            reader = csv.reader(f, delimiter=',', skipinitialspace=True)
            header = next(reader)  #takes the first row as header
            header = ','.join(header)
            header = header.replace('"', '').replace(' ', '_').replace('-','_').replace('%','pct').replace('/','_').lower().replace('''""''', '_')   
            header = header.split(',')
            header = [x if x[0] in valid_characters else 'c_'+ x for x in header]
            #checking for existing tablenames and create tables
            sql = "DROP TABLE IF EXISTS '" + tablename + "'"
            c1.execute(sql)
            sql = "CREATE TABLE " + tablename + "(" + ",".join(column+ " text" for column in header) + ")"
            c1.execute(sql)
            #inserting values in created tables using the other data after stripping the header
            for row in reader:
                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename,
                                               ", ".join([ "?" for column in row ]))
                if len(row) != 1:           #if the end of the file has blank rows, the insert query fails because blank values cannot be put into all columns
                    c1.execute(insertsql, row)
                    
        conn.commit()

c1.close()
conn.close()
    
    
    
    
    
    
    
    
    