from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

def pantip_crawling(url):
    topic_num = url.split("/")
    topic_num = topic_num[-1]

    # specify the url
    # url = 'https://pantip.com/topic/38478051'
    
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    
    # initialize the driver
    driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe", options=options)
    driver.get(url)
    
    try:
        cookie = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.pt-snackbar__actions.pt-action-policy")))
        cookie.click()
    except TimeoutException as ex:
        print("There is not the pop up")
    
    # Click to load page
    loadPage = True
    while loadPage:
        try:        
            load_comment_buttons = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.bar-paging-ed span.focus-txt")))
            driver.execute_script("return arguments[0].scrollIntoView({block: \"center\", inline: \"center\"});", load_comment_buttons)
            load_comment_buttons.click()
        except TimeoutException as ex:
            loadPage = False
    
    
    # Click to see reply
    try:
        comment_buttons = WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.reply.see-more span.focus-txt")))    
        for button in comment_buttons:
            driver.execute_script("return arguments[0].scrollIntoView({block: \"center\", inline: \"center\"});", button)
            button.click()
    except:       
        comment_buttons = ''
    
    
    # Click to see addional reply
    if comment_buttons != '':
        loadButton = True   
        while loadButton:    
            try:
               load_comment_buttons = WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.load-reply-next span.focus-txt"))) 
               for button in load_comment_buttons:
                   driver.execute_script("return arguments[0].scrollIntoView({block: \"center\", inline: \"center\"});", button)
                   button.click()
            except:
                loadButton = False
    
    
    
    # extract html
    content = driver.page_source
    soup = BeautifulSoup(content,'lxml')

    driver.close()
    
     # Extract main post informaiton
    all_comment = list()
    
    
    # Get owner post
    main_area = soup.find(class_ = 'main-post-inner sticky-navi-comment')
    title = main_area.find(class_ = 'display-post-title').get_text().strip()
    

    # Get rid of edit-history
    edit_history = main_area.find('div', class_ = 'edit-history')
    if edit_history is not None:
        edit_history.decompose()
    

    main = {      
            '_id' : topic_num + '0',
            'url': url,
            'title': title,
            'post' : main_area.find(class_ = 'display-post-story').get_text().strip(),
            'post_number' : '0',
            'owner' : main_area.find(class_ = 'display-post-name owner').get_text().strip(),
            'time' : main_area.find(class_ = 'timeago')['data-utime']
            }
    all_comment.append(main)
    
    # Get all replies
    for div in soup.find_all("div", id = re.compile("^(comment|reply)-[0-9]+")):

        # Get rid of edit-history
        edit_history = div.find('div', class_ = 'edit-history')
        if edit_history is not None:
            edit_history.decompose()
            
        # Extract information
        post = div.find(class_ = 'display-post-story').get_text().strip()
        if len(post) > 0:
            if post.find('ความคิดเห็นนี้ถูกลบเนื่องจาก') == -1:
                post_number = div.find(class_ = 'display-post-number').get_text().strip().split()[1]
                reply ={
                        '_id' : topic_num + post_number,
                        'url': url,
                        'title': title,
                        'post' : post,
                        'post_number' : post_number,
                        'owner' : div.find(class_ = 'display-post-name').get_text().strip(),
                        'time' : div.find(class_ = 'timeago')['data-utime']
                        }
                all_comment.append(reply)
 
    return all_comment