# Third Assignment

from __future__ import print_function
import requests # for sending Http requests 
import pandas as pd #pandas to create dataframes


# Step1 : Downloading and Extracting txt  training file

url = "http://kevincrook.com/utd/market_basket_training.txt"

r = requests.get(url) # this will connect to the url

f = open("market_basket_training.txt", "wb") # The wb indicates that the file is opened for writing in binary mode. On Unix systems (Linux, Mac OS X, etc.), binary mode does nothing - they treat text files the same way that any other files are treated. On Windows, however, text files are written with slightly modified line endings. This causes a serious problem when dealing with actual binary files, like exe or jpg files. Therefore, when opening files which are not supposed to be text, even in Unix, you should use wb or rb. Use plain w or r only for text files.

f.write(r.content) # writes the entire content in the url to the zip file

f.close() # closes the file

def read_data(file_name):
    #"""Read a file that lists possible transactions"""
    result = list()
    with open(file_name, 'r') as file_reader:
        for line in file_reader:
            order_set = list(line.strip().split(','))
            order_set = order_set[1:]
            result.append(order_set)
    return result

training_data = read_data("market_basket_training.txt")  # data stored in a list
    
products = [tuple(x) for x in training_data]  # changing each row into tuples

column_names = ['a', 'b', 'c', 'd']  #names of columns for dataframe

df = pd.DataFrame(products, columns = column_names)  # creating dataframe


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
        data = pd.DataFrame(df[df['c'].isnull()]) #getting rows which have data only in the first 2 columns
        data2 = pd.DataFrame(data.ix[:,:'b'])
        data2['Period'] = data2.a.astype(str).str.cat(data2.b.astype(str), sep=',') # creating a new column with combination of another product
        new_data = pd.DataFrame(data2['Period'])
        new_data = new_data[new_data['Period'].str.contains(test[0], na=False)]
        recomm = new_data.groupby('Period').size().idxmax()
        final_reco = list(set(recomm.split(',')) - set(test))
        return final_reco[0]
    
    if len(test) ==2:
        data = pd.DataFrame(df[~(df['c'].isnull()) & (df['d'].isnull())]) #getting rows which have data only in the first 3 columns
        data2 = pd.DataFrame(data.ix[:,:'c'])
        recomm = data2[((data2['a']== test[0]) | (data2['b'] == test[0]))&((data2['b']== test[1]) | (data2['c'] == test[1]))].groupby(['a','b','c']).size().idxmax()
        final_reco = list(set(recomm) - set(test))  #after getting the set of max count, subtracting the test products to get the recommended product
        return final_reco[0]
    
    if len(test) ==3:
        data = pd.DataFrame(df[~(df['d'].isnull())])  #get the rows which do not have null values in the 4th column
        recomm = data[((data['a']== test[0]) | (data['b'] == test[0]))&((data['b']== test[1]) | (data['c'] == test[1]))&((data['c']== test[2]) | (data['d'] == test[2]))].groupby(['a','b','c','d']).size().idxmax()
        final_reco = list(set(recomm) - set(test))
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
