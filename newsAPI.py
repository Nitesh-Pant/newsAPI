import requests
import pprint

url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
# url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=YOUR-KEY"
urll = requests.get(url).json()
article = urll["articles"]
count = 1
for i in article:
    print(count," Title: ",i["title"]) 
    print("    Descrition: ",i["description"])
    print("    Url: ",i["url"])
    count += 1