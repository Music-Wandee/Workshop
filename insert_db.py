from pymongo import MongoClient
def insert_db(host, db_name, col_name, data_dict):
    
    duplicate_data = list()
    status = True
    
    try:
        # Connect database
        client = MongoClient(host)
        # Access database
        mydb = client[db_name]
        # Access collection
        mycol = mydb[col_name]
        
        # Check if the data is list or one dictionary
        if isinstance(data_dict, list):
            # Chcek if the database is empty
            if mycol.count() == 0:
                mycol.insert_many(data_dict)
            else:    
                for data in data_dict:
                    # Check duplicate data
                    if mycol.find_one({"_id": data_dict['_id']}) is None:
                        mycol.insert_one(data_dict)
                    else:
                        duplicate_data.append(data_dict)
        else:      
            if mycol.find_one({"_id": data_dict['_id']}) is None:
                mycol.insert_one(data_dict)
            else:
                duplicate_data.append(data_dict)
    except:
        status = False
        mydb.logout()
            
    mydb.logout()
    
    result = dict()
    result['status'] = status
    result['duplicate'] = duplicate_data

    return result