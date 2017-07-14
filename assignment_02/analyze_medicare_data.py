#Assignment02

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

conn = sqlite3.connect("medicare_hospital_compare.db") #connection to open db, if the db doesn't exist it creates a new one.

c1 = conn.cursor()  # Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands

glob_dir = os.path.join(staging_dir_name,"*.csv")  # to get list of csv files

for file_name in glob.glob(glob_dir):
    Table_name = os.path.splitext(os.path.basename(file_name))[0]
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile) #Create an object which operates like a regular reader but maps the information read into a dict whose keys are given by the optional fieldnames parameter
        for row in reader:
            print(row['first_name'], row['last_name'])


with open(file_name, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


sql_str = """
create table if not exists my_table(
column_1 text,
column_2 text,
column_3 text
)
"""

c1.execute(sql_str)

sql_str = "insert into my_table(column_1, column_2, column_3) values(?,?,?)"
sql_tuple = ('a','b','c')
c1.execute(sql_str,sql_tuple)


conn.commit() #one commit at end will suffice to load the entire data


fn = os.path.join(staging_dir_name, "Timely and Effective Care - Hospital.csv")
in_fp = open(fn, "rt", encoding = 'cp1252') #in_fp is input file , rt is read text
input_data = in_fp.read()
in_fp.close()

ofn = os.path.join(staging_dir_name, "Timely and Effective Care - Hospital.csv.fix")
out_fp = open(ofn, "wt", encoding = 'utf-8') #in_fp is input file , rt is read text
for c in input_data:
    if c!= '\0':
        out_fp.write(c)
out_fp.close()







k_url = "http://kevincrook.com/utd/hospital_ranking_focus_states.xlsx"

r = requests.get(k_url)

xf = open("hospital_ranking_focus_states.xlsx", "wb")

xf.write(r.content)

xf.close()

wb = openpyxl.load_workbook("hospital_ranking_focus_states.xlsx")

for sheet_name in wb.get_sheet_names():
    print(sheet_name)
    
sheet = wb.get_sheet_by_name("Hospital National Ranking")

i = 1
while sheet.cell(row = i, column = 1).value !=None:
    print(sheet.cell(row = i, column = 1).value, "|", sheet.cell(row = i, column = 2).value)
    i +=1
    
    
sheet2 = wb.get_sheet_by_name("Focus States")

i = 1
while sheet2.cell(row = i, column = 1).value !=None:
    print(sheet2.cell(row = i, column = 1).value, "|", sheet2.cell(row = i, column = 2).value)
    i +=1
    
#creating a workbook
wb2 = openpyxl.Workbook()



sheet_1 = wb2.create_sheet("utd")

sheet_1.cell(row = 1, column = 1, value = "BUAN")

for i in range(2,11):
    sheet_1.cell(row = i, column=1,value = i-1)
    
sheet_2 = wb2.create_sheet("test")

sheet_2.cell(row = 1, column= 2, value = "valued")

for i in range(2,11):
    sheet_2.cell(row = i*2, column=i*2,value = i*2-1)
    
#remove sheet in xl
wb2.remove_sheet(wb2.get_sheet_by_name('Sheet'))

wb2.save("test.xlsx")

wb2.close()

openpyxl.__version__













