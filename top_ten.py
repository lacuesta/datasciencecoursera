import sys
import json

def read_tweet_hashtag(tweet_line):
	""" convert json line to hashtags list """
	tweet = json.loads(tweet_line)
	tweet_hashtags = []
	try:
		tweet_hashtags_object_list = tweet['entities']['hashtags']
		for hashtag_object in tweet_hashtags_object_list:
			tweet_hashtags.append(hashtag_object['text'].encode('utf-8'))
	except:
		pass		
	return tweet_hashtags 
	
	

def sort_dictionary(dictionary):
	""" create a list of top ten hashtags from the dictionary """
	sorted_list = []
	for w in sorted(dictionary, key=dictionary.get, reverse=True):
		sorted_list.append(w+" "+str(dictionary[w]))
	return sorted_list[0:10]
  	
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
	#print_dictionary(hashtags_dict)
	sorted_list = sort_dictionary(hashtags_dict)
	for line in sorted_list:
		print line
if __name__ == '__main__':
    main()
