# selenium installation
# pip install -U selenium

# Tutorial of BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Tutorial of Regular Expression
# https://www.w3schools.com/python/python_regex.asp

from bs4 import BeautifulSoup
from selenium import webdriver
import re
    
options = webdriver.ChromeOptions()
#options.add_argument('headless')

# define url
url = 'https://pantip.com/topic/39384671'

# initialize the driver
driver = webdriver.Chrome(executable_path = "C:\webdriver\chromedriver.exe", options = options)
driver.get(url)

# Get html
content = driver.page_source
soup = BeautifulSoup(content,'lxml')

# Searching by CSS class
main_area = soup.find('div', class_ = 'display-post-wrapper main-post type')


# Get title
title = main_area.find('h2' ,class_ = 'display-post-title').get_text()
print(title)

# Get main post
main_post = main_area.find('div' ,class_ = 'display-post-story').get_text()
print(main_post)

# Remove edit history
main_post = main_area.find('div', class_ = 'display-post-story')
edit_history = main_post.find('div', class_ = 'edit-history')
if edit_history is not None:
    edit_history.decompose()
    
main_post = main_post.get_text()
print(main_post)

# Get post owner
owner = main_area.find('a', class_ = 'display-post-name owner').get_text()
print(owner)

# Get time
time = main_area.find('abbr',class_ = 'timeago')
time = time['data-utime']
print(time)


# Get sub posts
all_comment = list()
sub_post = soup.find_all("div", id = re.compile("^comment-[0-9]+"))
for div in sub_post:
    if len(div.get_text().strip()) > 1:
        post = div.find(class_ = 'display-post-story').get_text().strip()
        if post.find('ความคิดเห็นนี้ถูกลบเนื่องจาก') == -1:
            reply ={
                    'post' : post,
                    'post_number' : div.find(class_ = 'display-post-number').get_text().strip(),
                    'post_owner' : div.find(class_ = 'display-post-name').get_text().strip(),
                    'time' : div.find(class_ = 'timeago').get_text().strip()
                    }
            all_comment.append(reply)

all_comment[:3]
driver.close()