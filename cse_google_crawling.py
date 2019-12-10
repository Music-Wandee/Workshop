# Reference https://www.simplifiedpython.net/google-custom-search-api-python/
# https://developers.google.com/custom-search/docs/overview?hl=th
# https://developers.google.com/custom-search/v1/cse/list
from googleapiclient.discovery import build
import re
#link = cse_google_crawling('\"กินดี\" after:2017-12-31 before:2019-1-1', 40)
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    
    if 'items' in res.keys():
        return res['items']
    else:
        return []

def cse_google_crawling(keyword, num_link):
    
    my_api_key = "AIzaSyB0IQLZSWV7iBYUc7tnrG2Nu6R7iNforMQ"
    my_cse_id = "001218037654599568255:526j1dfzayy"
    
    linklist = list()
    index = 1
    while(len(linklist) < num_link):
        
        results = list()
        results = google_search(keyword, my_api_key, my_cse_id, start = index)
        
        if len(results) == 0:
            print('Total links '+str(len(linklist)))
            return linklist
        
        for page_info in results:
            url = page_info['link']
            if re.search("^https://pantip.com/topic/[0-9]+", url):
                # check duplicate
                if url not in linklist:
                    linklist.append(url)

        index += len(results)
    
    linklist = linklist[:num_link]
    print('Total links '+str(len(linklist)))
    return linklist