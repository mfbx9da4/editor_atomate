"""
Words post and link are used interchangably. An fb Link object is a type of post. 
"""


import requests
import logging
import json 



def translateRowToData(header, row):
	cols = row.split('\t')
	result = {}
	for i in range(len(cols)):
		result[header[i]] = cols[i]
	return result

def postUnpublishedPost(access_token, link_data):
	feed = "https://graph.facebook.com/192003130834820/feed"
	static_data = {
	'published' : 'false',
	'access_token' : access_token,
	}
	link_data.update(static_data)
	resp = requests.post(feed, data=link_data)
	jso = json.loads(resp.content)
	if jso.get('error'):
		post_id = jso.get('error')
	else:
		post_id = jso.get('id').split('_')[-1]
	return post_id


# data = """URL	Post text	Link Headline	Link Caption	Description	Picture
# www.sportpursuit.com/deals/craghoppers_sale/1208?utm_medium=cpc&utm_source=facebook&st=FacebookPPC&ad=facebook&utm_campaign=adt-Ppost$t-Brand$b-Craghoppers$s-SportLifestyle$d-Desktop$tar-InLookR$bt-cpc$g-F$loc-A$age-20-45	Get your hands on up to 75% off Craghoppers Clothing for one week only! http://prsu.it/1eYVBrb                          Join thousands of others finding great deals on sports brands at SportPursuit.	Join SportPursuit for Free!	www.sportpursuit.com	SportPursuit is a growing community of sports enthusiasts exploring and discovering great deals on sports brands at up to 70% off.	http://content.sportpursuit.com/media/catalog/product/cache/1/small_image/298x/9df78eab33525d08d6e5fb8d27136e95/z/c/zcww1040_cerise.jpg
# www.sportpursuit.com/deals/craghoppers_sale/1208?utm_medium=cpc&utm_source=facebook&st=FacebookPPC&ad=facebook&utm_campaign=adt-Ppost$t-Brand$b-Craghoppers$s-SportLifestyle$d-Desktop$tar-InLookR$bt-cpc$g-F$loc-B$age-20-45	Get your hands on up to 75% off Craghoppers Clothing for one week only! http://prsu.it/18HYPG1                          Join thousands of others finding great deals on sports brands at SportPursuit.	Join SportPursuit for Free!	www.sportpursuit.com	SportPursuit is a growing community of sports enthusiasts exploring and discovering great deals on sports brands at up to 70% off.	http://content.sportpursuit.com/media/catalog/product/cache/1/small_image/298x/9df78eab33525d08d6e5fb8d27136e95/z/c/zcww1040_cerise.jpg
# www.sportpursuit.com/deals/craghoppers_sale/1208?utm_medium=cpc&utm_source=facebook&st=FacebookPPC&ad=facebook&utm_campaign=adt-Ppost$t-Brand$b-Craghoppers$s-SportLifestyle$d-Desktop$tar-InLookR$bt-cpc$g-M$loc-A$age-20-45	Get your hands on up to 75% off Craghoppers Clothing for one week only! http://prsu.it/1aQSnRd                          Join thousands of others finding great deals on sports brands at SportPursuit.	Join SportPursuit for Free!	www.sportpursuit.com	SportPursuit is a growing community of sports enthusiasts exploring and discovering great deals on sports brands at up to 70% off.	http://content.sportpursuit.com/media/catalog/product/cache/1/small_image/298x/9df78eab33525d08d6e5fb8d27136e95/z/c/zcmw660_red_pepper.jpg
# www.sportpursuit.com/deals/craghoppers_sale/1208?utm_medium=cpc&utm_source=facebook&st=FacebookPPC&ad=facebook&utm_campaign=adt-Ppost$t-Brand$b-Craghoppers$s-SportLifestyle$d-Desktop$tar-InLookR$bt-cpc$g-M$loc-B$age-20-45	Get your hands on up to 75% off Craghoppers Clothing for one week only! http://prsu.it/1eYVEmC                          Join thousands of others finding great deals on sports brands at SportPursuit.	Join SportPursuit for Free!	www.sportpursuit.com	SportPursuit is a growing community of sports enthusiasts exploring and discovering great deals on sports brands at up to 70% off.	http://content.sportpursuit.com/media/catalog/product/cache/1/small_image/298x/9df78eab33525d08d6e5fb8d27136e95/z/c/zcmw660_red_pepper.jpg"""


def postUnpublishedPosts(access_token, data):
	map_data_to_post = {
		'URL' : 'link',
		'Post text' : 'message',
		'Link Headline': 'name',
		'Link Caption': 'caption',
		'Description' : 'description',
		'Description' : 'description',
		'Picture' : 'picture',
		'Picture\r' : 'picture',
	}
	postIds = []
	all_rows = data.split('\n')
	header = all_rows[0].split('\t')
	header = [map_data_to_post[x] for x in header]
	rows = all_rows[1:]
	for row in rows:
		logging.error(row)
		if row:
			link_data = translateRowToData(header, row)
			postIds.append(postUnpublishedPost(access_token, link_data))
	logging.error(postIds)
	return postIds

