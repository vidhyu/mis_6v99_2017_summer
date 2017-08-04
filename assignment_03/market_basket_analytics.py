# Third Assignment

from __future__ import print_function
import requests # for sending Http requests 
import pandas as pd


# Step1 : Downloading and Extracting txt  training file

url = "http://kevincrook.com/utd/market_basket_training.txt"

r = requests.get(url) # this will connect to the url

f = open("market_basket_training.txt", "wb") # The wb indicates that the file is opened for writing in binary mode. On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.

f.write(r.content) # writes the entire content in the url to the zip file

f.close() # closes the file

def read_data(file_name):
    """Read a file that lists possible transactions"""
    result = list()
    with open(file_name, 'r') as file_reader:
        for line in file_reader:
            order_set = list(line.strip().split(','))
            order_set = order_set[1:]
            result.append(order_set)
    return result

training_data = read_data("market_basket_training.txt")
    
products = [tuple(x) for x in training_data]

column_names = ['a', 'b', 'c', 'd']

df = pd.DataFrame(products, columns = column_names)


# Step2 : Downloading and Extracting txt for test file

url = "http://kevincrook.com/utd/market_basket_test.txt"

r = requests.get(url) # this will connect to the url

f = open("market_basket_test.txt", "wb") # The wb indicates that the file is opened for writing in binary mode. On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.

f.write(r.content) # writes the entire content in the url to the zip file

f.close() # closes the file

test_data = read_data("market_basket_test.txt")

    
test_products = [list(x) for x in test_data]


# Step3 : Create recommendation file

def recommended_product(test):
    if len(test) ==1:
        data = pd.DataFrame(df[df['c'].isnull()])
        data2 = pd.DataFrame(data.ix[:,:'b'])
        data2['Period'] = data2.a.astype(str).str.cat(data2.b.astype(str), sep=',')
        new_data = pd.DataFrame(data2['Period'])
        new_data = new_data[new_data['Period'].str.contains(test[0], na=False)]
        recomm = new_data.groupby('Period').size().idxmax()
        final_reco = list(set(recomm.split(',')) - set(test))
        return final_reco[0]
    
    if len(test) ==2:
        data = pd.DataFrame(df[~(df['c'].isnull()) & (df['d'].isnull())])
        data2 = pd.DataFrame(data.ix[:,:'c'])
        data2['Period'] = data2.a.astype(str).str.cat(data2.b.astype(str), sep=',').str.cat(data2.c.astype(str), sep=',')
        new_data = pd.DataFrame(data2['Period'])
        new_data = new_data[new_data['Period'].str.contains(','.join(test), na=False)]
        recomm = new_data.groupby('Period').size().idxmax()
        final_reco = list(set(recomm.split(',')) - set(test))
        return final_reco[0]
    
    if len(test) ==3:
        data = pd.DataFrame(df[~(df['d'].isnull())])
        data['Period'] = data.a.astype(str).str.cat(data.b.astype(str), sep=',').str.cat(data.c.astype(str), sep=',').str.cat(data.d.astype(str), sep=',')
        new_data = pd.DataFrame(data['Period'])
        new_data = new_data[new_data['Period'].str.contains(','.join(test), na=False)]
        recomm = new_data.groupby('Period').size().idxmax()
        final_reco = list(set(recomm.split(',')) - set(test))
        return final_reco[0]
        




# Step4 : Print recommendation file

fn = 'market_basket_recommendations.txt' # file name
num = 1
with open(fn,'w') as f:   # opening the file name as write
    for row in test_products:
        #row.discard('P04')
        #row.discard('P08')
        try:
            row.remove('P04')
           
        except ValueError:
            pass  # do nothing!
            
        try:
            row.remove('P08')
        except ValueError:
            pass  # do nothing!
        print("%03d"%num +","+recommended_product(row), file=f)
        num += 1
