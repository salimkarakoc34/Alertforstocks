import requests

import stocksapi
for y in stocksapi.stocks:
    url=f'https://newsapi.org/v2/everything?q={y}&from=2023-01-06&to=2023-01-06&sortBy=popularity&apiKey=e14eb5320e554238965dad3ba884a14a'
    response = requests.request("GET", url)
    myjson = response.json()
    initial =myjson['articles'][0]['title']
    second =myjson['articles'][0]['description']
    link=myjson['articles'][0]['url']
    message=(f'Breaking News  \n Title : {initial} \n Description : {second} \n More Details: {link}' )
    print(message)