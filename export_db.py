from pymongo import MongoClient
import json
def export_db(host, db_name, col_name, file_name):
    '''
    host = 'mongodb://localhost:27017/'
    db_name = 'phase1'
    col_name = 'owner_post'
    '''
    status = True
    try:
        client = MongoClient(host)
        
        # Access database
        mydb = client[db_name]
        
        # Access collection
        mycol = mydb[col_name]   
           
        cursor = mycol.find({}) 
        json_db = '['
        for document in cursor:
            #convert to json https://www.w3schools.com/python/showpython.asp?filename=demo_json_from_python
            #json file structure https://www.journaldev.com/33302/python-pretty-print-json 
            #issue about ensure_ascii=False https://bugs.python.org/issue13769 
            json_db = json_db + json.dumps(document, ensure_ascii=False) + ','
            
        json_db = json_db[:-1]
        json_db = json_db + ']'
             
        with open(file_name, 'w', encoding='utf8') as file:
            file.write(json_db)
    except:
        status = False
        mydb.logout()
        
    mydb.logout()
    
    return status
