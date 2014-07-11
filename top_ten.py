import sys
import json

def read_tweet_hashtag(tweet_line):
	""" convert json line to tweet text """
	tweet = json.loads(tweet_line)
	tweet_hashtags = []
	try:
		tweet_hashtags_object_list = tweet['entities']['hashtags']
		for hashtag_object in tweet_hashtags_object_list:
			tweet_hashtags.append(hashtag_object['text'].encode('utf-8'))
	except:
		pass		
	return tweet_hashtags 
	
	
def print_dictionary(dictionary):
	for key in dictionary.keys():
		print key," ",dictionary[key]


def main():
	tweet_file = open(sys.argv[1])
	hashtags_dict = {}
	for line in tweet_file.readlines():
		tweet_hashtags = read_tweet_hashtag(line)
		for hashtag in tweet_hashtags:
			if hashtag in hashtags_dict.keys():
				hashtags_dict[hashtag] += 1
			else:
				hashtags_dict[hashtag] = 1
	print_dictionary(hashtags_dict)
if __name__ == '__main__':
    main()
