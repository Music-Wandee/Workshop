# data_preparation    
import string
import json
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import stopwords

def read_file(file_name):
    with open(file_name, 'r', encoding = 'utf8') as file:
        text = file.readlines()
    return text

def write_file(file_name, data):    
    with open('data_set.txt', 'w', encoding='utf8') as file:
        for header in data:
            file.write(header)
            file.write('\n')

def remove_punc(data_set):
    # Get punctuation
    punc_list = list()
    for c in string.punctuation:
        punc_list.append(c)
    
    # Remove punctuation
    for idx in range(len(data_set)):
        for punc in punc_list:
            data_set[idx] = data_set[idx].replace(punc, '')
    return data_set

def tokenize(data):
    seperated_data = list()
    for text in data:
        txt = word_tokenize(text, engine='newmm')
        seperated_data.append(txt)
    return seperated_data

def remove_space(data):
    modified_data = list()
    for text_list in data:
        #data = [word for word in text_list if word.strip() != '']
        new_list = list()
        for word in text_list:
            if word.strip() != '':
                new_list.append(word) 
        modified_data.append(new_list)
        
    return modified_data
    

def remove_stopwords(data):
    # Get stopwords
    # Add stopwords "C:\Users\user\Anaconda3\Lib\site-packages\pythainlp\corpus\stopwords-th.txt"
    sw = stopwords.words('thai')
    # Remove stopwords
    modified_data = list()
    for text in data:
        modified_list = list()
        for word in text:
            if word not in sw:
                modified_list.append(word)
        modified_data.append(modified_list)
    return modified_data


def json_write(file_name ,data_dict):
    data_json = json.dumps(data_dict, ensure_ascii=False)
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(data_json)


def json_read(file_name): 
    try:
        with open(file_name, 'r', encoding = 'utf8') as json_file:
            data = json.load(json_file)
    except:
        data = ''
        print("Cannot read "+ file_name + '.json')
    return data


# Read dataset
file_name = 'data_set.txt'
data = read_file(file_name)

# Remove punctuation
data = remove_punc(data)

# Tokenize data
tokenized_data = tokenize(data)

# Remove white spaces
tokenized_data = remove_space(tokenized_data)

# Remove stopwords
tokenized_data = remove_stopwords(tokenized_data)

'''
# Save data
data_dict = {'data':tokenized_data}
json_write('tokenized_data.json', data_dict)

# read data
tokenized_data = json_read('tokenized_data.json')
'''