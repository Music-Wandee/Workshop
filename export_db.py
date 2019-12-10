from pymongo import MongoClient
import json
def export_db(host, db_name, col_name, file_name):
    '''
    host = 'mongodb://localhost:27017/'
    db_name = 'phase1'
    col_name = 'owner_post'
    '''
    
    client = MongoClient(host)
    
    # Access database
    mydb = client[db_name]
    
    # Access collection
    mycol = mydb[col_name]   
       
    cursor = mycol.find({}) 
    json_db = '['
    for document in cursor:
        #https://bugs.python.org/issue13769 
        json_db = json_db + json.dumps(document, ensure_ascii=False) + ','
        
    json_db = json_db[:-1]
    json_db = json_db + ']'
         
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(json_db)
    mydb.logout()
