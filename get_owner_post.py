from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def get_owner_post(url):
    # specify the url
    topic_num = url.split("/")
    topic_num = topic_num[-1]
    
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    
    # initialize the driver
    driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe", options=options)
    driver.get(url)
    '''
    try:
        cookie = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.pt-snackbar__actions.pt-action-policy")))
        cookie.click()
    except TimeoutException as ex:
        print("There is not the pop up")
     '''   
    # extract html
    content = driver.page_source
    soup = BeautifulSoup(content,'lxml')
    
    try:
        main_area = soup.find('div', class_ = 'main-post-inner sticky-navi-comment')
    except TimeoutException as ex:
        print("cannot find the element")

    # Get rid of edit-history
    try:
        edit_history = main_area.find('div', class_ = 'edit-history')
        if edit_history is not None:
            edit_history.decompose()
    except TimeoutException as ex:        
        print("cannot find the element")

        

    main = {
            '_id' : topic_num + '0',
            'url': url,
            'title': main_area.find(class_ = 'display-post-title').get_text().strip(),
            'post' : main_area.find(class_ = 'display-post-story').get_text().strip(),
            'post_number' : '0',
            'owner' : main_area.find(class_ = 'display-post-name owner').get_text().strip(),
            'time' : main_area.find(class_ = 'timeago')['data-utime']
            }
    
    driver.close()
    return main