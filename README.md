# Data Aggregation, Big Data Analysis and Visualization using Hadoop Map Reduce

Introduction Sports has been a very important part of our daily lives. The amount of data related to sports on the web is huge. It has a very wide range of sources ranging from personal comments on social media, to blogs and to official websites to live videos. With this wide array of sources we can understand the patterns and can analyze the data. 
 
Implementation In this project the data pipeline has been set up by gathering the information sources. The data has been collected in three ways 
1. Twitter 2. NY Times articles 3. Common Crawl data 
 
Twitter Data Collection To gather the tweets, I used tweepy api of Twitter. I used python script to achieve this. I used tweepy AppAuth Handler to increase the tweet limit. Then I used the following search queries for Tweet Collection 
1. American football   #americanfootball, #football 
2. Basketball          #basket ball, #nba 
3. Baseball-softball   #softball 
4. Soccer              #soccer, #soccerteam 
5. wresting            #wwe, #wresting. 
The tweets were collected from 16/03/2019 to 17/04/2020 and saved them in a txt file. 
The number of tweets collected were in the range of 40,000. The script extracts the tweet’s text and stores them into a txt file. 
 
NY Times data Collection 
 
To gather the articles, I used the API provided by NY Times. I used python script to retrieve the articles content. I collected the data in 2 phases. 
Phase 1: Begin date = 20190316 
 End data = 20190331 
Phase 2: Begin date = 20190401 
 End date = 20190418 

The search terms included were the following ["americanfootball", "football","nba","softball","soccer", "wwe", "#wresting"] 
We used urlib request of python to hit the NY Times search article api, and fetched the result from the corresponding url and then from the docs. BeautifulSoup library is used to extract the paragraph content. Then that data has been send to the file to written to the text file. 
 
Common Crawl Data Collection 
 
Common Crawl the data has been extracted by using the CC News article. The data is available on AWS S3 in the commoncrawl bucket at /crawl-data/CC-NEWS/. Then using this command 
aws s3 ls --recursive s3://commoncrawl/crawl-data/CC-NEWS/ 
The listed WARC files are extracted using the AWS Command Line Interface then the WARC file that I used is the        s3://commoncrawl/crawl-data/CC-NEWS/2016/09/CC-NEWS-20190419211809-00000.warc.gz 
In the next step we extracted the warc file and then we iterated through the entire the entire urls of the warc file. I used requests.get(link) to hit the url and then used BeautifulSoup and then I iterated through the text to find any keywords and stored the url’s which provided me the best result. 
In the second step, I iterated through that url’s and fetched the result of the paragraph content from the url’s I above collected and stored them in a CSV file. 
