import json
def json_read(file_name): 
    try:
        with open(file_name, 'r', encoding = 'utf8') as json_file:
            data = json.load(json_file)
    except:
        data = ''
        print("Cannot read "+ file_name + '.json')
        
    return data