import requests
from apikey import *
api_add =  'https://newsapi.org/v2/top-headlines?country=us&apiKey='+api_key
json_data =requests.get(api_add).json()

alldata = []
def new_s():
    for i in range(3):
        alldata.append('Number '+str(i+1)+', '+ json_data['articles'][i]['title']+'.')
    return alldata
# a = new_s()
# print(a)    