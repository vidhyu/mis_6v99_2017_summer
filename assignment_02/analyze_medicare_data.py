#Assignment02

import requests
import os
import zipfile
import openpyxl #delete xl files
import sqlite3 #for sqlite
import glob
import getpass

url = "https://data.medicare.gov/views/bg9k-emty/files/0a9879e0-3312-4719-a1db-39fd114890f1?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip"

r = requests.get(url)

staging_dir_name = "staging"
os.mkdir(staging_dir_name)

zip_file_name = os.path.join(staging_dir_name, "Hospital_Data.zip")

zf = open(zip_file_name, "wb")

zf.write(r.content)

zf.close()

z = zipfile.ZipFile(zip_file_name,'r')
z.extractall(staging_dir_name)
z.close()

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


conn = sqlite3.connect("test.db") #connection to open db, if the db doesn't exist it creates a new one.

c1 = conn.cursor()

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











