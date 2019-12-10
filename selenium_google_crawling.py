from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import re
#link = selenium_google_crawling('กินดี site:pantip.com',43)
def selenium_google_crawling(keyword, num_link):
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    # define url
    url = 'https://www.google.com/'
    
    # initialize the driver
    driver = webdriver.Chrome(executable_path = "C:\webdriver\chromedriver.exe", options = options)
    driver.get(url)
    
    #keyword = 'กินดี site:pantip.com'
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(keyword)
    search_box.submit()

    linklist = list()
    while(len(linklist) < num_link):

        # Get html
        content = driver.page_source
        soup = BeautifulSoup(content,'lxml')
        
        # Get section of organic results
        organic_results = soup.find_all('div', class_='srg')
        
        
        for section in organic_results:
            all_link = section.find_all('a')
            for link in all_link:
                url = link['href']
                if re.search("^https://pantip.com/topic/[0-9]+", url):
                    if url not in linklist:
                        linklist.append(url)
                    
        if len(linklist) < num_link:
            try:
                nextpage = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "pnnext")))
                driver.execute_script("return arguments[0].scrollIntoView({block: \"center\", inline: \"center\"});", nextpage)
                nextpage.click()
                
            except TimeoutException as ex: 
                print('Cannot click the next page')
                print('total links '+ str(len(linklist)))
                driver.close()
                return linklist
            
    driver.close()
    linklist = linklist[:num_link]
    print('total links '+ str(len(linklist)))
    return linklist