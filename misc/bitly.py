import base64 
import requests
import json 
import logging

credentials = 'sportpursuit:bentley123'

def getShortURLs(urls):
	token = auth()
	return shortenURLs(token, urls)

def auth():
	base_auth = "https://api-ssl.bitly.com/oauth/access_token"
	headers = {'Authorization': 'Basic ' + base64.b64encode(credentials)}
	resp = requests.post(base_auth, headers=headers)
	return resp.content

def removeLastChar(long_url):
	return long_url[:-1]

def shortenURLs(token, long_urls):
	base = 'https://api-ssl.bitly.com/v3/shorten'
	short_urls = []
	for long_url in long_urls:
		if long_url:
			long_url = removeLastChar(long_url)
			params = {'access_token':token, 'longUrl' : 'https://' + long_url}
			logging.error(long_url)
			response = requests.get(base, params=params)
			logging.error(response.request.url)
			r = json.loads(response.content)
			logging.error(r)

			short_urls.append(r['data']['url'])
	return short_urls
