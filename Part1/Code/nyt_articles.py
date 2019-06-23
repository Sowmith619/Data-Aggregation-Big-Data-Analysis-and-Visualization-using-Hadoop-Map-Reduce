#Import libraries
import requests
from bs4 import BeautifulSoup
import urllib.request,json
import sys
import math

#NY Times search article Api
api_key="3XNf2AuXStd7KRvhqMFedwTw8N3oIwPA"

#Url for the NY Times article search
s="https://api.nytimes.com/svc/search/v2/articlesearch.json?"


#Specifying the time frame
#Change these accordingly.Format: yyyymmdd
begin_date="20190316"
end_date="20190416"



#Full list of terms
queryTerms=["soccer","americanfootball","nba","baseball","softball","wrestling","wwe"]
for query in queryTerms:
    # URL that takes above parameters
    print(query)
    inurl=s+"begin_date="+begin_date+"&end_date="+end_date+"&facet=true&q="+query+"&api-key="+api_key
    data=urllib.request.urlopen(inurl)
    response = json.load(data)['response']
    hits = response['meta']['hits']
    pages=math.ceil(hits/10)
    print(pages)
    for page in range(1,pages+1):
       # print(page)
        inurl=s+"begin_date="+begin_date+"&end_date="+end_date+"&page="+str(page)+"&facet=true&q="+query+"&api-key="+api_key
        data=urllib.request.urlopen(inurl)
        response = json.load(data)['response']
        docs=response['docs']
        i=0;
        for d in docs:
            i=i+1;
            url=d['web_url']
            try:
                resp = requests.get(url)
                soup = BeautifulSoup(resp.text, 'lxml')
                paragraphs = soup.find_all('p')
                paras=""
                for p in paragraphs:
                    paras = paras + p.get_text()
                    #writing the files into each folder
                with open(query+"_"+str(page)+"_"+str(i)+".txt", 'w') as outfile:  
                    outfile.write(paras)
            except:
                continue
    
    
    

