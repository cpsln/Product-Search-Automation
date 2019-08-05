from pymongo import MongoClient

# myclient=MongoClient('mongodb+srv://illmf:azsxdc12#@cluster0-oobsq.mongodb.net/test') 
myclient=MongoClient('mongodb://localhost:27017/')

print("Opened database successfully")
print("Opened database successfully")

mydb=myclient['SHOP']

category=mydb['Category']   
product=mydb['Product']
# addcart=mydb['addCart']                                                                          

print("DB created successfully")
