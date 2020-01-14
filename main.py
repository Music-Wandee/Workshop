from pantip_crawling import pantip_crawling
from selenium_google_crawling import selenium_google_crawling
from cse_google_crawling import cse_google_crawling
from get_owner_post import get_owner_post
from insert_db import insert_db
from export_db import export_db
from json_read import json_read
from discriminate_data import discriminate_data 
from pymongo import MongoClient

'''
d = {"id": "393974830", 
     "keyword": "เรียนพิเศษ", 
     "title": "ถ้ามีลูกแล้วไม่ส่งเรียนพิเศษอะไรเลย", 
     "post": "สงสัยว่าสมัยนี้ถ้ามีลูกแล้วเราไม่ส่งเรียนพิเศษอะไรเลย จะเป็นอะไรไหมครับ", 
     "owner": "สมาชิกหมายเลข 5516677", 
     "date": "20 มกราคม เวลา 23:28 น."}

url = 'https://pantip.com/topic/38478051'


data = pantip_crawling('https://pantip.com/topic/37395992')
'''

keyword = ['อยู่ดี', 'เงินเดือน']
time = ' after:2017-12-31 before:2019-1-1'
num_link = 5

data_ower = list()
for key in keyword:
    # Get links from google
    linklist = cse_google_crawling(key+time, num_link)
    for url in linklist:
        # Get owner post infomation
        post_info = get_owner_post(url)       
        if post_info['post'] != '':
            post_info['keyword'] = key
            data_ower.append(post_info)

# Database information      
host = 'mongodb://localhost:27017/'
db_name = 'phase1'
col_name = 'owner_post'

# Insert data for lebeling
result = insert_db(host, db_name, col_name, data_ower)
result = export_db(host, db_name, col_name, 'pantip.json')

# Labeling data Enter the site below
# https://www.lighttag.io/

# Read the result from labeled data
labeled_data = json_read(r"database\phase1_annotations.json")

# Discriminate data after labeling
labeled_data = discriminate_data(labeled_data)

# Insert data
host = 'mongodb://localhost:27017/'
db_name = 'phase1'
col_name = 'relevant_data'
result = insert_db(host, db_name, col_name, labeled_data['relevant'])

#################################### Phase 2 ###########################################

all_posts = list()
for post in labeled_data['relevant']:
    url = post['url']
    data = pantip_crawling(url)
    if data != []:
        all_posts = all_posts + data
        
        
db_name = 'phase1'
col_name = 'filtered_data'
result = insert_db(host, db_name, col_name, all_posts)


    
