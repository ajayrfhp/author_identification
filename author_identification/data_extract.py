import twitter
from keys import *
import re

api = twitter.Api(consumer_key = consumer_key,
                  consumer_secret = consumer_secret,
                  access_token_key = access_token_key,
                  access_token_secret = access_token_secret)

tweet_cnt = 1000
screen_names = ['henrywinter','SamWallaceTel', 'Marcotti', 'GaryLineker','honigstein']


def get_one_stream_per_user(api,screen_name,f,max_id = None):


	re_links_pattern = r'https://[^\s]*'
	tag_pattern = r'@'
	statuses = api.GetUserTimeline(max_id = max_id,screen_name = screen_name, count = 200, include_rts = False)
	for s in statuses:
		if( s.truncated == False   ):
			text = s.text
			text = re.sub(tag_pattern,"",text)
			text = re.sub(re_links_pattern,"",text)
			text = text.encode('ascii', 'ignore')
			text = text + '\n'
		if( len(text.split()) >3 ):
			f.write(text)
	return [statuses[-1].id,len(statuses)]


def get_all_stream_per_user(screen_name):

	with open(screen_name + '.txt', 'w') as f:
		t = 0
		max_id = None
		while(t < tweet_cnt):
			max_id, cnt = get_one_stream_per_user(api,screen_name,f,max_id)
			#print max_id
			t += cnt

for screen_name in screen_names:
	get_all_stream_per_user(screen_name)
	print 'pulled data for' + screen_name

